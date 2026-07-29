# Eval Log — Daily Morning Briefing

Manual evaluation practice for the Milestone 0 Routine (see `CLAUDE.md`). No automated eval harness exists yet — this log is the evidence base for whether/when to build one.

**Note:** routine push notifications are currently unreliable (see "Known limitations" in `CLAUDE.md`) — don't wait for a phone push. Check manually each morning via the Code tab in the mobile app or `claude.ai/code/routines`.

Right after reading each morning's briefing, add a row. Keep entries short — a phrase, not a paragraph.

- **Miss** — something that actually mattered today but wasn't mentioned
- **Wrong** — something inaccurate, hallucinated, or irrelevant that was mentioned
- Leave a cell blank ("—") if there's nothing to note for that column

| Date | Miss | Wrong | Notes |
|------|------|-------|-------|
| 2026-07-28 | — | AI News section | Links were weekly/monthly roundup listicles ("AI Weekly Pulse", "Seven Days Seven Releases", "AI Mega-Update"), not specific single articles — despite the prompt saying to avoid listicles. Tightened step 3 wording same day. |
| 2026-07-29 | Avvoka and Likha-IT/c-fo.com rejections | — | Application-status routine (not the morning briefing) reported both as "awaiting outcome" after their final interviews; user corrected live that both had already rejected him, through a channel Gmail/Calendar never saw (call, portal, or verbal). Root cause: the routine only had Gmail + Calendar as sources, so any status change happening outside those two channels was invisible and got silently stale. Fix same day: created a "Job Applications Tracker" Notion database as a persisted source of truth, and rewrote `prompts/application-status.md` to reconcile against it each run instead of re-deriving everything from Gmail/Calendar from scratch. |
| 2026-07-29 | 46 of 68 total applications since 2026-06-25 (Jun 25–Jul 27) | — | Original application-status scan only looked back ~3-5 days, so it only ever saw the tail end of a 5-week job search — 46 applications going back to 7/6 were invisible until a user-requested full-history deep scan (5 parallel subagents, one per week, over Gmail). Included 5 more rejections it didn't know about (Teoh Capital, Bauer, JustMarkets, plus the Avvoka/Likha-IT ones above) and 2 more live action items with real deadlines (IBM HackerRank test expiring ~8/3, St Trinity video interview). Root cause: no persisted state, so anything older than the lookback window was permanently lost each run — same underlying issue as the row above, now fully backfilled into the Notion tracker. Going forward the reconcile-against-Notion approach (see prior row) should prevent this specific gap from recurring, since the tracker no longer depends on a rolling email lookback to remember old applications. |

## How to read this later

After ~2 weeks, look for patterns, not one-off complaints:

- Recurring misses of the same *kind* (e.g. always missing follow-up emails) → evidence for a specific fix, not necessarily a whole new backend
- "It forgot something from a few days ago" → evidence for durable memory across runs
- "It mixed up two unrelated things" → evidence for workspace/company isolation
- "I can't tell why it said that" → evidence for provenance tracking

If nothing recurring shows up after a couple weeks, that itself is a useful result: the simple version is working, and building the custom engine isn't justified yet.
