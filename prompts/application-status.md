Review pending job applications, scheduled interviews, and outstanding action items — using the "Job Applications Tracker" Notion database as the persisted source of truth, not Gmail/Calendar alone.

1. Query the "Job Applications Tracker" Notion database. This is where state persists across runs — including outcomes that never show up in Gmail or Calendar (a rejection by phone call, a portal-only status change, something the user just tells you).
2. Search Gmail (last ~3-5 days, or since the tracker's most recent "Last Update" if longer) for application confirmations, interview invites/reminders, assessment nudges, and rejections. Search Calendar for scheduled interviews going forward from today.
3. Reconcile: for each new or changed item found in Gmail/Calendar, update the matching Notion row (Status, Last Update, Next Action, Notes) or create a new row if it's a new application. Match on Company + Role, not just Company. If a company/role in the tracker shows no new email activity, leave it as-is — don't assume it's still accurate, but don't overwrite it either.
4. Present the current state as a scannable summary, grouped by status:
   - **Action needed** — anything requiring the user to do something (schedule an interview, submit a document, complete an assessment). Flag clearly, include the next action and any deadline mentioned.
   - **Interviewing / awaiting response** — applications past initial application stage with no resolution yet.
   - **Recently applied** — applications submitted since the last run, still awaiting first response.
   - **Rejected / closed** — only if status changed since the last run; otherwise omit from the main summary (they're closed out, no need to re-report every day).
5. If the user mentions a status change in conversation (e.g. "X rejected me") that isn't reflected in Gmail/Calendar, update the Notion row directly from what they said — that's the whole point of persisting it there.

If there are no pending applications or interviews, confirm briefly. If the Notion database isn't found, say so plainly rather than reconstructing everything from Gmail each time.
