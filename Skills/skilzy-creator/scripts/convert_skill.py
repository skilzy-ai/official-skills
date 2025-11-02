#!/usr/bin/env python3
import os, json, re, argparse, subprocess, zipfile, tempfile, shutil, sys
from pathlib import Path

# FIXED: Added 'import sys' to imports
try:
    import yaml
except ImportError: print("PyYAML not found", file=sys.stderr); sys.exit(1)

def analyze_source(search_dir: Path):
    skill_md_path = next(search_dir.rglob('SKILL.md'), None)
    if not skill_md_path: raise FileNotFoundError("SKILL.md not found in archive.")
    content = skill_md_path.read_text(errors='ignore')
    parts = content.split('---', 2)
    if len(parts) < 3: raise ValueError("SKILL.md has no frontmatter.")
    front_matter = yaml.safe_load(parts[1])
    return skill_md_path.parent, front_matter

def generate_converted_skill(data, source_dir: Path):
    dest_dir = Path(data['name'])
    if dest_dir.exists(): raise FileExistsError(f"Directory '{dest_dir}' exists.")
    shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
    readme_content = f"# {data['name']}\n\n{data['description']}"
    (dest_dir / "README.md").write_text(readme_content)
    (dest_dir / "skill.json").write_text(json.dumps(data, indent=2))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_zip")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as td:
        try:
            zipfile.ZipFile(args.source_zip).extractall(td)
            s_dir, fm = analyze_source(Path(td))
            data = {
                'name': fm.get('name', 'converted-skill'),
                'description': fm.get('description', 'A converted skill.'),
                'author': fm.get('author', 'Converted'),
                'license': fm.get('license', 'MIT'),
                'version': '1.0.0',
                # FIXED: Changed entrypoint from 'SKILL.md' to 'README.md'
                'entrypoint': 'README.md'
            }
            generate_converted_skill(data, s_dir)
            print(f"✨ Successfully converted '{data['name']}' with backwards compatibility.")
        except Exception as e: print(f"❌ Conversion failed: {e}")

if __name__ == "__main__": main()
