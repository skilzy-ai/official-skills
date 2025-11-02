#!/usr/bin/env python3
import json
from pathlib import Path
import sys

try:
    import jsonschema
except ImportError: print("jsonschema not installed. Run: pip install jsonschema", file=sys.stderr); sys.exit(1)

SKILL_SCHEMA = {"$schema":"http://json-schema.org/draft-07/schema#","title":"Skilzy Skill Manifest","type":"object","properties":{"name":{"type":"string","pattern":"^[a-z0-9]+(-[a-z0-9]+)*$","maxLength":40},"version":{"type":"string","pattern":"^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"},"description":{"type":"string","minLength":20,"maxLength":250},"author":{"type":"string"},"license":{"type":"string"},"licenseFile":{"type":"string"},"entrypoint":{"type":"string","default":"README.md"}},"required":["name","version","description","author","license","entrypoint"]}

def do_validation(skill_dir: str) -> tuple[bool, list[str]]:
    skill_path, errors = Path(skill_dir).resolve(), []
    manifest_path = skill_path / "skill.json"
    if not manifest_path.exists(): return False, ["skill.json not found."]
    try: manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e: return False, [f"skill.json is invalid JSON: {e}"]
    schema_errors = sorted(jsonschema.Draft7Validator(SKILL_SCHEMA).iter_errors(manifest), key=lambda e: str(e.path))
    if schema_errors: errors.extend([f"Schema error at {'.'.join(map(str,e.path)) or 'root'}: {e.message}" for e in schema_errors])
    if skill_path.name != manifest.get("name"): errors.append(f"Dir name '{skill_path.name}' != manifest name '{manifest.get('name')}'.")
    for field in ["icon", "licenseFile", "entrypoint"]:
        if path_str := manifest.get(field):
            if not (skill_path / path_str).exists(): errors.append(f"{field} path '{path_str}' not found.")
    if errors: return False, errors
    return True, ["✅ Skill is valid!"]

def main():
    if len(sys.argv) != 2: print("Usage: python validate_skill.py <path/to/dir>"); sys.exit(1)
    is_valid, messages = do_validation(sys.argv[1])
    print("--- Validation Summary ---")
    for msg in messages:
        print(msg)
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
