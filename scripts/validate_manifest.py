#!/usr/bin/env python3
"""Validate ai-research migration manifest invariants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "projects" / "manifest.json"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_STATUS = {
    "pre-flight",
    "ready-for-import",
    "hold",
    "attribution-review",
    "imported-verified",
    "integration-verified",
}
REQUIRED_FIELDS = {
    "name",
    "source_repository",
    "target_path",
    "layer",
    "status",
    "observed_main_sha",
    "blocker",
    "integration_notes",
}


def fail(message: str) -> None:
    print(f"manifest validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and SHA40.fullmatch(value) is not None


def nonempty_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and item.strip() for item in value)
    )


def main() -> None:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {MANIFEST.relative_to(ROOT)}: {exc}")

    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if data.get("umbrella") != "Lei-TzuY/ai-research":
        fail("umbrella must be Lei-TzuY/ai-research")

    projects = data.get("projects")
    if not isinstance(projects, list) or not projects:
        fail("projects must be a non-empty list")

    names: set[str] = set()
    sources: set[str] = set()
    targets: set[str] = set()

    for index, project in enumerate(projects):
        if not isinstance(project, dict):
            fail(f"projects[{index}] must be an object")
        missing = REQUIRED_FIELDS - project.keys()
        if missing:
            fail(f"projects[{index}] missing fields: {', '.join(sorted(missing))}")

        name = project["name"]
        source = project["source_repository"]
        target = project["target_path"]
        layer = project["layer"]
        status = project["status"]
        observed = project["observed_main_sha"]
        blocker = project["blocker"]
        notes = project["integration_notes"]

        if not isinstance(name, str) or not name:
            fail(f"projects[{index}].name must be non-empty")
        if source != f"Lei-TzuY/{name}":
            fail(f"{name}: source_repository must be Lei-TzuY/{name}")
        if target != f"projects/{name}":
            fail(f"{name}: target_path must be projects/{name}")
        if not isinstance(layer, str) or not layer.strip():
            fail(f"{name}: layer must be non-empty")
        if status not in ALLOWED_STATUS:
            fail(f"{name}: unsupported status {status!r}")
        if not valid_sha(observed):
            fail(f"{name}: observed_main_sha must be a 40-character lowercase hex SHA")
        if not isinstance(notes, str) or not notes.strip():
            fail(f"{name}: integration_notes must be non-empty")

        if name in names or source in sources or target in targets:
            fail(f"{name}: duplicate project identity/source/target")
        names.add(name)
        sources.add(source)
        targets.add(target)

        if status in {"hold", "pre-flight", "attribution-review"}:
            if not isinstance(blocker, str) or not blocker.strip():
                fail(f"{name}: {status} requires an explicit blocker")

        if status == "hold":
            prs = project.get("active_pr_numbers")
            if (
                not isinstance(prs, list)
                or not prs
                or not all(isinstance(number, int) and number > 0 for number in prs)
                or len(set(prs)) != len(prs)
            ):
                fail(f"{name}: HOLD requires non-empty unique active_pr_numbers")

        if status == "attribution-review":
            if not nonempty_strings(project.get("observed_attribution_evidence")):
                fail(f"{name}: attribution-review requires observed_attribution_evidence")

        if status == "ready-for-import":
            if blocker is not None:
                fail(f"{name}: READY entry cannot have a blocker")
            if project.get("source_ci_conclusion") != "success":
                fail(f"{name}: READY entry requires successful source CI evidence")
            if not isinstance(project.get("source_ci_run_id"), int):
                fail(f"{name}: READY entry requires an integer source_ci_run_id")
            contract = project.get("source_equivalent_ci")
            if not nonempty_strings(contract):
                fail(f"{name}: READY entry requires source_equivalent_ci")

        if status in {"imported-verified", "integration-verified"}:
            if blocker is not None:
                fail(f"{name}: verified status cannot retain a blocker")
            if not (ROOT / target).is_dir():
                fail(f"{name}: verified status requires an existing target subtree")
            if not valid_sha(project.get("imported_source_sha")):
                fail(f"{name}: verified import requires imported_source_sha")

    print(f"validated {len(projects)} AI research project entries")


if __name__ == "__main__":
    main()
