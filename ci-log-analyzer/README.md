# CI Log Analyzer

Analyze a GitHub Actions or CI log and print a concise failure report.

## Usage

```bash
python3 analyze_ci_log.py sample-failure.log
```

## Example Output

```text
CI Log Report
-------------
Likely category: dependency-install
Confidence: medium

Evidence:
- npm ERR! code ERESOLVE
- Could not resolve dependency

Suggested next steps:
- Check package manager lockfile and dependency version ranges.
- Re-run install locally with the same Node.js version used in CI.
- Prefer a minimal dependency change over deleting the lockfile.
```

