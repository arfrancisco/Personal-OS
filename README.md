# Personal OS

A personal AI "second brain" — durable, source-backed memory across calendar, email, projects, tasks, and decisions — built partly as a vehicle for learning current AI-orchestration patterns (context engineering, MCP, evals, provenance).

**Current phase: Milestone 0.** No custom backend yet. Four Claude Routines run against this repo instead:

- **Daily Morning Briefing** — calendar/email triage each morning, plus a quick AI-news digest
- **Bill payment reminder** — checks for upcoming bills, creates calendar reminders
- **Application status check** — tracks pending job applications and interviews
- **LinkedIn post drafts** — twice-weekly AI + Rails post ideas drafted to Notion for manual review/posting

See:
- [`CLAUDE.md`](./CLAUDE.md) — full project context, architecture principles, and known limitations. Read this first.
- [`prompts/`](./prompts) — the actual instructions each routine runs, versioned as plain files rather than buried in routine config
- [`docs/eval-log.md`](./docs/eval-log.md) — the manual evaluation practice tracking whether this is actually useful, and what (if anything) justifies building a real backend later

A Rails skeleton exists under `app/`/`config`/etc. from early exploration but is currently paused — see `CLAUDE.md` for why.
