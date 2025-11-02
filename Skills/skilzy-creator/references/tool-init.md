# Tool Reference: init_skill.py

## Purpose

Create a new, valid Skilzy skill directory with all required files and proper structure. This tool eliminates manual setup and ensures every new skill starts with a compliant foundation.

## Command Syntax

```bash
python scripts/init_skill.py <skill-name> [options]
```
### Non-Interactive Options

For AI agents and automated workflows:

**Required:**
- `<skill-name>` - Skill name in hyphen-case
- `--description` - Description (20-250 chars)

**Optional:**
- `--author` - Author name (default: "Unknown")
- `--license` - License identifier (default: "MIT")
- `--keywords` - Comma-separated: "pdf,data,analysis"
- `--repository` - Git URL: "https://github.com/user/repo"
- `--python-deps` - Packages: "pandas>=2.0,numpy>=1.20"
- `--system-deps` - Tools: "ffmpeg,imagemagick"

**Example:**
```bash
python scripts/init_skill.py web-scraper \
  --non-interactive \
  --description "Scrapes websites and extracts structured data. Use when users need web data extraction." \
  --author "Data Team" \
  --keywords "web,scraping,html,data" \
  --python-deps "requests>=2.31,beautifulsoup4>=4.12" \
  --system-deps "chromium-driver"
```

This creates a complete skill with all metadata populated.


### Arguments

- `<skill-name>` - Name of the skill to create (required)
  - Must be lowercase with hyphens (e.g., `data-analyzer`, not `data_analyzer`)
  - Will be used as the directory name
  - Will be set in skill.json `name` field

### Options

- `--non-interactive` - Use default values without prompting
- `--path <directory>` - Output directory for the skill (default: current directory)

## What It Creates

The initialization script generates a complete skill directory:

```
<skill-name>/
├── skill.json                 # Skilzy manifest with default metadata
├── SKILL.md                   # Agent instructions with YAML frontmatter
├── README.md                  # Human-readable documentation template
├── LICENSE                    # MIT license placeholder
├── assets/
│   └── icon.svg              # Default SVG icon
├── scripts/
│   └── example_script.py     # Example executable script
└── references/
    └── example_reference.md  # Example reference documentation
```

## Interactive vs Non-Interactive Mode

### Interactive Mode (Default)

When run without `--non-interactive`, the script prompts for:

1. **Skill name** (if not provided as argument)
   - Must match pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
   - Example: `web-scraper`, `pdf-processor`

2. **Description** for skill.json
   - Must be 20-250 characters
   - Should specify what the skill does and when to use it
   - Example: "Extracts data from websites using customizable scraping rules. Use when users need to collect structured data from HTML pages."

3. **Author name**
   - Your name or organization
   - Default: "Unknown"

4. **License**
   - Keyboard-driven selector with common options:
     - MIT (default)
     - Apache-2.0
     - GPL-3.0
     - BSD-3-Clause
     - Proprietary

5. **Repository URL** (optional)
   - Git repository for the skill
   - Can be left empty

### Non-Interactive Mode

When run with `--non-interactive`:

**Default values used:**
- `author`: "Unknown"
- `description`: "A Skilzy AI agent skill"
- `license`: "MIT"
- `repository`: null (not included)
- All prompts skipped

**Usage:**
```bash
python scripts/init_skill.py data-processor --non-interactive
```

**Ideal for:**
- Automated workflows
- Testing
- Quick prototyping
- AI agent-driven creation

## Generated File Contents

### skill.json

Generated with these defaults:

```json
{
  "name": "skill-name",
  "version": "0.1.0",
  "description": "Provided description or default",
  "author": "Provided author or Unknown",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "python": [],
    "system": [],
    "skills": []
  },
  "keywords": []
}
```

### SKILL.md

Generated with YAML frontmatter and TODO placeholders:

```markdown
---
name: skill-name
description: "[TODO: Complete this with an informative explanation of what the skill does and when to use it. Include specific scenarios, file types, or tasks that trigger it.]"
---

# Skill Name

[TODO: Describe the purpose of this skill in a few sentences.]

## When to Use

[TODO: Specify when this skill should be used. What user requests or scenarios trigger this skill?]

## How to Use

[TODO: Provide step-by-step instructions for how an AI agent should use this skill.]

### Bundled Resources

**Scripts:**
- `scripts/example_script.py` - [TODO: Describe what this script does]

**References:**
- `references/example_reference.md` - [TODO: Describe what this reference contains]

**Assets:**
- `assets/icon.svg` - Skill icon for registry display
```

### README.md

Generated with human-friendly template:

```markdown
# Skill Name

[TODO: Brief description of what this skill does]

## Features

- [TODO: List key features]
- [TODO: List capabilities]

## Installation

```bash
skilzy install <author>/skill-name.skill
```

## Usage

[TODO: Provide examples of how users would invoke this skill]

## Requirements

[TODO: List any prerequisites or dependencies]

## License

MIT License - See LICENSE file for details
```

### LICENSE

MIT License placeholder with copyright year and author name.

### assets/icon.svg

Default SVG icon (simple geometric shape) that can be replaced with custom branding.

### scripts/example_script.py

Example Python script demonstrating structure:

```python
#!/usr/bin/env python3
"""
Example script for skill-name.

This is a template script. Replace with actual functionality.
"""

def main():
    """Main entry point for the script."""
    print("Example script executed successfully")
    # TODO: Implement actual functionality

if __name__ == "__main__":
    main()
```

### references/example_reference.md

Example reference documentation:

```markdown
# Example Reference

This is an example reference file. Replace with actual documentation.

## Purpose

[TODO: Describe what information this reference provides]

## Contents

[TODO: Add detailed reference information, schemas, API docs, etc.]
```

## Example Workflows

### Workflow 1: Quick Prototyping (Non-Interactive)

```bash
# Create skill with defaults
python scripts/init_skill.py web-scraper --non-interactive

# Directory created: web-scraper/
# Next: Edit files and add functionality
```

### Workflow 2: Interactive Setup

```bash
# Run in interactive mode
python scripts/init_skill.py

# Prompts:
# Skill name: pdf-processor
# Description: Extracts text and metadata from PDF files. Use when users upload PDFs.
# Author: John Doe
# License: [Select MIT]
# Repository: https://github.com/johndoe/pdf-processor

# Directory created: pdf-processor/
# All metadata populated from prompts
```

### Workflow 3: Custom Output Directory

```bash
# Create skill in specific location
python scripts/init_skill.py data-analyzer --path ~/projects/skills/ --non-interactive

# Directory created: ~/projects/skills/data-analyzer/
```

## After Initialization

Once the skill is initialized, follow these steps:

1. **Delete example files** not needed for your skill:
   ```bash
   rm scripts/example_script.py
   rm references/example_reference.md
   ```

2. **Update SKILL.md**:
   - Replace all [TODO] placeholders
   - Complete the description in YAML frontmatter
   - Add actual instructions for agent usage

3. **Update README.md**:
   - Replace all [TODO] placeholders
   - Add real features and examples
   - Update installation instructions

4. **Update skill.json**:
   - Add keywords for discoverability
   - Add dependencies (Python packages, system tools)
   - Update description if needed

5. **Add actual resources**:
   - Create real scripts in `scripts/`
   - Create real references in `references/`
   - Add assets to `assets/`

6. **Validate the skill**:
   ```bash
   python scripts/validate_skill.py skill-name/
   ```

## Common Issues

### Error: "Skill directory already exists"

**Cause:** A directory with that name already exists

**Fix:** Choose a different name or delete the existing directory

### Error: "Invalid skill name format"

**Cause:** Skill name contains uppercase letters, underscores, or special characters

**Fix:** Use only lowercase letters, numbers, and hyphens (e.g., `my-skill-name`)

### Error: "Description too short"

**Cause:** In interactive mode, provided description is under 20 characters

**Fix:** Provide a more detailed description (minimum 20 characters)

## Best Practices

1. **Use descriptive names** - `pdf-processor` instead of `pdf-tool`
2. **Run non-interactively** when AI agents create skills (avoids prompts)
3. **Customize immediately** - Replace TODOs while context is fresh
4. **Delete unused examples** - Keep only needed resource directories
5. **Validate early** - Run validation after initial edits