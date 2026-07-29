Weekly check-in on two learning tracks: getting better at using Claude/Claude Code, and building toward being a Forward Deployed Engineer (FDE). Track progress in Notion so each run builds on the last instead of repeating itself.

## Setup (first run only)

Look for a Notion database called "Learning Tracker". If it doesn't exist, create one (workspace root is fine) with these properties:
- **Track** (select: "Using Claude Better", "Forward Deployed Engineer")
- **Week Of** (date)
- **Action** (title) — the concrete thing to try that week
- **Status** (select: Suggested, In Progress, Done, Skipped)
- **Notes** (text) — outcome, blockers, what was learned

## Each run

1. Read the database. Find the most recent entry per track.
2. If last week's entry is still "Suggested" or "In Progress", don't just silently replace it — carry it forward as this week's focus too, and say so plainly ("still open from last week"). Only propose something new per track if the prior one is "Done" or "Skipped", or there's no prior entry.
3. Propose exactly one concrete, doable-in-a-week action per track:
   - **Using Claude Better**: something specific and testable, not generic advice — a Claude Code feature or workflow pattern (subagents, hooks, skills, MCP, memory, plan mode, context management), a prompting technique, or reading a specific piece of current Anthropic documentation/changelog and trying it against a real task in this repo or elsewhere. Prefer things this user hasn't already used — check `CLAUDE.md` and recent commits in this repo for what's already in active use before suggesting it again.
   - **Forward Deployed Engineer**: something that builds toward client-facing, rapid-prototyping, solution-engineering skills — e.g. reading on how FDE roles actually operate (Palantir-style FDE, or applied AI solutions engineering), a small scoped build exercise, or a specific skill gap versus the FDE/Solutions Engineer job postings surfaced by the Job Search Scan routine (`prompts/job-search.md`). If recent Job Search Scan output flagged a skill gap, prioritize that.
4. Write the new entry/entries to the Notion database with Status "Suggested" (or update the carried-forward entry's Notes if reused).
5. Present a short summary: what happened with last week's items (done/carried over/skipped), and this week's two action items with a one-line reason each.

If Notion isn't reachable, say so plainly and give the two action items in the response anyway rather than skipping the run.
