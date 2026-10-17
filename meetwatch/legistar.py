"""Pull land-use items for data centers / energy from a Legistar client's public Web API.

Legistar's OData filter is case-sensitive substring matching on titles, so we query
each keyword in a couple of casings and de-duplicate by MatterId.
"""

import datetime as dt
import json
import time
import urllib.parse
import urllib.request

API = "https://webapi.legistar.com/v1"
UA = "Mozilla/5.0 (compatible; MeetWatch/0.1)"

KEYWORDS = [
    "data center", "Data Center", "DATA CENTER", "datacenter",
    "solar", "Solar", "SOLAR", "photovoltaic",
    "battery", "Battery", "energy storage", "Energy Storage", "BESS",
    "substation", "Substation", "transmission line", "Transmission Line",
    "moratorium", "Moratorium",
    "rezoning", "Rezoning", "REZONING", "special use permit", "Special Use Permit",
    "conditional use", "Conditional Use",
]


def get(path, params=None, retries=3):
    url = f"{API}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, safe="$'(),:", quote_via=urllib.parse.quote)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def matters(client, since, keywords=KEYWORDS):
    found = {}
    for kw in keywords:
        flt = f"substringof('{kw}',MatterTitle) and MatterIntroDate ge datetime'{since}'"
        for m in get(f"{client}/matters", {"$filter": flt, "$top": 500}):
            found.setdefault(m["MatterId"], m)
        time.sleep(0.3)
    return list(found.values())


def enrich(client, m):
    mid = m["MatterId"]
    hist = get(f"{client}/matters/{mid}/histories")
    atts = get(f"{client}/matters/{mid}/attachments")
    return {
        "client": client,
        "id": mid,
        "file": m.get("MatterFile"),
        "title": (m.get("MatterTitle") or "").strip(),
        "type": m.get("MatterTypeName"),
        "status": m.get("MatterStatusName"),
        "body": m.get("MatterBodyName"),
        "intro_date": (m.get("MatterIntroDate") or "")[:10],
        "agenda_date": (m.get("MatterAgendaDate") or "")[:10],
        "history": [
            {
                "date": (h.get("MatterHistoryActionDate") or "")[:10],
                "body": h.get("MatterHistoryActionBodyName"),
                "action": h.get("MatterHistoryActionName"),
                "result": h.get("MatterHistoryPassedFlagName"),
                "tally": h.get("MatterHistoryTally"),
                "text": h.get("MatterHistoryActionText"),
            }
            for h in sorted(hist, key=lambda h: h.get("MatterHistoryActionDate") or "")
        ],
        "attachments": [{"name": a["MatterAttachmentName"], "url": a["MatterAttachmentHyperlink"]} for a in atts],
        "url": f"https://{client}.legistar.com/LegislationDetail.aspx?ID={mid}&GUID={m.get('MatterGuid', '')}",
    }


def upcoming_events(client, days=60):
    today = dt.date.today().isoformat()
    end = (dt.date.today() + dt.timedelta(days=days)).isoformat()
    flt = f"EventDate ge datetime'{today}' and EventDate le datetime'{end}'"
    events = get(f"{client}/events", {"$filter": flt, "$orderby": "EventDate", "$top": 200})
    return [
        {
            "id": e["EventId"],
            "date": (e.get("EventDate") or "")[:10],
            "time": e.get("EventTime"),
            "body": e.get("EventBodyName"),
            "agenda_pdf": e.get("EventAgendaFile"),
            "url": e.get("EventInSiteURL"),
        }
        for e in events
    ]


def event_items(client, event_id):
    items = get(f"{client}/events/{event_id}/eventitems", {"AgendaNote": 1, "MinutesNote": 1, "Attachments": 1})
    return [
        {
            "title": (i.get("EventItemTitle") or "").strip(),
            "matter_id": i.get("EventItemMatterId"),
            "matter_file": i.get("EventItemMatterFile"),
            "action": i.get("EventItemActionName"),
            "result": i.get("EventItemPassedFlagName"),
            "tally": i.get("EventItemTally"),
            "attachments": [
                {"name": a.get("MatterAttachmentName"), "url": a.get("MatterAttachmentHyperlink")}
                for a in (i.get("EventItemMatterAttachments") or [])
            ],
        }
        for i in items
    ]
