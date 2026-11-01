"""Validate the distributable skill and documentation without network access.

This checks packaging invariants, not model behavior. Run from any directory:
    python scripts/validate.py
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

try:
    import yaml
except ImportError:
    raise SystemExit("Install validation dependencies: python -m pip install -r requirements-dev.txt")


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "einstein-skill"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate() -> tuple[int, int]:
    source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", source, re.DOTALL)
    require(match is not None, "SKILL.md needs YAML frontmatter and LF line endings")
    metadata = yaml.safe_load(match.group(1))
    require(isinstance(metadata, dict), "Skill frontmatter must be a mapping")
    name = metadata.get("name")
    require(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), "Invalid skill name")
    require(name == SKILL.name and len(name) <= 64, "Name must match the skill directory and be at most 64 characters")
    description = metadata.get("description")
    require(isinstance(description, str) and 0 < len(description.strip()) <= 1024, "Missing or oversized description")
    require(metadata.get("license") == "MIT" and (ROOT / "LICENSE").is_file(), "License declaration or file missing")
    require((SKILL / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(), "Installed skill must carry the package license")
    require(len(source.splitlines()) < 500, "Keep the entrypoint below 500 lines")
    custom = metadata.get("metadata", {})
    require(isinstance(custom, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in custom.items()), "metadata keys and values must be strings")

    agent = yaml.safe_load((SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    interface = agent.get("interface", {})
    require(interface.get("display_name") == "Einstein-skill", "Display name missing or inconsistent")
    short = interface.get("short_description", "")
    require(isinstance(short, str) and 25 <= len(short) <= 64, "Short description must be 25-64 characters")
    require(f"${name}" in interface.get("default_prompt", ""), "Default prompt must invoke the skill")
    require(agent.get("policy", {}).get("allow_implicit_invocation", True) is True, "Automatic discovery must stay enabled")

    documents = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")), *sorted(SKILL.rglob("*.md"))]
    links = 0
    for document in documents:
        text = document.read_text(encoding="utf-8")
        targets = re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text)
        targets += re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', text)
        for target in targets:
            target = target.strip().removeprefix("<").removesuffix(">")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (document.parent / unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(ROOT), f"Link escapes package in {document.relative_to(ROOT)}: {target}")
            require(resolved.exists(), f"Broken link in {document.relative_to(ROOT)}: {target}")
            # A copied skill must not depend on files outside its own folder.
            if document.is_relative_to(SKILL):
                require(resolved.is_relative_to(SKILL), f"Skill resource isn't self-contained: {target}")
            links += 1

    hero = ET.parse(ROOT / "assets" / "hero.svg").getroot()
    require(hero.tag == "{http://www.w3.org/2000/svg}svg", "Hero isn't an SVG document")

    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    require(isinstance(cases, list) and len(cases) > 0, "Evaluation cases missing")
    seen: set[str] = set()
    for case in cases:
        require(isinstance(case, dict), "Each case must be an object")
        for field in ("id", "context", "prompt"):
            require(isinstance(case.get(field), str) and bool(case[field].strip()), f"Case needs {field}")
        require(case["id"] not in seen, f"Duplicate case ID: {case['id']}")
        seen.add(case["id"])
        for field in ("expected", "reject"):
            values = case.get(field)
            require(isinstance(values, list) and len(values) > 0 and all(isinstance(v, str) and bool(v.strip()) for v in values), f"Invalid {field} criteria in {case['id']}")

    return links, len(cases)


if __name__ == "__main__":
    try:
        link_count, case_count = validate()
    except (ValueError, OSError, yaml.YAMLError, ET.ParseError, TypeError, AttributeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: skill metadata, agent metadata, {link_count} local links, SVG, {case_count} evaluation case definitions")
    print("Package checks only; no model behavior evaluation was executed.")
