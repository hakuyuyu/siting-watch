# Siting Watch (MeetWatch) — 72-hour test kit

- `meetwatch/legistar.py`, `meetwatch/collect.py` — pull on-topic matters, votes, attachments and upcoming meetings from Legistar clients (pima, dekalbcountyga, louisville, princegeorgescountymd, ...): `python3 -m meetwatch.collect pima louisville --since 2026-06-01`
- `meetwatch/agendas.py` — agenda/minutes text from Granicus (Frederick VA, Prince William VA) and CivicClerk (Spotsylvania VA): `python3 -m meetwatch.agendas`
- Loudoun (eScribe): agenda pages parse; packet PDFs are behind a bot check (403) and need a headless browser.
- Triage and the brief are written by an LLM over `data/`, then checked claim by claim (`sample/accuracy-check.md`).
- `research/jurisdictions.md` — which counties are active and how each publishes.
- `sample/` — the customer-facing sample brief and its accuracy check.
- `outreach/` — prospects (55 companies), plan, email templates, tracking sheet.
