# Developer Workflow Demos

Small practical demos for developer workflow fixes, automation scripts, and browser tools.

This repository is a portfolio for focused freelance work:

- Debugging CI, build, and deployment failures.
- Writing small Python or JavaScript automation scripts.
- Building lightweight Chrome extensions for browser workflows.

## Demos

### CI Log Analyzer

Location: `ci-log-analyzer/`

A Python script that reads a CI log and summarizes the likely failure category, evidence, and next steps.

Run it:

```bash
cd ci-log-analyzer
python3 analyze_ci_log.py sample-failure.log
```

### CSV Cleaner

Location: `csv-cleaner/`

A Python script that trims cells, validates email-like fields, removes duplicate rows, and writes clean and rejected output files.

Run it:

```bash
cd csv-cleaner
python3 clean_csv.py sample-input.csv --dedupe-key email --out clean.csv --rejects rejects.csv
```

### Chrome Table Exporter

Location: `chrome-table-exporter/`

A minimal Chrome extension that exports the first HTML table on the current page as CSV.

Install it locally:

1. Open `chrome://extensions`.
2. Enable Developer mode.
3. Click "Load unpacked".
4. Select the `chrome-table-exporter` folder.

### Deployment Env Checker

Location: `deployment-env-checker/`

A Python script that checks whether required deployment environment variables are present before a build or deploy step.

Run it:

```bash
cd deployment-env-checker
python3 check_env.py required-env.txt sample.env
python3 check_env.py required-env.txt sample-complete.env
```

## Services These Demos Support

These examples map to small, scoped tasks that are easy to verify:

- Fix a failing GitHub Actions workflow.
- Diagnose an npm, Python, Docker, or deployment error.
- Create a small data cleanup script.
- Build a tiny Chrome extension for a repeated browser task.

## Work Style

For each task, I aim to provide:

- A short root-cause summary.
- A small patch or script.
- Clear verification steps.
- Notes for anything that requires the client's private environment.
