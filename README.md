# Personal OS

A personal AI "second brain" — durable, source-backed memory across calendar, email, projects, tasks, and decisions — built partly as a vehicle for learning current AI-orchestration patterns (context engineering, MCP, evals, provenance).

**Current phase: Milestone 0.** No custom backend yet. Five scheduled automations run against this repo instead:

- **Daily Morning Briefing** — calendar/email triage each morning, plus a quick AI-news digest
- **Bill payment reminder** — checks for upcoming bills, creates calendar reminders
- **Application status check** — tracks pending job applications and interviews
- **Job search scan** — daily search for new job postings matching my background (Senior SWE / AI-LLM engineer roles), with fit rationale and application links
- **Learning & growth check-in** — weekly, two tracks: using Claude/Claude Code better, and building toward a Forward Deployed Engineer skillset. Progress tracked in a Notion "Learning Tracker" database

They run as scheduled Claude Routines, fetching their prompt live from GitHub each run rather than duplicating it. `prompts/*.md` in this repo is the versioned source of truth.

See:
- [`CLAUDE.md`](./CLAUDE.md) — full project context, architecture principles, and known limitations. Read this first.
- [`prompts/`](./prompts) — the actual instructions each routine runs, versioned as plain files rather than buried in routine config
- [`docs/eval-log.md`](./docs/eval-log.md) — the manual evaluation practice tracking whether this is actually useful, and what (if anything) justifies building a real backend later

A Rails skeleton exists under `app/`/`config`/etc. from early exploration but is currently paused — see `CLAUDE.md` for why.
