"""Fetch upcoming/recent agenda documents from non-Legistar platforms and save their text.

Granicus (ViewPublisher RSS) and CivicClerk (public OData API) publish whole agenda
packets as PDFs rather than structured items, so we save text per meeting and let the
triage step pull out the on-topic items.

Usage: python3 -m meetwatch.agendas
"""

import datetime as dt
import html
import json
import pathlib
import re
import subprocess
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
TOPIC = re.compile(r"data ?cent|solar|photovolt|battery|energy storage|\bbess\b|substation|transmission|moratorium|hyperscale|technology (park|campus)", re.I)

SOURCES = {
    "frederick-va": {"kind": "granicus", "host": "fcva", "view_id": 1},
    "prince-william-va": {"kind": "granicus", "host": "pwcgov", "view_id": 23},
    "spotsylvania-va": {"kind": "civicclerk", "tenant": "spotsylvaniacova"},
}


def s3_path_style(url):
    # Granicus's bucket name has an underscore, which breaks TLS on virtual-host S3 URLs.
    return re.sub(r"https://([a-z0-9_]+)\.s3\.amazonaws\.com/", r"https://s3.amazonaws.com/\1/", url)


class _Redirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return super().redirect_request(req, fp, code, msg, headers, s3_path_style(newurl))


_opener = urllib.request.build_opener(_Redirect)


def fetch(url, binary=False, retries=4):
    req = urllib.request.Request(s3_path_style(url), headers={"User-Agent": UA})
    for attempt in range(retries):
        try:
            with _opener.open(req, timeout=90) as r:
                body = r.read()
            break
        except (ConnectionError, urllib.error.URLError):
            if attempt == retries - 1:
                raise
            time.sleep(5 * (attempt + 1))
    return body if binary else body.decode("utf-8", "replace")


def pdf_to_text(pdf_bytes, dest):
    pdf = dest.with_suffix(".pdf")
    pdf.write_bytes(pdf_bytes)
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    dest.write_text(text)
    return text


def on_topic_lines(text, context=2):
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines):
        if TOPIC.search(line):
            hits.append("\n".join(l.strip() for l in lines[max(0, i - context): i + context + 1] if l.strip()))
    return hits


def granicus(name, host, view_id, window):
    rss = fetch(f"https://{host}.granicus.com/ViewPublisherRSS.php?view_id={view_id}&mode=agendas")
    meetings = []
    for item in ET.fromstring(rss).iter("item"):
        title, link = item.findtext("title"), html.unescape(item.findtext("link") or "")
        m = re.search(r"(\w{3} \d{1,2}, \d{4})", title or "")
        if not m:
            continue
        date = dt.datetime.strptime(m.group(1), "%b %d, %Y").date()
        if not (window[0] <= date <= window[1]):
            continue
        # AgendaViewer either redirects straight to the PDF or serves an HTML agenda.
        meetings.append({"title": title, "date": date.isoformat(), "url": link, "pdf": link})
    return meetings


def civicclerk(name, tenant, window):
    api = f"https://{tenant}.api.civicclerk.com/v1"
    url = (f"{api}/Events/GetEventsList(fromDate='{window[0]}',toDate='{window[1]}',categoryIds=%5B%5D,"
           "skip=0,sortDescending=false,cursorId=0)")
    meetings = []
    for e in json.loads(fetch(url))["items"]:
        agenda = next((f for f in e.get("publishedFiles", []) if f.get("type") in ("Agenda", "Agenda Packet")), None)
        meetings.append({
            "title": e["eventName"],
            "date": e["eventDate"][:10],
            "url": f"https://{tenant}.portal.civicclerk.com/event/{e['id']}/overview",
            "pdf": f"{api}/Meetings/GetMeetingFileStream(fileId={agenda['fileId']},plainText=false)" if agenda else None,
        })
    return meetings


def main():
    today = dt.date.today()
    window = (today - dt.timedelta(days=45), today + dt.timedelta(days=60))
    for name, src in SOURCES.items():
        out_dir = DATA / name / "docs"
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            meetings = granicus(name, src["host"], src["view_id"], window) if src["kind"] == "granicus" else civicclerk(name, src["tenant"], window)
        except Exception as e:
            print(f"{name}: failed to list meetings: {e}")
            continue
        for m in meetings:
            slug = re.sub(r"[^a-z0-9]+", "-", f"{m['date']}-{m['title']}".lower())[:80]
            if not m.get("pdf"):
                m["status"] = "agenda not posted yet"
                continue
            try:
                body = fetch(m["pdf"], binary=True)
                if body[:4] == b"%PDF":
                    text = pdf_to_text(body, out_dir / f"{slug}.txt")
                else:
                    text = html.unescape(re.sub(r"<[^>]+>", " ", body.decode("utf-8", "replace")))
                    (out_dir / f"{slug}.txt").write_text(text)
                m["chars"] = len(text)
                m["hits"] = on_topic_lines(text)
            except Exception as e:
                m["error"] = str(e)
        on_topic = [m for m in meetings if m.get("hits")]
        (DATA / f"{name}.json").write_text(json.dumps({"source": src, "window": [str(w) for w in window], "meetings": meetings}, indent=1))
        print(f"{name}: {len(meetings)} meetings in window, {len(on_topic)} with on-topic text")


if __name__ == "__main__":
    main()
