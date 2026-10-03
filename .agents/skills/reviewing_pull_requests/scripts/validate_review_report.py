#!/usr/bin/env python3
"""Validate the deterministic structure of a PR readiness review report.

This script checks the report format only. It does not assess code quality,
correctness, or the quality of the review findings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = (
    "Review Context",
    "Requirements / Acceptance Criteria Reviewed",
    "Test Evidence",
    "MUST FIX",
    "SHOULD FIX",
    "OPTIONAL",
    "Final Review Summary",
)

HUMAN_DECISION_PATTERN = re.compile(
    r"^\s*Human decision required\s*:\s*.*$",
    re.MULTILINE,
)


def validate_report(report_path: Path) -> list[str]:
    """Return a list of deterministic format errors."""
    if not report_path.is_file():
        return [f"File does not exist: {report_path}"]

    try:
        content = report_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"Unable to read file '{report_path}': {exc}"]

    errors = []

    for heading in REQUIRED_HEADINGS:
        pattern = re.compile(
            rf"^\s*##\s+{re.escape(heading)}\s*$",
            re.MULTILINE,
        )
        if pattern.search(content) is None:
            errors.append(f"Missing section: ## {heading}")

    if HUMAN_DECISION_PATTERN.search(content) is None:
        errors.append("Missing line: Human decision required:")

    return errors


def main(argv: list[str]) -> int:
    """Validate the report and return a process exit code."""
    if len(argv) > 2:
        print(
            f"Usage: {Path(argv[0]).name} [review_report.md]",
            file=sys.stderr,
        )
        return 2

    report_path = (
        Path(argv[1]) if len(argv) == 2 else Path("review_report.md")
    )
    errors = validate_report(report_path)

    if errors:
        print("Review report format is invalid.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Review report format is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))