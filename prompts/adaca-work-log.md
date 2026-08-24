# Adaca / Beamtree — onboarding & daily work log

Context: independent contractor engagement with Adaca Projects Pty Ltd (Sydney,
contact Lambros Photios), working on the Beamtree client project. Ruby on Rails
full stack. Fixed 10-month term, target 160 hrs/month, monthly invoicing.
Services start Monday, 24 August 2026.

This file is the canonical source for the onboarding checklist and the daily
log habit below — versioned here per the repo's routine convention
so changes are diffable and reviewable, even though this isn't wired to a
scheduled Cowork task yet (deliberately manual for now — see "Status" below).

## Onboarding checklist

- Send a **start-of-day** email each work day.
- Send an **end-of-day** email each work day.
- Post a **time in** and **time out** message in Adaca's Slack, channel
  `client-beamtree-` (trailing dash confirmed correct — a naming quirk from
  whoever created the channel, not a typo).
- Track time and work in **one.adaca.com** (time entry page: https://one.adaca.com/time).
- **Leaves/emergencies**: inform Adaca first, then file leave on **Adaca One**
  and on the **Monday.com** form.
- Send an **invoice** on the 1st of each month, covering the month just
  finished — see "Invoicing" below for the full process.

**One email thread per work day.** Start the thread with the SOD in the
morning, then send the EOD as a reply on that same thread. Keeps the day's
plan and its outcome side by side for the manager, and makes it easy to see
what actually landed against what was planned.

Subject: `Daily Report: DD Month YYYY (Alain Francisco)`. Deliberately not
"Start of Day", so the EOD reply doesn't read oddly against it.

### SOD (start-of-day) email template

Send from the **Adaca Outlook account**, not personal Gmail. Starts the
day's thread.
To: Arpan (direct manager, Beamtree) · CC: Den (HR, Adaca).
Addresses are in the Notion page, not here — this repo is public.

```
Today's Task:

Priority

* Status (In progress) Task 1
* Status (Not yet started) Task 2

Blockers: None (or note the issue)
Questions:
```

### EOD (end-of-day) email template

Send as a **reply on that day's existing SOD thread**, from the Adaca
Outlook account.

```
Here's my end of day report:

Completed Today:

* Task 1
* Task 2

Next Focus:

* Task 1
* Task 2
```

Adaca's original template opened with "Hi [Direct Manager]" and ended the
line with a period. Dropping the greeting and using a colon reads better —
that's the preferred form above.

## Invoicing

Adaca supplies an Excel invoice template (guide effective August 2025). Fill
in the **Invoice Template** tab only — never edit the `Invoice_Log` tab.

**Settled practice: send the invoice on the 1st of the following month**,
covering the month just finished, dated the day it goes out. This clears
every deadline Adaca states — their docs variously say "no later than the
7th" and "on or before the 2nd", and the 1st beats both, so the discrepancy
never needs resolving. The service period is also genuinely complete by then
and the invoice date falls in the following month, as the template expects.

### Cycle

| Step | When |
|---|---|
| Deliver services | 1st to last day of the month |
| Submit invoice | 1st of the following month |
| Finance reviews | 7th–10th of the following month |
| Payment released | 15th of the following month |

Late or incomplete invoices get deferred to the next payment cycle.

### Before you start

- Have your signed Independent Contractor Agreement handy (confirms the rate).
- Have complete bank details: bank name, branch, Swift/BIC, account number,
  account holder name.

### Fields

Yellow cells = fill in. Blue text / orange / light blue = formulas or
system-generated, do not edit.

- **Invoice No.** — sequential per client, format `INV-[CLIENT]-[NNN]`
  (e.g. `INV-MORRISON-001`).
- **Invoice Date** — the date of submission.
- **Service Period** — always the full calendar month: 1st to last day.
- **Due Date** — auto-filled as the 15th of the following month. Do not edit.
- **Inv # This Year** — auto-pulled from the Invoice Log. Do not edit.
- **Contractor details** — full legal name and role exactly as they appear in
  the Contractor Agreement, plus home address, personal email, phone.
- **Bank details** — as above; double-check the account number every time.
  Account holder name must match your ID.
- **Client** / **Project + SOW** — the end client and project/SOW reference.
- **Monthly Rate** — pre-filled by Finance in PHP. Do not change it without
  confirming with Finance first.
- **QTY (hours)** — 160 for a standard full month. Adjust only for a partial
  month, and attach a written explanation plus notify Finance.
- **Rate per Hour** — formula (monthly rate ÷ 160). Do not edit.
- **Amount** — formula (QTY × rate per hour). Do not edit.
- **Adjustments** — agreed deductions or additions (e.g. leave without pay,
  reimbursements). Enter `0` if none; never leave blank.
- **Total Due** — formula (subtotal + adjustments). Do not edit.
- **Notes** — optional context for any deduction, adjustment, or unusual item
  (e.g. "3 days LWOP, pre-approved by manager on 15 Jun").

### Submitting

- Save as **PDF**, not Excel.
- Email to **accounts@adaca.com** (also the address for payment queries).
- Subject line: `Invoice – [Name] – [Service Period] – [Client/Project]`
  (e.g. `Invoice – Maria Santos – July 2026 – Client ABC`).

## Access & IT

Access requests go through **TechD** (external IT support service Adaca/
Beamtree use for provisioning) — not Adaca or Beamtree staff directly.

Current grant/pending status for specific tools (Teams, Jira, git repo, etc.)
is tracked in the Notion Daily Log, not here — see "Daily log habit" below
for why.

## Daily log habit

Starting 24 August 2026, keep a daily log of everything worked on for Adaca/
Beamtree. Two tiers, matching how this repo splits things:

- **This file (rarely changes)**: onboarding process, checklist, standing
  rules Adaca/Beamtree communicate, and email/message templates. Edit this
  file directly (or ask Claude Code to) when the process itself changes.
  Litmus test: would this line still be true a month from now unedited? If
  yes, it belongs here. If it's a status that will flip (access granted/
  pending, a blocker that gets resolved), it belongs in Notion instead —
  don't let this file accumulate a running status list that gets rewritten
  every time something changes; that's what the Daily Log is for.
- **Notion (day-to-day, changes constantly)**: the actual daily entries —
  what got worked on, decisions, blockers, current access/status snapshots,
  anything worth remembering later. Lives at **Adaca — Beamtree → Daily Log**
  in Notion: https://app.notion.com/p/3c252229fba0818bb04eca32e51644cd

  Entry format (one per work day, newest at the bottom, matches the existing
  Build Log convention used for other projects):
```
YYYY-MM-DD — short headline
What got worked on, decisions made, blockers, anything notable — written
so it's useful later for updating the career repo resume.
```

## Why this exists

The Notion daily log is meant to eventually feed updates into the
`arfrancisco/career` repo (the YAML/Markdown-driven resume build) — a running
record of real work makes it much easier to write accurate, specific resume
bullets later instead of trying to reconstruct months of work from memory.

## Status

No scheduled Cowork task yet — logging is manual (write the day's entry
yourself, or ask Claude/Cowork to draft one from what you tell it). If this
becomes a real daily habit worth automating, the next step is a Cowork
scheduled task that fires at end of day, reads this file for instructions,
and writes the entry to the Notion page above — following the same
fetch-prompt-live pattern as the other four routines in this repo.
