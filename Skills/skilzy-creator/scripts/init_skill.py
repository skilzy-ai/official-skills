#!/usr/bin/env python3
import os, json, re, argparse, subprocess
from pathlib import Path

ICON_CONTENT = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.23L19.77 7 12 11.77 4.23 7 12 4.23zM3 8.5l9 5.06v9.44L3 17.5V8.5zm18 0v9l-9 5.06v-9.44L21 8.5z"/></svg>'

SKILL_MD_TEMPLATE = """---
name: {skill_name}
description: {description}
---

# {skill_title}

## Purpose

This skill enables you to...

## When to Use

Use this skill when...

## Instructions

### Step 1: Initial Setup

[Describe what the agent should do first]

### Step 2: Main Processing

[Provide detailed instructions]

### Bundled Resources

**Scripts:**
- `scripts/example.py` - [Describe purpose]

**References:**
- `references/example.md` - [Describe content]
"""

README_MD_TEMPLATE = """# {skill_title}

## Overview

{description}

## Features

- Feature 1: [Description]
- Feature 2: [Description]
- Feature 3: [Description]

## Installation

```bash
skilzy install {author}/{skill_name}.skill
```

## Usage

[Provide examples of how users would invoke this skill]

## Requirements

{requirements_section}

## License

{license}
"""

def get_git_user_name():
    try: return subprocess.run(["git", "config", "--get", "user.name"], capture_output=True, text=True, check=False).stdout.strip()
    except Exception: return ""

def create_skill_scaffold(data):
    skill_dir = Path(data['name'])
    print(f"\n🚀 Initializing skill: {skill_dir}...\n")
    if skill_dir.exists():
        print(f"❌ Error: Directory '{skill_dir}' already exists.")
        return False
    try:
        skill_dir.mkdir()
        for sub_dir in ["assets", "scripts", "references"]: (skill_dir / sub_dir).mkdir()

        # Write skill.json
        with open(skill_dir / "skill.json", 'w') as f: 
            json.dump(data, f, indent=2)

        skill_title = data['name'].replace('-', ' ').title()

        # Write SKILL.md with frontmatter
        skill_md_content = SKILL_MD_TEMPLATE.format(
            skill_name=data['name'],
            description=data['description'],
            skill_title=skill_title
        )
        (skill_dir / "SKILL.md").write_text(skill_md_content)

        # Generate requirements section for README
        requirements = []
        if data.get('dependencies', {}).get('python'):
            requirements.append(f"**Python packages:** {', '.join(data['dependencies']['python'])}")
        if data.get('dependencies', {}).get('system'):
            requirements.append(f"**System tools:** {', '.join(data['dependencies']['system'])}")

        requirements_section = "\n".join(requirements) if requirements else "No external dependencies required."

        # Write README.md
        readme_content = README_MD_TEMPLATE.format(
            skill_title=skill_title,
            description=data['description'],
            author=data.get('author', 'unknown'),
            skill_name=data['name'],
            requirements_section=requirements_section,
            license=data.get('license', 'MIT')
        )
        (skill_dir / "README.md").write_text(readme_content)

        # Write LICENSE
        (skill_dir / data['licenseFile']).write_text(f"Licensed under {data['license']}.")

        # Write icon
        (skill_dir / data['icon']).write_text(ICON_CONTENT)

        print(f"✅ Created directory and all required files for '{data['name']}'.")
    except Exception as e:
        print(f"❌ Error during file creation: {e}")
        if skill_dir.exists(): import shutil; shutil.rmtree(skill_dir)
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description='Initialize a new Skilzy skill')
    parser.add_argument("skill_name", nargs='?', default=None, help='Name of the skill (hyphen-case)')
    parser.add_argument("--non-interactive", action='store_true', help='Run without prompts')
    parser.add_argument("--description", help='Skill description (20-250 chars)')
    parser.add_argument("--author", help='Author name or organization')
    parser.add_argument("--license", default="MIT", help='License (default: MIT)')
    parser.add_argument("--keywords", help='Comma-separated keywords (e.g., "pdf,data,analysis")')
    parser.add_argument("--repository", help='Git repository URL')
    parser.add_argument("--python-deps", help='Comma-separated Python dependencies (e.g., "pandas>=2.0,numpy")')
    parser.add_argument("--system-deps", help='Comma-separated system dependencies (e.g., "ffmpeg,imagemagick")')

    args = parser.parse_args()

    try:
        if args.non_interactive:
            # Non-interactive mode - use arguments or defaults
            if not args.skill_name:
                print("❌ Error: skill_name is required in non-interactive mode")
                return

            if not args.description:
                print("❌ Error: --description is required in non-interactive mode")
                return

            data = {
                'name': args.skill_name,
                'author': args.author or "Unknown",
                'license': args.license,
                'version': "0.1.0",
                'entrypoint': 'README.md',
                'licenseFile': 'LICENSE',
                'icon': 'assets/icon.svg',
                'runtime': {"type": "python", "version": ">=3.9"},
                'description': args.description
            }

            # Add keywords if provided
            if args.keywords:
                data['keywords'] = [k.strip().lower() for k in args.keywords.split(',')]
            else:
                data['keywords'] = []

            # Add repository if provided
            if args.repository:
                data['repository'] = {
                    'type': 'git',
                    'url': args.repository
                }

            # Add dependencies
            dependencies = {}
            if args.python_deps:
                dependencies['python'] = [d.strip() for d in args.python_deps.split(',')]
            else:
                dependencies['python'] = []

            if args.system_deps:
                dependencies['system'] = [d.strip() for d in args.system_deps.split(',')]
            else:
                dependencies['system'] = []

            data['dependencies'] = dependencies

        else:
            # Interactive mode
            def_name = args.skill_name or "my-new-skill"
            data = {
                'name': input(f"Skill Name [{def_name}]: ") or def_name,
                'author': input(f"Author [{get_git_user_name() or 'Unknown'}]: ") or get_git_user_name() or "Unknown",
                'license': input("License [MIT]: ") or "MIT",
                'version': "0.1.0",
                'entrypoint': 'README.md',
                'licenseFile': 'LICENSE',
                'icon': 'assets/icon.svg',
                'runtime': {"type": "python", "version": ">=3.9"}
            }
            data['description'] = input("Description (for registry): ")

            # Optional fields
            keywords_input = input("Keywords (comma-separated, optional): ")
            if keywords_input:
                data['keywords'] = [k.strip().lower() for k in keywords_input.split(',')]
            else:
                data['keywords'] = []

            repo_input = input("Repository URL (optional): ")
            if repo_input:
                data['repository'] = {'type': 'git', 'url': repo_input}

            python_deps = input("Python dependencies (comma-separated, optional): ")
            system_deps = input("System dependencies (comma-separated, optional): ")

            dependencies = {}
            if python_deps:
                dependencies['python'] = [d.strip() for d in python_deps.split(',')]
            else:
                dependencies['python'] = []

            if system_deps:
                dependencies['system'] = [d.strip() for d in system_deps.split(',')]
            else:
                dependencies['system'] = []

            data['dependencies'] = dependencies

        if create_skill_scaffold(data): 
            print("\n✨ Skill initialized successfully!")
    except (ValueError, KeyboardInterrupt) as e: 
        print(f"\n❌ Aborted: {e}")

if __name__ == "__main__":
    main()
