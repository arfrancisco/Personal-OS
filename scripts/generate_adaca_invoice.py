#!/usr/bin/env python3
"""Fill Adaca's contractor invoice template for a given month.

Personal details (name, address, bank) live in a config file OUTSIDE this
repo, because this repo is public. Default location:

    ~/.config/adaca/invoice.json

Usage:
    python3 scripts/generate_adaca_invoice.py --month 2026-09
    python3 scripts/generate_adaca_invoice.py --month 2026-09 --hours 152 \
        --notes "3 days unpaid leave, pre-approved 12 Sep."

Dates follow the settled practice in prompts/adaca-work-log.md: the invoice
is dated the last working day of the month being invoiced, the service
period is that full calendar month, and the Due Date field carries the 15th
of the following month, which is what the template expects. Finance's own
payroll notice is the authority on when payment actually lands.

Formulas are left untouched. Only the yellow contractor-filled cells and the
Inv # This Year cell are written.
"""

import argparse
import calendar
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import openpyxl

DEFAULT_CONFIG = Path.home() / ".config" / "adaca" / "invoice.json"
SHEET = "Invoice Template"

# Cell map, verified against "Invoice Template - AU Contractors.xlsx".
CELLS = {
    "invoice_no": "E3",
    "invoice_date": "E5",
    "service_period": "E6",
    "due_date": "E7",
    "inv_this_year": "E8",
    "full_name": "C6",
    "position": "C7",
    "home_address": "C8",
    "personal_email": "C9",
    "phone_number": "C10",
    "bank_name": "C13",
    "branch": "C14",
    "swift_bic": "C15",
    "account_number": "C16",
    "account_holder": "C17",
    "client": "E15",
    "project_sow": "E16",
    "monthly_rate": "E17",
    "description": "B21",
    "qty_hours": "C21",
    "adjustments": "E25",
    "notes": "B35",
}

# Written by formulas in the template. Never touch these.
DO_NOT_TOUCH = ("D21", "E21", "D22", "E22", "E24", "E26")


def last_working_day(year: int, month: int) -> dt.date:
    """Last Mon-Fri of the month. Does not account for public holidays."""
    day = calendar.monthrange(year, month)[1]
    d = dt.date(year, month, day)
    while d.weekday() > 4:
        d -= dt.timedelta(days=1)
    return d


def fmt(d: dt.date) -> str:
    """31 Aug 2026 — matches the template's own date style."""
    return f"{d.day} {d.strftime('%b')} {d.year}"


def build(cfg: dict, args) -> Path:
    year, month = (int(x) for x in args.month.split("-"))
    first = dt.date(year, month, 1)
    last = dt.date(year, month, calendar.monthrange(year, month)[1])

    invoice_date = (
        dt.date.fromisoformat(args.invoice_date)
        if args.invoice_date
        else last_working_day(year, month)
    )
    due = dt.date(year + (month == 12), (month % 12) + 1, 15)

    seq = args.seq if args.seq is not None else cfg["next_sequence"]
    eng, con, bank = cfg["engagement"], cfg["contractor"], cfg["bank"]
    hours = args.hours if args.hours is not None else eng["standard_hours"]

    period_start = dt.date.fromisoformat(args.period_start) if args.period_start else first
    period_end = dt.date.fromisoformat(args.period_end) if args.period_end else last

    values = {
        "invoice_no": f"{eng['invoice_prefix']}-{seq:03d}",
        "invoice_date": fmt(invoice_date),
        "service_period": f"{fmt(period_start)} – {fmt(period_end)}",
        "due_date": fmt(due),
        "inv_this_year": seq,
        "client": eng["client"],
        "project_sow": eng["project_sow"] or None,
        "monthly_rate": eng["monthly_rate"],
        "description": f"{con['position']}: {con['full_name']}",
        "qty_hours": hours,
        "adjustments": args.adjustments,
        "notes": args.notes or None,
        **{k: con[k] for k in
           ("full_name", "position", "home_address", "personal_email", "phone_number")},
        **{k: bank[k] for k in
           ("bank_name", "branch", "swift_bic", "account_number", "account_holder")},
    }

    template = Path(cfg["template_path"])
    if not template.exists():
        sys.exit(f"Template not found: {template}")

    out = Path(cfg["output_dir"]) / (
        f"{values['invoice_no']} - {con['full_name'].split()[0]} "
        f"{con['full_name'].split()[-1]} - {invoice_date.strftime('%b %Y')}.xlsx"
    )
    shutil.copy(template, out)

    wb = openpyxl.load_workbook(out)
    ws = wb[SHEET]
    for key, cell in CELLS.items():
        ws[cell] = values[key]
    wb.save(out)

    rate = eng["monthly_rate"] / eng["standard_hours"]
    print(f"Written: {out}\n")
    print(f"  Invoice no.      {values['invoice_no']}")
    print(f"  Invoice date     {values['invoice_date']}")
    print(f"  Service period   {values['service_period']}")
    print(f"  Due date         {values['due_date']}")
    print(f"  Hours            {hours}")
    print(f"  Rate per hour    {rate:,.2f}")
    print(f"  Expected total   PHP {hours * rate + args.adjustments:,.2f}")
    if hours != eng["standard_hours"] and not args.notes:
        print("\n  WARNING: hours differ from standard and no --notes given.")
        print("  Adaca requires a written explanation for a non-standard quantity.")
    print("\n  Open in Excel, confirm the totals, export to PDF, and send to")
    print("  accounts@adaca.com. Then bump next_sequence in the config.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--month", required=True, help="Month being invoiced, YYYY-MM")
    p.add_argument("--hours", type=float, help="Actual hours logged (default: standard)")
    p.add_argument("--adjustments", type=float, default=0,
                   help="Deductions or additions; 0 if none (default: 0)")
    p.add_argument("--notes", help="Required when hours differ from standard")
    p.add_argument("--seq", type=int, help="Invoice sequence number (default: from config)")
    p.add_argument("--invoice-date", help="Override, YYYY-MM-DD")
    p.add_argument("--period-start", help="Override, YYYY-MM-DD (for partial months)")
    p.add_argument("--period-end", help="Override, YYYY-MM-DD")
    p.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = p.parse_args()

    if not args.config.exists():
        sys.exit(f"Config not found: {args.config}")
    build(json.loads(args.config.read_text()), args)


if __name__ == "__main__":
    main()
