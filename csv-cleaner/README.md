# CSV Cleaner

Clean a CSV file with Python standard library only.

Features:

- Trim whitespace in every cell.
- Normalize header names.
- Validate email-like columns.
- Remove duplicate rows by a selected key.
- Write clean and rejected rows.

## Usage

```bash
python3 clean_csv.py sample-input.csv --dedupe-key email --out clean.csv --rejects rejects.csv
```

## Files

- `clean_csv.py` - Script.
- `sample-input.csv` - Example input.

