# Eval Log — Daily Morning Briefing

Manual evaluation practice for the Milestone 0 Routine (see `CLAUDE.md`). No automated eval harness exists yet — this log is the evidence base for whether/when to build one.

Right after reading each morning's briefing, add a row. Keep entries short — a phrase, not a paragraph.

- **Miss** — something that actually mattered today but wasn't mentioned
- **Wrong** — something inaccurate, hallucinated, or irrelevant that was mentioned
- Leave a cell blank ("—") if there's nothing to note for that column

| Date | Miss | Wrong | Notes |
|------|------|-------|-------|
|      |      |       |       |

## How to read this later

After ~2 weeks, look for patterns, not one-off complaints:

- Recurring misses of the same *kind* (e.g. always missing follow-up emails) → evidence for a specific fix, not necessarily a whole new backend
- "It forgot something from a few days ago" → evidence for durable memory across runs
- "It mixed up two unrelated things" → evidence for workspace/company isolation
- "I can't tell why it said that" → evidence for provenance tracking

If nothing recurring shows up after a couple weeks, that itself is a useful result: the simple version is working, and building the custom engine isn't justified yet.
