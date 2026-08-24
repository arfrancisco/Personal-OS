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
  `client-beamtree-` (looks like a truncated channel name, confirm the full
  one when convenient).
- Track time and work in **one.adaca.com** (time entry page: https://one.adaca.com/time).
- **Leaves/emergencies**: inform Adaca first, then file leave on **Adaca One**
  and on the **Monday.com** form.
- Send an **invoice** on the last workday of each month.

### SOD (start-of-day) email template

To: [Direct Manager] · CC: Den

```
Today's Task:

Priority

* Status (In progress) Task 1
* Status (Not yet started) Task 2

Blockers: None (or note the issue)
Questions:
```

### EOD (end-of-day) email template

To: [Direct Manager]

```
Hi [Direct Manager]
Here's my end of day report.

Completed Today:

* Task 1
* Task 2

Next Focus:

* Task 1
* Task 2
```

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
