# Memory Architecture

Status: design reference only — no dedicated memory service is being built yet (Milestone 0 gate applies, see `CLAUDE.md`). This doc exists so that when the custom backend is eventually built, memory doesn't get redesigned from scratch — it gets migrated.

## Reference model (industry-standard shape, roughly the CoALA framing)

1. **Tiered, not monolithic** — working memory is the live context window; long-term memory is external and split by kind: episodic (what happened), semantic (durable facts), procedural (learned rules/preferences).
2. **Agent-driven read/write** — the agent decides what's worth persisting and when to pull it back in, rather than every fact auto-flowing into context every turn.
3. **Provenance-linked** — memory entries point back to a source of truth; they aren't the source of truth themselves.
4. **Consolidation** — periodic summarization/pruning so memory doesn't grow unbounded or go stale silently.

## Two things currently called "memory" — keep them distinct

Milestone 0 already has two separate persisted stores, serving different roles and heading toward different parts of the future system of record. Don't conflate them:

1. **Claude Code's session memory** (`~/.claude/projects/-home-armfrancisco-personal-os/memory/`) — the *agent's* operational memory about this project: preferences, past decisions, corrections. Scoped to me (the coding agent working on personal-os), not domain data the routines read or write.
2. **Notion** — the *domain* data the routines persist across runs: job application status, bill due dates, the Learning Tracker. This is subject matter, not agent bookkeeping.

### Claude Code session memory

Implements a lightweight version of the reference model above:

- Four types — `user`, `feedback`, `project`, `reference` — split roughly along semantic/procedural/episodic lines.
- `MEMORY.md` is the retrieval index (agent reads it every session, opens individual files by relevance judgment — no embedding search needed at this scale).
- Each entry carries provenance (`originSessionId`, `modified` timestamp) and cross-links related entries (`[[name]]`).
- Retrieval and write decisions are already agentic, not a blind dump.

### Notion

Right now Notion is the de facto system of record for routine-persisted domain data, not a "mirror" of anything — `CLAUDE.md`'s "Notion is a mirror, never source of truth" is a future-state principle for once Postgres is canonical. Until then there's nothing else for it to mirror, so it's the real store.

This is deliberate, not a temporary hack to feel bad about: letting each routine create/shape its own Notion structure as it needs it (per [[feedback-notion-schema-in-prompts]] — don't hardcode schema into prompts) means the schema that emerges is *evidence* of what a future Postgres schema actually needs to support, rather than a guess made before any routine had run once.

## Mapping to the future system of record

| Current store | Current role | Future Postgres entity (per `CLAUDE.md`'s "system of record") |
|---|---|---|
| Claude Code memory: `project` | agent's record of decisions/state about this repo | `projects` / `decisions`, tied to a `SourceRecord` |
| Claude Code memory: `feedback` | agent's record of corrected behavior | no direct analogue yet — a procedural-preferences table, kept distinct from facts |
| Claude Code memory: `user` | agent's record of who the user is | low-churn `facts` about the user |
| Claude Code memory: `reference` | pointers to external systems | pointers only; shouldn't need to survive migration |
| Notion (Learning Tracker, job application tracker, bill tracker, etc.) | Milestone-0 system of record for routine-persisted domain data | `events` / `tasks` / `projects` / `decisions`, per whatever structure each Notion database ends up needing |

## Day-to-day practice (works now, doesn't block migration)

- Keep writing memory using the four-type taxonomy as-is — it's already aligned with where this is headed.
- Every few weeks, or when `MEMORY.md` starts approaching its 200-line display cap, do a consolidation pass: merge overlapping entries, delete stale ones, split any file that's accumulated multiple unrelated facts.
- Treat a contradiction between a memory entry and live repo/API state as a signal to fix the memory immediately, not just note the discrepancy in conversation.
- Let each routine keep shaping its own Notion structure as needed rather than prescribing it upfront — that's the point, not a gap to fix.

## Migration trigger

Same eval-log-driven gate as the rest of Milestone 0 (see `docs/eval-log.md`) — don't build a vector store, dedicated memory service, or Postgres schema speculatively. Signals specifically worth watching for:

- `MEMORY.md` hitting its line cap despite regular consolidation (the index itself is out of room).
- A memory file going stale faster than it's caught (repeatedly contradicts live state).
- Needing cross-workspace/company isolation for memory — already flagged as a known future requirement in `CLAUDE.md`, not yet designed.
- Notion straining under its own role: routines needing to join/query across databases in ways Notion handles poorly, or duplicate/contradictory pages appearing because there's no real schema enforcement. That strain is itself the evidence for what the Postgres schema needs to formalize — not a reason to patch Notion harder.

If/when triggered, the mapping table above is the starting schema sketch, not a new architecture decision.
