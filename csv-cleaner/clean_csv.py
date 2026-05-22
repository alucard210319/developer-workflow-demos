#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_header(value):
    return value.strip().lower().replace(" ", "_")


def clean_cell(value):
    return value.strip()


def clean_row(row):
    return {key: clean_cell(value) for key, value in row.items()}


def is_valid_email(value):
    return bool(EMAIL_RE.match(value))


def main():
    parser = argparse.ArgumentParser(description="Clean CSV rows and split invalid rows.")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("--dedupe-key", default="email", help="Column used for duplicate detection")
    parser.add_argument("--out", default="clean.csv", help="Clean output CSV")
    parser.add_argument("--rejects", default="rejects.csv", help="Rejected output CSV")
    args = parser.parse_args()

    input_path = Path(args.input)
    out_path = Path(args.out)
    rejects_path = Path(args.rejects)

    with input_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise SystemExit("Input CSV has no header row.")

        fieldnames = [normalize_header(name) for name in reader.fieldnames]
        seen = set()
        clean_rows = []
        rejected_rows = []

        for raw_row in reader:
            normalized_raw = {
                normalize_header(key): value
                for key, value in raw_row.items()
                if key is not None
            }
            row = clean_row(normalized_raw)
            reject_reason = ""

            key_value = row.get(args.dedupe_key, "")
            if not key_value:
                reject_reason = f"missing {args.dedupe_key}"
            elif args.dedupe_key == "email" and not is_valid_email(key_value):
                reject_reason = "invalid email"
            elif key_value.lower() in seen:
                reject_reason = "duplicate"

            if reject_reason:
                rejected = dict(row)
                rejected["reject_reason"] = reject_reason
                rejected_rows.append(rejected)
                continue

            seen.add(key_value.lower())
            clean_rows.append(row)

    with out_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean_rows)

    reject_fields = fieldnames + ["reject_reason"]
    with rejects_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=reject_fields)
        writer.writeheader()
        writer.writerows(rejected_rows)

    print(f"Wrote {len(clean_rows)} clean rows to {out_path}")
    print(f"Wrote {len(rejected_rows)} rejected rows to {rejects_path}")


if __name__ == "__main__":
    main()

