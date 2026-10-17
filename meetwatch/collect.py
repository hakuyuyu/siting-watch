"""Collect candidate items for a set of Legistar jurisdictions into data/<client>.json.

Usage: python3 -m meetwatch.collect pima phoenix dekalbcountyga --since 2026-06-01
Then the triage step (an LLM or a person) decides which items are real land-use
decisions about data centers / energy and writes the weekly brief.
"""

import argparse
import json
import pathlib
import re
import subprocess
import urllib.request

from . import legistar

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOPIC = re.compile(r"data ?cent|solar|photovolt|battery|energy storage|\bbess\b|substation|transmission|moratorium|hyperscale", re.I)


def pdf_text(url, dest):
    if dest.exists():
        return dest.read_text(errors="replace")
    pdf = dest.with_suffix(".pdf")
    req = urllib.request.Request(url, headers={"User-Agent": legistar.UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        pdf.write_bytes(r.read())
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    dest.write_text(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clients", nargs="+")
    ap.add_argument("--since", default="2026-06-01")
    ap.add_argument("--max-attachment-chars", type=int, default=6000)
    args = ap.parse_args()

    for client in args.clients:
        cdir = DATA / client
        (cdir / "docs").mkdir(parents=True, exist_ok=True)
        items = []
        for m in legistar.matters(client, args.since):
            # Generic zoning keywords match a lot; keep those only if the title is on-topic.
            if not TOPIC.search(m.get("MatterTitle") or ""):
                continue
            item = legistar.enrich(client, m)
            for a in item["attachments"][:4]:
                try:
                    text = pdf_text(a["url"], cdir / "docs" / f"{item['id']}-{re.sub(r'[^A-Za-z0-9]+', '_', a['name'])[:60]}.txt")
                    a["excerpt"] = text[: args.max_attachment_chars]
                except Exception as e:
                    a["error"] = str(e)
            items.append(item)

        events = legistar.upcoming_events(client)
        for e in events:
            e["items"] = [i for i in legistar.event_items(client, e["id"]) if TOPIC.search(i["title"])]
        events = [e for e in events if e["items"]]

        out = {"client": client, "since": args.since, "matters": items, "upcoming": events}
        (DATA / f"{client}.json").write_text(json.dumps(out, indent=1))
        print(f"{client}: {len(items)} on-topic matters, {len(events)} upcoming meetings with on-topic items")


if __name__ == "__main__":
    main()
