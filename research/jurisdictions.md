# Meeting Watch: candidate jurisdictions (data centers / BESS / substations / transmission)

Research date: **2026-10-16**. Every agenda, API and portal URL below was fetched on that date (curl with a browser User-Agent) unless marked otherwise. News claims are cited with publication dates. "Upcoming" means scheduled on or after 2026-10-16.

---

## Summary ranking

Scores run 1–5, where 5 is best. "Activity" means live land-use decisions on the calendar for Oct–Dec 2026. "Machine access" means how easily the agendas can be pulled programmatically, based on what was actually fetched.

| Rank | Jurisdiction | Body | Activity Oct–Dec 2026 | Machine access | Platform / key |
|---|---|---|---|---|---|
| 1 | **Frederick County, VA** | Board of Supervisors + Planning Commission | 5: two data center applications (CUP + 220-ac rezoning) at the BOS on **Oct 28**; a BESS zoning text amendment at the PC on **Oct 21** | 4: Granicus RSS feed, and agenda links resolve to PDFs on S3 | Granicus `fcva`, `view_id=1` |
| 2 | **Spotsylvania County, VA** | Board of Supervisors + Planning Commission | 5: 555-ac Crossroads Technology Campus SUP (PC recommended approval 4-2) awaits the BOS; transmission-line resolution; BESS briefing; Comprehensive Plan update | 5: CivicClerk public OData API with structured agenda items and PDF download | CivicClerk tenant `spotsylvaniacova` |
| 3 | **Loudoun County, VA** | Board of Supervisors + Planning Commission | 5: Data center/substation **pause resolution on Oct 20**; Golden Substation SPEX moved to **Nov 5**; Quantum Park data center ZCPA on Oct 20 | 4: eScribe JSON calendar endpoint works and agenda HTML is parseable; **PDF FileStream is behind a bot check** | eScribe `pub-loudoun`; Granicus `loudoun` view_id=77 for PC video |
| 4 | **Louisville Metro, KY** | Metro Council Planning & Zoning Committee | 4: Data center Land Development Code ordinance O-251-26 (25-LDC-0014) held Oct 6; P&Z Committee **Oct 20** has four data center discussion items, including a "potential committee vote" | 5: Legistar Web API works (events, matters, histories, attachments) | Legistar `louisville` |
| 5 | **DeKalb County, GA** | Board of Commissioners | 4: Data center definitions ordinance (2026-1273) **deferred with a substitute on Oct 13**, so it comes back in Oct/Nov; moratorium runs to Mar 30, 2027; lawsuit pending | 5: Legistar Web API works | Legistar `dekalbcountyga` |
| 6 | **Pima County, AZ** | Board of Supervisors (+ P&Z Commission) | 3–4: 120-day moratorium adopted Sep 22, 2026; zoning code text amendment due at the P&Z Commission "October hearing" and at the BOS before the moratorium expires (~Jan 2027) | 4: Legistar Web API works for the BOS; P&Z Commission is **not** in Legistar | Legistar `pima` |
| 7 | **Prince George's County, MD** | County Council (PHED Committee) | 3: CB-085-2026 (data centers in rural/residential zones) held in committee Sep 21; CB-103-2026 (data center tax exemption) referred | 5: Legistar Web API works | Legistar `princegeorgescountymd` |
| 8 | **Stafford County, VA** | Planning Commission → Board of Supervisors | 5: Kings Corridor Technology Campus (Forest Lane, Simms Farm, Sisson N/S; >1,500 ac) PC hearing moved to **Nov 18**; Accokeek Creek rezoning approved Oct 8 (4-3) | 1: no machine-readable source found (details below) | YouTube + OnBase records portal |

**Recommended top 4 for the sample report:** Frederick County VA, Spotsylvania County VA, Loudoun County VA and Louisville Metro KY. Each has a dated hearing in Oct–Nov 2026 and a source I fetched successfully. DeKalb County GA is a strong #5 if a non-Virginia, Legistar-native example is wanted.

---

## 1. Frederick County, Virginia (Winchester area)

**Bodies:** Board of Supervisors (BOS); Planning Commission (PC).

### Active items
- **BOS, Wed Oct 28, 2026, Item 12.A: Conditional Use Permit #03-26, Winchester Gateway LLC.** Data center on 71.85 ± ac of M1 (Light Industrial) land at Apple Valley Rd (Rt 652) / Middle Rd (Rt 628), bounded by Rt 37. PIN 63-A-80I, Back Creek District. Public hearing. *(Source: BOS 10/28/26 agenda PDF, below.)*
- **BOS, Oct 28, 2026, Item 12.B: Rezoning #04-26, Virginia Technology Park.** Rezone 220.06 ± ac from RA to TM (Technology-Manufacturing Park) with proffers for data center uses. South of Rest Church Rd, Clear Brook; PINs 33-A-89, 33-A-90, 33-9-1A; Stonewall District. Public hearing.
  - The applicant is Equus Capital Partners. The plan is 10–11 data center buildings, 3 substation pads and up to 288 generators. The **PC voted 10-0 to recommend denial.** A predecessor proposal on the same parcels ("Fruit Hill") was rejected by the BOS 4-3 in Sep 2024. Source: Northern Virginia Daily, "Planners vote down Clear Brook data center campus" (undated in fetch; published before the Oct 28 BOS meeting): https://www.nvdaily.com/nvdaily/planners-vote-down-clear-brook-data-center-campus/article_8e6c14d9-ce6f-51fd-9c04-e46953e6b6e5.html
- **PC, Wed Oct 21, 2026, Item 8.B: Zoning Ordinance amendment (Ch. 165).** Allows **Battery Energy Storage Systems (BESS)** as a conditional use in certain districts and adds BESS regulations (Articles VI, VII, XI). Public hearing. *(Source: PC 10/21/26 agenda PDF.)*

### How it publishes (verified)
- **Granicus ViewPublisher:** https://fcva.granicus.com/ViewPublisher.php?view_id=1. The Planning Commission-only view is `view_id=4`.
- **RSS (machine-readable list):** https://fcva.granicus.com/ViewPublisherRSS.php?view_id=1&mode=agendas
  - Returned on 10/16: "Board of Supervisors - Oct 28, 2026", "Planning Commission - Oct 21, 2026", "Board of Supervisors - Oct 14, 2026", and others.
- **Upcoming agenda (BOS 10/28/26):** https://fcva.granicus.com/AgendaViewer.php?view_id=1&event_id=1142 redirects to the PDF https://granicus_production_attachments.s3.amazonaws.com/fcva/68c28a1e7062a2350dc5a061917a60af0.pdf
- **PC 10/21/26 agenda:** https://fcva.granicus.com/AgendaViewer.php?view_id=1&event_id=996 redirects to https://granicus_production_attachments.s3.amazonaws.com/fcva/79f569f4804d3e27d52bc2cda207648f0.pdf
- **Past meeting video and agenda:** `AgendaViewer.php?view_id=1&clip_id=368` (BOS Oct 14, 2026).
- **Notes:** The county website `www.fcva.us` returned HTTP 403 to curl. The Granicus host works without restriction. There is no Legistar instance (the client names `fcva` and `frederickcountyva` are not set up).

---

## 2. Spotsylvania County, Virginia

**Bodies:** Board of Supervisors; Planning Commission.

### Active items
- **SUP26-0003 "Crossroads Technology Campus" (RCK Digital Crossroads LLC).**
  - Data center campus SUP on ~555 ac of I-1/I-2 land on the north side of Eagle Dr (Rt 736), Lee Hill School Dr and Mills Dr (Rt 17), next to the CSX line. Tax parcels 37-A-20, 37-A-21, 37-A-17D; Lee Hill District.
  - Up to **2,087,000 sf** of data center buildings and **three electrical substations**. The PC also took a separate §15.2-2232 comprehensive-plan conformance vote on the substations.
  - Source: CivicClerk agenda items for the PC meeting of 2026-09-16 (agendaId 376).
  - **PC voted 4-2 to recommend approval.** Source: WJLA, 2026-09-21, https://wjla.com/news/local/spotsylvania-planning-commission-mega-data-center-complex-55-acres-amazon-web-services-data-center-county-mega-crossroads-technology-campus-wildlife-trees-substations-noise-generators-residents-land-property-taxes
  - WJLA reports the end user is AWS; other outlets name Kettler/RCK. **The BOS public hearing is not yet on a posted agenda.** Candidate BOS dates from the API are Oct 27, Nov 17 and Dec 8, 2026.
- **BOS 2026-10-13:** a resolution asking electric utilities, the SCC and the CTB to place new **transmission lines** in existing right-of-way (agendaId 353).
- **PC 2026-10-21:** a "Dominion and REC Battery Energy Storage System" presentation (agendaId 378).
- **PC 2026-10-07:** CPA25-0002, the 2026 Comprehensive Plan major 5-year update (agendaId 377).
- **Context:** organized opposition (Safeguard Spotsy) and requests for a moratorium. WJLA, "Spotsylvania residents push back on data centers…": https://wjla.com/news/local/story/data-center-spotsylvania-county-centers-virginia-low-tax-prince-william-stafford-lee-hill-niehbrohood-residents-react-support-condemn-environmental-attorney-industrial-supervisors

### How it publishes (verified)
- **CivicClerk public portal:** https://spotsylvaniacova.portal.civicclerk.com/
- **CivicClerk public API (OData, no auth).** Base URL: `https://spotsylvaniacova.api.civicclerk.com/v1`
  - **Categories:** `GET /v1/EventCategories` returns JSON, e.g. id 26 "Board of Supervisors".
  - **Events in a date range:** `GET /v1/Events/GetEventsList(fromDate='2026-09-15T00:00:00.000Z',toDate='2026-12-31T23:59:59.000Z',categoryIds=[],skip=0,sortDescending=false,cursorId=0)`
    - The `[]` must be URL-encoded as `%5B%5D`.
    - Returns `{"hasMore":false,"items":[…]}` with `id`, `agendaId`, `eventName`, `startDateTime`, `categoryName` and `publishedFiles[]`.
    - On 10/16 this returned 12 events, including BOS 2026-10-27 (event 795), 11-17 (796) and 12-08 (797), and PC 11-04, 11-18, 12-02 and 12-16.
  - **Full structured agenda:** `GET /v1/Meetings/{agendaId}`, e.g. `/v1/Meetings/376`. Returns nested `items[].childItems[]` with `agendaObjectItemName` and `agendaObjectItemDescription`.
  - **Agenda PDF:** `GET /v1/Meetings/GetMeetingFileStream(fileId=2818,plainText=false)` returned `200 application/pdf` (BOS Agenda, 2026-10-13). Human URL pattern: `https://spotsylvaniacova.portal.civicclerk.com/event/794/files/attachment/<fileId>`.
- **Note:** the CivicClerk tenant is derived from the portal subdomain. The portal shell loads for any subdomain, so I checked tenants through `/v1/EventCategories`. Stafford's `staffordcountyva` tenant returned 404, meaning it is not a real tenant.

---

## 3. Loudoun County, Virginia

**Bodies:** Board of Supervisors; Planning Commission.

### Active items
- **BOS Business Meeting, Tue Oct 20, 2026, Item 14.p: "Resolution to Pause Board of Supervisors Consideration of Legislative Applications for Data Centers and Substations."**
  - Pauses Board action for up to 12 months from the date each application first went to the Planning Commission. The aim is to apply **Phase 2 of the Data Centers Standards and Locations ZOAM and CPAM** to those applications.
  - The pause is effective retroactively to Sep 15, 2026, and applications do not go inactive.
  - Source: Oct 20 eScribe agenda.
  - Background: the BOS voted 7-1-1 on Sep 15, 2026 to advance the pause, with a separate "grid reliability" substation exception. WJLA, 2026-09-16: https://wjla.com/news/local/loudoun-county-data-centers-development-applications-board-supervisors-pause-northern-virginia-regulations-leesburg-catoctin-grid-reliability-dominion-energy-merger-power-lines-laws
  - County release: https://www.loudoun.gov/CivicAlerts.aspx?AID=10874
- **Item 14.o: Golden Substation (LEGI-2025-0012; SPEX-2025-0032, -0033, -0137), Sterling District.** A motion to move BOS review from the **Dec 1** to the **Nov 5, 2026** business meeting.
- **Item 14.j: Quantum Park, ZCPA-2023-0008 (LEGI-2023-0097), Broad Run District.** Amends the CDP and proffers (ZMAP-1998-0003 WorldCom/Northern Virginia Campus; ZCPA-2017-0009) to expand the building envelope for already-approved **data center, utility substation and office** floor area.
- **Upcoming BOS meetings** (from the eScribe API): Nov 5, Nov 12 (public hearing), Nov 17, Dec 1, Dec 9 (public hearing), Dec 15.
- **Upcoming PC meetings** (Granicus): Oct 27, Nov 19 and Dec 17 public hearings.

### How it publishes (verified)
- **eScribe** became the BOS agenda system by Sep 2026. Portal: https://pub-loudoun.escribemeetings.com/
  - **JSON calendar endpoint (works):**
    `POST https://pub-loudoun.escribemeetings.com/MeetingsCalendarView.aspx/GetCalendarMeetings` with header `Content-Type: application/json` and body `{"calendarStartDate":"2026-09-01","calendarEndDate":"2026-12-31"}`
  - It returns `d[]` with `MeetingName`, `StartDate`, `ID` and `MeetingDocumentLink[]`. On 10/16 that was 20 meetings across BOS, TLUC and FGOEDC.
  - **HTML agenda (parseable):** https://pub-loudoun.escribemeetings.com/Meeting.aspx?Id=22e65f92-8862-46da-afba-f594bd09768a&Agenda=Agenda&lang=English (BOS, Oct 20, 2026)
  - **Agenda PDF:** https://pub-loudoun.escribemeetings.com/FileStream.ashx?DocumentId=1946
    - **Caveat:** from curl this returned HTTP 403 with a "Verifying your browser — eScribe" interstitial, even with cookies and a referer. A real browser or headless browser will probably be needed for PDFs. Parse the HTML agenda instead.
- **Granicus** (video, minutes, PC agendas): https://loudoun.granicus.com/ViewPublisher.php?view_id=77
  - RSS: https://loudoun.granicus.com/ViewPublisherRSS.php?view_id=77&mode=agendas
  - The feed's latest BOS entry is July 2026, which suggests BOS agendas moved to eScribe. PC entries continue (e.g. PC Work Session Oct 8, 2026, `clip_id=8264`, with MP3/MP4 on archive-video.granicus.com).
- **YouTube:** https://www.youtube.com/user/loudouncountyva
- **Index page:** https://www.loudoun.gov/meetings embeds both the eScribe portal and Granicus `view_id=92`.
- **No Legistar** (client `loudoun` is not set up).

---

## 4. Louisville / Jefferson County Metro, Kentucky

**Bodies:** Metro Council and its Planning and Zoning Committee; Louisville Metro Planning Commission.

### Active items
- **O-251-26: "An Ordinance Amending the Louisville Metro Land Development Code Regarding Data Centers (Case No. 25-LDC-0014)"** (Legistar MatterId 65905), sponsored by Andrew Owen (D-9).
  - Legistar history: assigned 2026-09-10; at P&Z Committee 2026-09-15, "recommended for approval" and then "postponed"; P&Z Committee **2026-10-06 "held"**.
  - Oct 6 action summary: https://legistar2.granicus.com/louisville/meetings/2026/10/12716_M_Planning_and_Zoning_Committee_26-10-06_Action_Summary.pdf
- **P&Z Committee, Tue Oct 20, 2026, 1:00 PM (EventId 11235; agenda not yet posted on 10/16).** Four matters filed 2026-10-16 (MatterIds 66303–66306) are tentatively scheduled:
  - "Tentative Data Center Discussion" on electricity, water, waste heat, noise and generators
  - zoning classifications, the CUP process and size caps/setbacks
  - accessory data centers, telecom hotels and decommissioning
  - "Review of recommendations and general discussion; **potential committee vote**"
- **Planning Commission** held hearings and business sessions on the text amendment on Jul 24, Jul 31, Aug 7, Aug 14 and Aug 19, 2026, and voted 5-3 to recommend it. The draft caps facility size and sets permits, noise and water standards. Spectrum News 1, 2026-09-04: https://spectrumnews1.com/ky/louisville/news/2026/09/04/data-center-code-amendments
- **Moratorium:** the P&Z Committee approved a 180-day moratorium on new hyperscale data centers 7-1. WAVE, 2026-08-04: https://www.wave3.com/2026/08/04/louisville-metro-committee-approves-180-day-moratorium-new-data-centers/
- **Office of Planning data center page:** https://louisvilleky.gov/government/office-planning/data-centers

### How it publishes (verified)
- **Legistar client:** `louisville`. Web portal: https://louisville.legistar.com/
- `curl "https://webapi.legistar.com/v1/louisville/events?$filter=EventDate ge datetime'2026-10-14'&$orderby=EventDate"` returned 30+ events (Metro Council 10/15, Planning Commission 10/15, P&Z Committee 10/20, …) with `EventAgendaFile` PDFs.
- **Matter histories:** `/v1/louisville/matters/65905/histories` works.
- **Recent agenda PDF:** https://legistar2.granicus.com/louisville/meetings/2026/10/12716_A_Planning_and_Zoning_Committee_26-10-06_Meeting_Agenda.pdf
- **Video:** `EventVideoPath` is null in the API. Metro TV/YouTube video is not linked through Legistar (not verified further).

---

## 5. DeKalb County, Georgia

**Body:** Board of Commissioners (BOC), including the BOC Zoning Meeting and Committee of the Whole.

### Active items
- **2026-1273 (MatterId 17745):** an ordinance amending Chapter 27 to set **Data Center Definitions and Data Center Classifications**.
  - BOC 2026-09-29: "Normal Course". BOC **2026-10-13: "Deferred substitute"**, so it is expected back at a following BOC meeting. Next dates are not yet posted in the API.
- **2026-1109 (MatterId 17581):** resolution **extending the data center moratorium to 11:59 pm, March 30, 2027**. Approved by the BOC on 2026-07-07.
  - Covers SLUPs, rezonings, LDPs, building permits, business licenses and COs.
  - Attachment: https://dekalbcountyga.legistar1.com/dekalbcountyga/attachments/0ce6cc71-d298-42f5-b32f-d6270f2533f8.pdf
- **Earlier history:** the BOC denied the land-use data center regulations 7-0 on Jun 23, 2026. Atlanta News First, 2026-06-26: https://www.atlantanewsfirst.com/2026/06/26/dekalb-county-rejects-data-center-regulations/
- **Litigation:** Shadowbox Studios and an affiliate sued over the moratorium. Atlanta News First, 2026-08-13: https://www.atlantanewsfirst.com/2026/08/13/dekalb-county-sued-over-moratorium-new-data-centers/

### How it publishes (verified)
- **Legistar client:** `dekalbcountyga`. Portal: https://dekalbcountyga.legistar.com/
- `curl "https://webapi.legistar.com/v1/dekalbcountyga/events?$top=5&$orderby=EventDate desc"` returned BOC 2026-10-13, CoW 2026-10-06, BOC 2026-09-29, the BOC Zoning Meeting 2026-09-24, and others.
- **Recent agenda PDF:** https://dekalbcountyga.legistar1.com/dekalbcountyga/meetings/2026/10/4494_A_Board_of_Commissioners_26-10-13_Agenda.pdf

---

## 6. Pima County, Arizona (Tucson area; Project Blue)

**Bodies:** Board of Supervisors; Planning & Zoning Commission.

### Active items
- **Resolution 2026-56, Moratorium on Data Center Development** (File ID 20801, MatterId 21867). **Approved 2026-09-22.**
  - Runs 120 days in unincorporated Pima County, ending about late January 2027.
  - Exhibit A work plan: Development Services presents a data center **zoning code text amendment to the P&Z Commission "at the October hearing"**. The amendment then goes to the BOS for adoption **before the moratorium expires**.
  - Resolution PDF: https://legistar.granicus.com/pima/attachments/12c764f2-f432-4394-ade0-5a388cc6cdbd.pdf
  - KJZZ, 2026-09-23: https://www.kjzz.org/fronteras-desk/2026-09-23/pima-county-passes-120-day-moratorium-on-future-data-center-projects
- **Background:** Project Blue (Beale Infrastructure / Humphrey's Peak Properties) binding MOA approved 3-2 in Dec 2025 (MatterId 20735). Separately, "Project Gravel" is proposed on ~160 ac south of Tucson (per KJZZ).
- No data center item appears on the 2026-10-20 BOS agenda (checked through the API eventitems).

### How it publishes (verified)
- **Legistar client:** `pima`. Portal: https://pima.legistar.com/
- `curl "https://webapi.legistar.com/v1/pima/events?$top=5&$orderby=EventDate desc"` returned BOS 2026-10-20, 10-13 (×2), 09-22 (×2) and 09-08, each with `EventAgendaFile`.
- **Recent agenda PDF:** https://legistar.granicus.com/pima/meetings/2026/10/1872_A_Board_of_Supervisors_26-10-20_Online_Agenda.pdf
- **Bodies in Legistar:** only the BOS, BOS Addendum and BOS Study Sessions. **The P&Z Commission hearing on the text amendment will not appear in Legistar.** It needs Pima Development Services' own P&Z agenda page (not verified here).

---

## 7. Prince George's County, Maryland

**Body:** County Council, including its Planning, Housing and Economic Development (PHED) Committee. The council also sits as the District Council.

### Active items
- **CB-085-2026:** "Use Regulations – Qualified Data Centers". Would permit qualified data centers in certain Rural/Agricultural and Residential base zones and repeal the detailed-site-plan exemption.
  - M-NCPPC technical staff opposed it (2026-07-14). The Planning Board took no position (2026-07-28).
  - Presented and referred 2026-09-01; **held in the PHED Committee 2026-09-21** (Legistar history).
- **CB-103-2026:** "Qualified Data Centers – Personal Property Tax Exemption" restructuring. Presented and referred 2026-09-01.
- **Context:** the council's earlier resolution paused data center approvals pending regulation. NBC Washington: https://www.nbcwashington.com/news/local/prince-georges-county/zoning-legislation-puts-prince-georges-data-center-moratorium-in-question/4132791/

### How it publishes (verified)
- **Legistar client:** `princegeorgescountymd`. Portal: https://princegeorgescountymd.legistar.com/
- The API returned County Council 2026-10-20 and District Council 2026-10-20, among others.
- **Agenda PDF:** https://princegeorgescountymd.legistar1.com/princegeorgescountymd/meetings/2026/10/12219_A_County_Council_26-10-20_Meeting_Agenda.pdf

---

## 8. Stafford County, Virginia: high activity, poor machine access

**Bodies:** Planning Commission → Board of Supervisors.

### Active items
- **Kings Corridor Technology Campus:** Forest Lane (~850 ac, rezoning A-1/M-1 to M-2; applicant Real Estate Pursuits 2 LC), Simms Farm, and Sisson North and South. Together they cover more than 1,500 ac along Kings Highway (Rt 3).
  - Staff recommended denial of most of the applications.
  - **The PC hearing was moved from Oct 14 to Nov 18, 2026.** Potomac Local, 2026-10-14, "Stafford cancels today's (Oct. 14, 2026) Planning Commission meeting; Kings Highway data center hearings moved to Nov. 18": https://www.potomaclocal.com/2026/10/14/stafford-cancels-oct-14-planning-commission-kings-highway-data-center-hearings-nov-18/ (from search results; the page did not resolve from this environment)
  - WJLA: https://wjla.com/newsletter-daily/stafford-county-data-center-accokeek-planning-commission-staff-denial-supervisors-residents-opposition-projects-locations-public-hearing-rappahannock-kings-corridor-technology-water
- **Accokeek Creek data center rezoning:** approved by the BOS 4-3 on Oct 8, 2026. Fredericksburg Free Lance-Star: https://fredericksburg.com/news/local/article_b221658a-b73b-4e44-b4a8-ce262f14251c.html (search result; not fetched)

### How it publishes (checked)
- **The Revize "Agenda Center" has no 2026 documents.**
  - Planning Commission page: https://www.staffordcountyva.gov/residents/connect/agenda_center/planning_commission.php (PDFs up to about 2022).
  - BOS agenda page: https://www.staffordcountyva.gov/government/elected_and_appointed_officials/board_of_supervisors/agenda_and_minutes.php (no agenda links in the static HTML).
- **OnBase public records portal:** https://pob.staffordcountyva.gov/PublicAccess/ (search form; not an API).
- **YouTube:** https://www.youtube.com/channel/UC84j3uG-l8f0ryzoojSz0zw
- **Ruled out:** no Legistar (`staffordcounty`, `staffordcountyva`), no CivicClerk tenant (`staffordcountyva` 404), no Granicus subdomain found.
- **Verdict:** good news value, but it would need manual monitoring or headless scraping.

---

## Also checked (not ranked in the top 8)

- **Legistar Web API probe** (`/v1/{client}/events?$top=1&$orderby=EventDate desc`) on 2026-10-16:
  - **Working with current data:** `pima`, `mesa`, `laramiecounty`, `dekalbcountyga`, `columbus` (OH), `phoenix`, `louisville`, `princegeorgescountymd`, `dane` (WI), `madison`, `richmondva`, `santaclara`, `sanjose`, `nashville`, `stpaul`, `austintexas`.
  - **Exists but empty:** `pwcgov` returns `[]`. Prince William County actually publishes through Granicus: https://pwcgov.granicus.com/ViewPublisher.php?view_id=23 (RSS works; BOCS Oct 20, 2026 = `event_id=3469`).
  - **Not Legistar (error "LegistarConnectionString setting is not set up"):** loudoun, culpeper, fauquier, frederickcountymd, fayettecountyga, coweta, douglascountyga, bastrop, chandler, newalbany, licking, stcharlesparish, shelbycounty, memphis, cheyenne, bessemer, hermantown, indy/indianapolis, peculiar, tucson, maricopacounty, staffordcounty.
  - **Client exists but misconfigured:** `maricopa` and `mooresville` return a different error ("Agenda Draft Status … is not setup").
- **Mesa, AZ** (Legistar `mesa`): data center cases in 2026 include ZON25-00626 "NTT Mesa PH10" (170 ac; P&Z recommended approval 2026-05-13) and ZON25-00535 "Edgecore Mesa North Campus" (43.8 ac). No Oct–Dec council date was found, and the API shows few Oct/Nov events. Lower priority.
- **Phoenix, AZ** (Legistar `phoenix`): recurring "Binding Waiver of Enforcement of the Special Permit Provisions for Data Centers" items. The latest is 5C Data Centers, adopted 2026-06-16. No live Oct–Dec item was found.
- **Columbus, OH** (Legistar `columbus`):
  - Data centers were moved to conditional use in July 2026.
  - Ordinance 2560-2026 "Large Load/High-Volume Peak User Rates" passed (introduced 2026-09-09).
  - A three-part package (behind-the-meter generation, water, decommissioning) was announced 2026-09-17 but not yet filed as legislation. Axios, 2026-09-17: https://www.axios.com/local/columbus/2026/09/17/hardin-wyche-propose-new-data-center-guardrails
  - Worth watching later.
- **Laramie County, WY** (Legistar `laramiecounty`): the API works (BOCC 2026-10-06, PC 2026-09-10) but no data center land-use matters were found. Cheyenne city annexation and moratorium petitions are covered by city sources that are not on Legistar.
- **Dane County, WI** (Legistar `dane`): an "Advisory Committee on Data Centers" meets monthly (10/08/2026 items). This is policy study rather than land-use decisions.
- **Johnson County, IA:** the BOS extended its data center moratorium to Aug 8, 2027 (Daily Iowan, 2026-10-15): https://dailyiowan.com/2026/10/15/joco-board-of-supervisors-extends-data-center-moratorium/. Platform not checked.

---

## Method notes and caveats
- All API calls were anonymous GETs (plus one POST for eScribe) through a browser User-Agent. No keys were needed. The Legistar Web API occasionally dropped connections mid-request, so a retry is needed.
- Hearing dates for items "not yet on a posted agenda" (the Spotsylvania Crossroads BOS hearing, DeKalb 2026-1273 after deferral, the Pima P&Z October hearing) are inferred from status and process. Confirm them against the next posted agenda.
- WebFetch could not resolve several news domains from this environment. Those article dates come from search-result metadata or from curl'd JSON-LD `datePublished`.
