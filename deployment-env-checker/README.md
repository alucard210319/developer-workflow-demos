# Deployment Env Checker

Check whether required deployment environment variables are present before a build or deploy step.

This is useful for small apps deployed to Vercel, Render, Railway, Netlify, Docker, or GitHub Actions.

## Usage

```bash
python3 check_env.py required-env.txt sample.env
python3 check_env.py required-env.txt sample-complete.env
```

## Example Output

```text
Deployment Env Report
---------------------
Status: failed

Present:
- DATABASE_URL
- NEXT_PUBLIC_APP_URL

Missing:
- STRIPE_SECRET_KEY
- GITHUB_TOKEN
```

## Files

- `check_env.py` - Script.
- `required-env.txt` - Example required variables.
- `sample.env` - Example environment file.
- `sample-complete.env` - Example environment file that passes.
