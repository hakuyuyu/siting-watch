# Siting Watch: 72-hour outreach test

Working name "Siting Watch". Rename freely before sending.

## The offer

Weekly brief plus same-day alerts on county/city government actions that affect data center, BESS, solar, substation and transmission sites: rezonings, special/conditional use permits, moratoria, ordinance rewrites, comp plan amendments, hearing dates and vote tallies. Every line links to the primary agenda, minutes or packet.

| Plan | Price | What's included |
|---|---|---|
| Watchlist | $199/month | Up to 10 counties you pick. Weekly brief. Same-day email when a posted agenda mentions your project, your parcel or a keyword you set. |
| Portfolio | $499/month | Up to 40 counties. Everything in Watchlist, plus tracking named applicants (competitors), a hearing calendar you can export, and any new county added within 48 hours. |

Founding customers (first 10): price locked for 12 months, cancel any time, refund in the first 14 days if it isn't useful.

Before sending, create two Stripe Payment Links (monthly subscriptions, $199 and $499) and paste them below.

- Watchlist link ($199/mo): https://buy.stripe.com/aFa9AVbsZ9f22m893w9sk00
- Portfolio link ($499/mo): https://buy.stripe.com/7sY28tcx30Iwf8U6Vo9sk01

Stripe account: snowllc (live). Neither link has had a test payment.

## The test

- **Who:** 40 people from `prospects.csv`. Priority order: mid-size data center developers (land/entitlement roles), mid-size solar/storage developers (development managers), land-use attorneys, then site selectors and powered-land brokers.
- **How:** personal email where the company publishes one, otherwise a LinkedIn connection note, then a message once connected. Send from your own name and address, not a bulk tool.
- **Personalize every message** with one real item from a county they're active in. Use the evidence link in the CSV and the sample brief.
- **Attach** the sample brief (`/home/user/meetwatch/sample/siting-watch-sample-2026-10-16.md`, exported to PDF).
- **Track** every send in `tracking.csv` (columns below).

| Result at hour 72 | Decision |
|---|---|
| 2+ paid, or 5+ calls booked | Continue: onboard them by hand, add their counties, run 4 weeks |
| 3+ replies but no calls | Change the angle once (price, segment or format), run another 72 hours |
| Under 3 replies | Stop. Write down why and move on |

Also check: the sample's accuracy check must be 90%+ verified before it goes out.

## Email A: data center developers (land / entitlements)

Subject: {County} pause on data center applications

> Hi {First name},
>
> {County} {specific action, e.g. "votes Oct 20 on pausing Board action on data center and substation applications for up to 12 months, retroactive to Sep 15" or "removed data centers as a use in every zoning district on Sep 23, with only two grandfathered cases left to be heard by Oct 28"}. With {Company} active in {their market}, I figured that kind of change is something your team needs to hear about the day the agenda posts, not after the vote.
>
> I run Siting Watch: AI reads every agenda, minutes and packet in the counties you choose, a person checks it, and you get a weekly brief plus same-day alerts on rezonings, SUPs, moratoria and hearing dates, each linked to the source document. A sample covering 8 counties is attached.
>
> Founding price is $199/month for 10 counties (start here: https://buy.stripe.com/aFa9AVbsZ9f22m893w9sk00). If you'd rather judge it first, tell me which counties matter to you and I'll send this week's brief for them free.
>
> {Your name}

## Email B: solar / storage developers

Subject: BESS and solar items on {County} agendas

> Hi {First name},
>
> {County}'s planning commission {specific action, e.g. "takes up a zoning change to allow battery storage as a conditional use on Oct 21"}. Each county you develop in rewrites these rules on its own schedule, and the notice usually sits inside a 300-page packet.
>
> Siting Watch reads those packets for you. Pick up to 10 counties and you get a weekly brief plus a same-day alert when a posted agenda mentions solar, BESS, a substation, your parcel or a competitor. Every line links to the source. Sample attached.
>
> $199/month as a founding customer (start here: https://buy.stripe.com/aFa9AVbsZ9f22m893w9sk00). Or send me your county list and I'll run this week's brief for them free first.
>
> {Your name}

## Email C: land-use attorneys, site selectors, powered-land brokers

Subject: Tracking data center hearings across {state/region}

> Hi {First name},
>
> Saw {firm}'s work on {matter/market}. I've built a service that reads every agenda, minutes and packet in the counties you choose and flags data center, BESS and substation items: new applications, staff recommendations, vote tallies, moratoria, hearing dates, each linked to the primary document.
>
> Firms like yours use it to brief clients early and spot new applications by competitors. A sample covering 8 counties (Loudoun, Prince William, Frederick and Spotsylvania VA; Louisville; DeKalb; Pima; Prince George's) is attached.
>
> $199/month for 10 counties (https://buy.stripe.com/aFa9AVbsZ9f22m893w9sk00) or $499 for 40 (https://buy.stripe.com/7sY28tcx30Iwf8U6Vo9sk01). Happy to run a free brief on the counties you're working in this month first.
>
> {Your name}

Every email ends with the footer: "This is a commercial email. [Your mailing address] · Reply 'no' and I won't email again." (CAN-SPAM: cold sales email must say it is an advertisement, give a real postal address, and offer a working opt-out; there is no business-to-business exemption.) The From name and the subject line must be accurate. Honor an opt-out the same day and never email that person again.

## Follow-ups

- **Day 2:** "Quick add: {new item from that day's agendas in a county they care about}. This is the kind of thing the alert would have flagged. Want me to set up your counties?"
- **Day 3 (last):** "Last note from me. If county agenda tracking isn't a pain for your team, a one-word reply helps me too."

## LinkedIn connection note (300 characters max)

> Hi {First name}, I track county data center/BESS/substation hearings (agendas, votes, moratoria) across VA, GA, KY, AZ, MD. Saw {Company} is active in {market}; happy to share this week's brief for your counties.

## 10-minute call script

1. "Which counties are you watching right now, and how do you find out about agenda items today?" (Listen for: a person checking websites, local counsel, news alerts, surprises.)
2. "When was the last time you learned about a hearing or rule change late? What did it cost?"
3. Show the sample on screen. "Which of these would you have wanted to know earlier?"
4. "If this covered your counties every week, would $199 a month be easy to approve, or does it need to go through someone?"
5. Close: "Send me your counties; I'll run the first brief free. If it's useful, here's the link to start." Send the $199 link (https://buy.stripe.com/aFa9AVbsZ9f22m893w9sk00), or the $499 link (https://buy.stripe.com/7sY28tcx30Iwf8U6Vo9sk01) if they need more than 10 counties.

## tracking.csv columns

`date_sent, company, segment, person, title, channel, county_hook, replied (y/n), reply_summary, call_booked (y/n), paid (y/n), plan, notes`

---

# Operator guide (for the agent running outreach)

You are running the 72-hour outreach test for Siting Watch on the founder's behalf. Read this whole section before sending anything.

## Files

| File | What it is |
|---|---|
| `outreach/emails/0-send-order.md` | Which emails go out in which batch, and what to check before each |
| `outreach/emails/1-data-center-developers.md` | 25 emails |
| `outreach/emails/2-solar-storage-developers.md` | 16 emails |
| `outreach/emails/3-brokers-consultants-law-firms.md` | 14 emails |
| `sample/siting-watch-sample-2026-10-16.pdf` | Attach to every first email |
| `outreach/tracking.csv` | Log every send and reply here |
| `outreach/prospects.csv` | Background on each company |

Each email entry has: To (person or role + LinkedIn hint), Subject, Body, Day-2 follow-up, LinkedIn note, Sources, and sometimes "Check before sending".

## Before the first send (ask the founder once)

1. The founder's sender name, title and mailing address, to replace `[Your name]` and `[Your mailing address]` in every email.
2. Which inbox and LinkedIn account to use.
3. Approval of the first 3 emails exactly as they will go out. After that, send the rest of batch 1 without asking again unless something below says to stop.

## Steps for each email

1. **Find the person.** If To names someone, confirm on the company's site or LinkedIn that they still hold that role. If To gives a role, find one real person in that role. Never guess or construct an email address. If no verified email exists, use LinkedIn instead (connection note first, then the email body as a message once accepted).
2. **Fill placeholders.** Replace `{First name}`, `[Your name]`, `[Your mailing address]`. Search the final text for `{` and `[` before sending; none may remain.
3. **Check the hook is still true.** Open the source link. If the item has moved on (vote happened, date passed), update the sentence to the current fact or switch to another verified item from the sample. Loudoun's Oct 20 vote, Frederick's Oct 21/28 hearings, Harmony Township's Oct 22 vote and DeKalb's Nov 10 committee are date-sensitive: after those dates, state the outcome, not the plan.
4. **Send** with the PDF attached, from the founder's own account, one at a time (no bulk tool, no tracking pixels).
5. **Log** a row in `tracking.csv` immediately.

## Pace

- Batch 1 (15 emails) on day 1, batch 2 (20) on day 2, batch 3 (20) on day 3 only if batches 1–2 got at least one reply.
- Day-2 follow-up goes to people who haven't replied, 2 days after the first email. Day-3 "last note" (in plan.md) after 3 days. Never more than 3 touches per person.
- No more than 25 new emails per day from one inbox.

## Replies

| Reply | What to do |
|---|---|
| "Not interested" / "no" / unsubscribe | Thank them in one line, mark `replied=y`, never contact again |
| Question about the service or price | Answer from this plan (offer, pricing, what's covered). If unsure, draft and ask the founder |
| "Send me a brief for my counties" | Collect their county list, log it, and hand it to the founder right away (the founder runs the brief with Claude; non-sample counties take 1–2 hours each) |
| Wants a call | Offer 2–3 times; once agreed, put it on the founder's calendar and log `call_booked=y`. The founder takes the call (script in plan.md) |
| Ready to pay | Send the $199 link (or $499 if they need >10 counties). Log `paid=y` only when Stripe shows the payment |
| Hostile, legal or press | Don't reply; forward to the founder |

## Never

- Claim things not in the sample or plan (no made-up customers, accuracy rates, coverage or legal claims). The service is not legal advice.
- Change prices, offer discounts, or promise delivery dates the plan doesn't state, without the founder.
- Email anyone who opted out, or anyone at a company that has asked not to be contacted.
- Post in Reddit, forums or group chats.
- Send an email without the footer above, with a misleading subject or From name, or to an address you guessed rather than found published.
- Text anyone, or make a cold sales call (Texas telemarketing registration, Bus. & Com. Code ch. 302, has no general business-to-business exemption and the question is open).

## Report to the founder

- End of each day: sends, replies, calls booked, payments, any county requests (one short message).
- Hour 72: the totals plus which row of the decision table above applies (continue / change angle / stop), and the 3 most telling reply quotes.
