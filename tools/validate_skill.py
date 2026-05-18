#!/usr/bin/env python3
"""Basic local validator for the gentle-curiosity-flowcurrent skill package."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print("ERROR: PyYAML is required to validate frontmatter.")
    raise SystemExit(2) from exc

REQUIRED_FILES = [
    "SKILL.md",
    "references/source-model.md",
    "references/flowcurrent-operating-protocol.md",
    "references/quadrant-diagnostics.md",
    "references/knowledge-cracks-and-belief-revision.md",
    "references/task-patterns.md",
    "references/safety-and-epistemic-boundaries.md",
    "references/terminology.md",
    "templates/task-immersion-card.md",
    "templates/flow-session-note.md",
    "templates/response-checklist.md",
    "examples/coding-flow.md",
    "examples/research-flow.md",
    "examples/creative-flow.md",
    "evals/evals.json",
]

NAME_RE = re.compile(r"^[a-z][a-z0-9_-]*$")


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md frontmatter is not closed")
    return yaml.safe_load(parts[1]) or {}


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    skill_md = root / "SKILL.md"
    if skill_md.exists():
        try:
            fm = read_frontmatter(skill_md)
        except Exception as exc:
            errors.append(str(exc))
            fm = {}

        name = fm.get("name")
        if name != root.name:
            errors.append(f"Frontmatter name {name!r} must match directory name {root.name!r}")
        if not isinstance(name, str) or not NAME_RE.match(name):
            errors.append("Frontmatter name must match ^[a-z][a-z0-9_-]*$")
        if not fm.get("description"):
            errors.append("Frontmatter description is required")
        if not fm.get("version"):
            errors.append("Frontmatter version is required")
        metadata = fm.get("metadata") or {}
        hermes = metadata.get("hermes") or {}
        tags = hermes.get("tags") or []
        for expected in ["gentle-curiosity", "flow-state", "agent-operating-mode"]:
            if expected not in tags:
                errors.append(f"Missing recommended Hermes tag: {expected}")
        if metadata.get("source_inspiration") != "https://flowstateguide.com/":
            errors.append("metadata.source_inspiration must cite https://flowstateguide.com/")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills/gentle-curiosity-flowcurrent")
    root = root.resolve()
    if not root.is_dir():
        print(f"ERROR: Not a directory: {root}")
        return 2
    errors = validate(root)
    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
