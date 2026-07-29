# Personal OS — Project Context

Read this first. Any Claude Code session touching this repo — local, a scheduled Routine, or an ad-hoc Cowork session from mobile — should start here instead of from zero.

## What this is

A personal AI "second brain" / operating system: durable, source-backed memory (calendar, email, projects, tasks, decisions) plus AI that can answer "what needs my attention" without relying on chat history as memory.

It is also, deliberately, a vehicle for learning current, hireable AI-orchestration patterns (context engineering, MCP, provider-neutral design, evals, provenance) — favor legible, explainable decisions over cleverness. Treat docs/decisions here as seriously as code.

## Current phase: Milestone 0 — no custom backend

We are deliberately NOT running a custom Rails/Postgres engine yet. Instead:

- Four scheduled automations — Daily Morning Briefing, Bill payment reminder, Application status check, Job search scan — run as **Claude Routines**, using native MCP connectors and fetching their prompt from `prompts/*.md` in this repo live on each run — no custom code.
- **Claude Cowork** (mobile/web/desktop) also handles ad-hoc questions any time, in addition to running the scheduled tasks above.
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

## Known limitations

- **Routine push notifications don't reliably deliver.** As of July 2026 this is a reported upstream bug: routine-triggered sessions log a "push requested" success but don't actually send anything (Claude Code issues #54994, #50949, #60208) — only Remote Control sessions push reliably. Confirmed on this account: all phone-side settings (app notification permissions, account match, battery optimization, in-app settings) checked out fine, and the routine itself fires correctly — it's the delivery path that's broken, not the setup. It's also inconsistent, not a hard "never works" — a push did arrive once during testing, then failed to on other identical runs. **Don't rely on the push arriving from the Daily Morning Briefing routine** — check it manually (Code tab in the mobile app, or `claude.ai/code/routines` in a browser) until this is fixed upstream. If it stays broken long-term, that's a concrete reason to eventually want an alternative delivery path (e.g. email) rather than depending on Anthropic's routine-push specifically.
- **No reliable way to navigate back to a past routine/Cowork session on mobile.** Opening a session via a push notification works, but once you back out, there's no confirmed session-history list in the mobile app to find it again — Cowork/Routines mobile support is still a gradual beta rollout (Anthropic's own docs note some plans "may have to wait until their accounts receive the feature"). **Fallback:** `claude.ai/code/routines` in a browser shows run history for each routine regardless of what the mobile app currently supports — use that to re-read a past run's output.

## Routine convention: prompts live in the repo, not in the routine config

Keep the actual instructions in a versioned file under `prompts/` (e.g. `prompts/daily-briefing.md`), not embedded in the routine's own config. Each routine's own prompt (the `events[].data.message.content` field, set via `RemoteTrigger`) should be reduced to a thin pointer: *"Read `prompts/<name>.md` in this repo and follow it exactly to produce today's output. If the file isn't found, say so plainly rather than improvising."*

This requires `Read` in the routine's `allowed_tools`, and the routine's `session_context.sources` must include this repo's `git_repository` so there's actually something to check out and read.

**Connectors attach automatically at routine creation.** Connect services once at claude.ai/customize/connectors (Gmail, Calendar, Drive, Notion, etc.) — don't pass `mcp_connections` when calling `RemoteTrigger action:"create"`. The API auto-populates it from every connector already connected on the account; confirmed by creating this project's four routines with no `mcp_connections` specified and seeing Gmail/Calendar/Notion/Drive show up in the response unrequested. The `/schedule` skill's own preloaded "no connectors" warning is unreliable (stale/differently-scoped) — trust the live `RemoteTrigger create` response instead, not that static text.

Reasoning: prompt changes then become normal git commits (diffable, reviewable, show up in `git log`) instead of opaque edits only visible by calling the routine/task API. Matches the project's general principle of versioning prompts, not just code.

## Working conventions

- No em-dashes/hyphen-dashes in prose written for career-facing docs elsewhere in this user's environment — not strictly required here, but keep writing plain and direct.
- Prefer concise, scannable docs over long narrative ones. This file itself should stay short enough to actually get read by a cold session.
