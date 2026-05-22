#!/usr/bin/env python3
import argparse
from pathlib import Path


def read_required(path):
    names = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if value and not value.startswith("#"):
            names.append(value)
    return names


def read_env(path):
    values = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def main():
    parser = argparse.ArgumentParser(description="Check required deployment environment variables.")
    parser.add_argument("required", help="File with one required variable name per line")
    parser.add_argument("envfile", help="Env file to inspect")
    args = parser.parse_args()

    required = read_required(args.required)
    env = read_env(args.envfile)
    present = [name for name in required if env.get(name)]
    missing = [name for name in required if not env.get(name)]

    print("Deployment Env Report")
    print("---------------------")
    print(f"Status: {'passed' if not missing else 'failed'}")
    print()
    print("Present:")
    for name in present:
        print(f"- {name}")
    if not present:
        print("- none")
    print()
    print("Missing:")
    for name in missing:
        print(f"- {name}")
    if not missing:
        print("- none")

    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

