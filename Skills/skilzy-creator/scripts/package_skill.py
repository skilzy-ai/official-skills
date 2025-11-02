#!/usr/bin/env python3
import json, zipfile, argparse
from pathlib import Path
import sys

try:
    from validate_skill import do_validation
except ImportError: print("Error: 'validate_skill.py' not found.", file=sys.stderr); sys.exit(1)

def package_skill(skill_path: Path, output_dir: Path, custom_name: str = None):
    print(f"📦 Starting package process for {skill_path.name}...")
    is_valid, messages = do_validation(str(skill_path))
    if not is_valid:
        print(f"\n❌ Validation failed for {skill_path.name}. Cannot package:")
        for msg in messages: print(msg)
        return False, None
    print(f"✅ Skill '{skill_path.name}' is valid, proceeding with packaging.")
    manifest = json.loads((skill_path / 'skill.json').read_text(encoding='utf-8'))

    # FIXED: Changed .skill.zip to .skill
    archive_file_name = custom_name if custom_name else f"{manifest['name']}-{manifest['version']}.skill"

    output_path = output_dir / archive_file_name
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"- Creating archive: {output_path}")
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in skill_path.rglob('*'):
                if not file_path.is_dir():
                    # FIXED: Preserve skill directory as root folder in archive
                    # Instead of: file_path.relative_to(skill_path)
                    # Use: skill_path.name / file_path.relative_to(skill_path)
                    arcname = Path(skill_path.name) / file_path.relative_to(skill_path)
                    zf.write(file_path, arcname)
    except Exception as e:
        print(f"\n❌ Failed during zip creation: {e}")
        return False, None

    print(f"✨ Successfully packaged skill to: {output_path}")
    return True, output_path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory", nargs='?', default='.')
    parser.add_argument("-o", "--output-dir", default="dist")
    parser.add_argument("--output-name", help="Specify a custom name for the output zip file.")
    args = parser.parse_args()
    package_skill(Path(args.skill_directory), Path(args.output_dir), custom_name=args.output_name)

if __name__ == "__main__":
    main()
