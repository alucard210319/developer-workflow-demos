#!/usr/bin/env python3
import argparse
from pathlib import Path


RULES = [
    {
        "category": "dependency-install",
        "patterns": ["npm ERR!", "ERESOLVE", "Could not resolve dependency", "No matching distribution found"],
        "steps": [
            "Check package manager lockfile and dependency version ranges.",
            "Re-run install locally with the same runtime version used in CI.",
            "Prefer a minimal dependency change over deleting the lockfile.",
        ],
    },
    {
        "category": "missing-command",
        "patterns": ["command not found", "No such file or directory", "not recognized as an internal"],
        "steps": [
            "Confirm the command is installed in the CI job before it is used.",
            "Check PATH differences between local shell and CI.",
            "Pin tool versions in the workflow when possible.",
        ],
    },
    {
        "category": "test-failure",
        "patterns": ["FAILED", "AssertionError", "expected", "received", "Tests failed"],
        "steps": [
            "Find the first failing test, not the final summary.",
            "Run that test locally in isolation.",
            "Check whether the failure depends on time, network, locale, or filesystem paths.",
        ],
    },
    {
        "category": "permission",
        "patterns": ["Permission denied", "EACCES", "403", "Resource not accessible by integration"],
        "steps": [
            "Check repository token permissions and workflow permissions.",
            "Confirm secrets are available for the event type.",
            "Avoid exposing secrets in pull_request workflows from forks.",
        ],
    },
    {
        "category": "process-abort",
        "patterns": ["Fatal Python error", "exit code 134", "Aborted", "core dumped", "SIGABRT"],
        "steps": [
            "Check whether tests passed before the process aborted.",
            "Compare against the default branch to detect unrelated CI instability.",
            "Collect runtime, OS, and dependency versions from the failing job.",
        ],
    },
]


def score_rule(text, rule):
    matches = []
    lower_text = text.lower()
    for pattern in rule["patterns"]:
        if pattern.lower() in lower_text:
            matches.append(pattern)
    return matches


def confidence(match_count):
    if match_count >= 3:
        return "high"
    if match_count == 2:
        return "medium"
    return "low"


def analyze(text):
    candidates = []
    for rule in RULES:
        matches = score_rule(text, rule)
        if matches:
            candidates.append((len(matches), rule, matches))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0]


def main():
    parser = argparse.ArgumentParser(description="Analyze a CI log and summarize likely failure causes.")
    parser.add_argument("logfile", help="Path to the CI log file")
    args = parser.parse_args()

    path = Path(args.logfile)
    text = path.read_text(encoding="utf-8", errors="replace")
    result = analyze(text)

    print("CI Log Report")
    print("-------------")

    if not result:
        print("Likely category: unknown")
        print("Confidence: low")
        print()
        print("Suggested next steps:")
        print("- Search for the first error before the final failure summary.")
        print("- Compare the failing run with a passing run if available.")
        print("- Capture runtime versions, environment variables, and changed files.")
        return

    match_count, rule, matches = result
    print(f"Likely category: {rule['category']}")
    print(f"Confidence: {confidence(match_count)}")
    print()
    print("Evidence:")
    for match in matches:
        print(f"- {match}")
    print()
    print("Suggested next steps:")
    for step in rule["steps"]:
        print(f"- {step}")


if __name__ == "__main__":
    main()

