# Personal OS — Project Context

Read this first. Any Claude Code session touching this repo — local, a scheduled Routine, or an ad-hoc Cowork session from mobile — should start here instead of from zero.

## What this is

A personal AI "second brain" / operating system: durable, source-backed memory (calendar, email, projects, tasks, decisions) plus AI that can answer "what needs my attention" without relying on chat history as memory.

It is also, deliberately, a vehicle for learning current, hireable AI-orchestration patterns (context engineering, MCP, provider-neutral design, evals, provenance) — favor legible, explainable decisions over cleverness. Treat docs/decisions here as seriously as code.

## Current phase: Milestone 0 — no custom backend

We are deliberately NOT running a custom Rails/Postgres engine yet. Instead:

- A scheduled **Claude Routine** ("Daily Morning Briefing") checks Google Calendar + Gmail each morning and searches the web for AI news, using native MCP connectors — no custom code.
- **Claude Cowork** (mobile/web/desktop) can be pointed at this repo any time for ad-hoc questions.
- A `Gemfile`/`app/` Rails skeleton already exists in this repo from an earlier exploration, but is **paused**. Do not resume building it without a concrete, evidenced reason (see below).

## Why this phase exists

Building the full custom engine (Postgres schema, context builder, MCP server, provider-neutral LLM clients, eval harness) speculatively — before knowing what a daily briefing actually needs — risks building the wrong thing. Milestone 0 uses only off-the-shelf Anthropic tooling to validate real usefulness first. See `docs/eval-log.md` for the ongoing manual evaluation practice that produces that evidence.

**Only resume the custom backend when the eval log shows a concrete, recurring gap** — e.g. "it keeps forgetting something from days ago" (durable memory), "it mixed up two unrelated things" (workspace isolation), "I can't tell why it said that" (provenance). Don't build ahead of that evidence.

## Architecture principles already agreed (for whenever the real build resumes)

- **Two decoupled loops**: ingestion (proactive, scheduled, keeps source data fresh, no user involved) vs. interactive (pull-based, on-demand, triggered by a user asking something). A Routine or Cowork session should never need to live-fetch from Gmail itself — that's the ingestion loop's job.
- **System of record, if/when built**: Postgres is canonical (events, tasks, projects, decisions, facts, provenance). Notion is a human-readable mirror, never the source of truth. Every derived fact/event/decision traces back to a `SourceRecord` with `source_type`, `source_id`, `retrieved_at`.
- **Frontend**: Claude's own apps (mobile/desktop/web), not a bespoke web UI — via a future custom MCP connector exposing tools like `get_daily_context`, backed by the Postgres data. This is why "no custom backend yet" doesn't mean "no frontend yet" — Claude Routines/Cowork already are the frontend.
- **Multi-agent is not the default.** A second agent (e.g. a future "Knowledge Curator" routine) is only justified by a genuinely different trigger, tool-set, or write-target — not because "multiple agents" sounds more sophisticated. See the reasoning in this project's design conversation for the CrewAI/multi-agent tradeoff discussion; the short version: single agent + tools solves almost everything here.
- **Company/workspace isolation** is a real future requirement (this user works across multiple companies) but is not yet designed in detail — do not assume single-tenant when the real backend gets built.
- **Human approval before risky actions.** Retrieval before writes; no autonomous production-affecting actions without explicit sign-off.

## Working conventions

- No em-dashes/hyphen-dashes in prose written for career-facing docs elsewhere in this user's environment — not strictly required here, but keep writing plain and direct.
- Prefer concise, scannable docs over long narrative ones. This file itself should stay short enough to actually get read by a cold session.
