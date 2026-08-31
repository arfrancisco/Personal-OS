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
- **Work out the daily hours at the start of each month.** The target is 160
  hours per month, not 8 hours per day, and the number of working days
  varies. Divide 160 by that month's weekdays and log that figure daily so
  the month lands exactly on target. Watch the h:mm conversion, since the
  decimal and the minutes are different numbers: September 2026 has 22
  weekdays, so 160/22 is 7.2727 hours, which is **7h 16m**, not 7h 22m.
  Logging 7h 22m would overshoot by about two hours across the month.
- **Submit logged hours weekly** in Adaca One. Logging time is not enough on
  its own — there is a submit button at the bottom of the time page, and the
  week's hours have to be submitted for approval. Do it at the end of each
  week. Finance treats submitted timesheets as a precondition for the monthly
  payroll run, so unsubmitted hours can hold up payment even when the invoice
  went in on time.
- **Leaves/emergencies**: inform Adaca first, then file leave on **Adaca One**
  and on the **Monday.com** form.
- Send an **invoice** on the last working day of each month, covering that
  same month. Miss it and payment defers a full cycle. See "Invoicing" below.

**One email thread per work day.** Start the thread with the SOD in the
morning, then send the EOD as a reply on that same thread. Keeps the day's
plan and its outcome side by side for the manager, and makes it easy to see
what actually landed against what was planned.

Subject: `Daily Report: DD Month YYYY (Alain Francisco)`. Deliberately not
"Start of Day", so the EOD reply doesn't read oddly against it.

**Always draft against the previous day's SOD and EOD.** Before writing a
new one, read back what was planned and what was reported, then check
whether the intent actually happened:

- Anything in yesterday's SOD that did not land should either appear in
  today's Priority list or be dropped deliberately, not silently.
- Anything in yesterday's EOD "Next Focus" is the natural starting point
  for today's "Today's Task".
- If something keeps carrying over across several days, say so rather than
  restating it as if it were new. A repeatedly deferred item is usually a
  blocker, a bad estimate, or something that should be dropped.

The point is that the reports reflect what actually happened rather than
drifting into a list of intentions nobody checks.

**Report substantive work, not setup and admin.** Routine environment
setup, credential rotation, tool access and similar housekeeping are part
of the day but not worth a line in the report. They go in the Notion daily
log instead. Keep the email to things the manager would actually want to
know about.

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

**Settled practice: send the invoice on the last working day of the month
being invoiced.** Not the following month.

This comes from Adaca Finance directly (August 2026 payroll notice), which
required manual invoices "on or before 31 August 2026", i.e. the last day of
the service month itself. Finance was explicit that contractors who miss the
deadline are excluded from that payroll run and do not get paid until the
next cycle.

**Trust Finance's payroll notices over the invoice template documents.** The
template pack disagrees with itself (one page says submit by the 7th of the
following month, another says the 2nd) and both are wrong about the operative
deadline. It also states payment on the 15th, while Finance scheduled the
August run for 10 September. The template is useful for filling in fields;
it is not reliable on dates.

### Cycle

| Step | When |
|---|---|
| Deliver services | 1st to last day of the month |
| Submit invoice | On or before the last working day of that same month |
| Payment released | Per Finance's notice for that run (10 September for the August 2026 period) |
| Missed the deadline | Deferred to the next cycle, roughly five weeks later |

### Generating it

`scripts/generate_adaca_invoice.py` fills Adaca's template from a config
file. Personal and bank details live in `~/.config/adaca/invoice.json`,
outside this repo, because this repo is public.

```
python3 scripts/generate_adaca_invoice.py --month 2026-09 --hours 160
```

Add `--notes` whenever hours differ from 160, since Adaca requires a written
explanation for a non-standard quantity (the script warns if you forget).
Use `--period-start` and `--period-end` for a partial month. Bump
`next_sequence` in the config after each send.

It writes the yellow contractor cells and leaves every formula alone. It
also writes a literal value into the "Inv # This Year" cell, which is a
deliberate fix: the template's own `=COUNTA(Invoice_Log!B:B)-1` counts the
Invoice_Log summary labels as if they were invoices, so it reports a wrong
number.

Open the result in Excel, confirm the totals, then export to PDF. Two things
Excel gets wrong if a value is typed rather than written by the script:
phone numbers become scientific notation unless the cell is text, and dates
can reformat.

### Practical routine

Send at the end of the last working day of the month, so the hours are
actual rather than estimated. To avoid starting from scratch on a day that
is usually busy, **pre-fill everything except the final hours count a day or
two ahead**: name, bank details, invoice number, service period, client,
rate and any partial-month explanation. Then the last day is just adding the
final hours and exporting to PDF.

Don't leave it late in the evening. Adaca Finance is in Sydney, two hours
ahead of Manila, so a Manila late-night send can carry a timestamp that
tips into the following month against an "on or before" deadline. Aim for
Manila early evening at the latest.

Don't rely on a scheduled reminder for this. Routine push notifications are
unreliable on this account (see `CLAUDE.md`). The dependable mechanism is
the daily SOD, which gets written anyway, so put the invoice on it.

### Also required each period

- Submit timesheets for approval.
- Log any overtime in Adaca One, pre-approved. Overtime not pre-approved does
  not get paid.
- Log any unpaid leave taken in the period, for record-keeping.

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
- Then upload the PDF to the invoices folder in Google Drive:
  https://drive.google.com/drive/u/0/folders/1s3nvs_c7nrs0T5gvEGhewcqec35ZtD2S
  Manual drag and drop. PDF only, since the xlsx can be regenerated from the
  script at any time.
- Update the invoice tracker in Notion, and bump `next_sequence` in
  `~/.config/adaca/invoice.json`.

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
