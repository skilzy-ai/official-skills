# Skilzy Skill Creator

A comprehensive toolset for creating, converting, validating, and packaging Skilzy-compliant AI agent skills.

## Overview

Skilzy Skill Creator provides everything needed to build professional skills for the Skilzy.ai universal skills registry. Whether you're creating a new skill from scratch, converting an existing Claude skill, or preparing a skill for distribution, this toolset guides you through the entire process with automated validation and packaging.

## Features

- **🎯 Guided Workflow** - Step-by-step process from concept to published skill
- **🛠️ Four Powerful Tools** - Initialize, convert, validate, and package skills
- **📚 Dual Documentation** - Separate docs for AI agents (SKILL.md) and humans (README.md)
- **✅ Automated Validation** - Ensure compliance with Skilzy specifications
- **📦 One-Click Packaging** - Create distributable `.skill` archives
- **🔄 Claude Compatibility** - Convert existing Claude skills to Skilzy format
- **📖 Complete Reference** - Detailed documentation for every aspect of skill creation

## When to Use This Skill

Use Skilzy Skill Creator when you want to:

- Create a new skill from scratch
- Convert a Claude skill to Skilzy format
- Validate an existing skill's structure and compliance
- Package a skill for distribution to the registry
- Learn best practices for effective skill design
- Update or iterate on an existing skill

## Installation

```bash
skilzy install skilzy/skilzy-creator
```

## The Four Tools

### 1. Initialize New Skills

Create a complete skill directory structure with all required files:

```bash
python scripts/init_skill.py my-new-skill --non-interactive
```

### 2. Convert Claude Skills

Migrate existing Claude skills to Skilzy format:

```bash
python scripts/convert_skill.py path/to/claude-skill.skill
```

### 3. Validate Skills

Check compliance with Skilzy specifications:

```bash
python scripts/validate_skill.py path/to/my-skill/
```

### 4. Package for Distribution

Create a distributable `.skill` archive:

```bash
python scripts/package_skill.py path/to/my-skill/ -o dist/
```

## Requirements

- Python 3.9 or higher
- Dependencies: `PyYAML`, `jsonschema`


## Learn More

- **Complete workflow guide** - See SKILL.md for the full creation process
- **Tool references** - Detailed docs in `references/tool-*.md` files
- **Schema reference** - Full specification in `references/schema-reference.md`
- **Troubleshooting** - Common errors in `references/troubleshooting.md`
- **Examples** - Real skill.json files in `references/examples.md`

## Support

- **Skilzy Registry**: https://skilzy.ai
- **Documentation**: https://skilzy.ai/docs