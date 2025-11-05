# Dify Tool Plugin Developer

Transform your AI agent into an expert Dify plugin developer with structured workflow guidance and mandatory documentation loading.

## Overview

This Skilzy skill guides AI agents through the complete lifecycle of Dify tool plugin development using official documentation and direct CLI commands. It's a **workflow guide**, not an automation wrapper—teaching agents the proper sequence, best practices, and when to load specific documentation.

## What It Does

- 🎯 **Requirements Gathering** - Structured questioning to define plugin scope
- 📋 **Project Planning** - Determine permissions, dependencies, and architecture
- 🚀 **Automated Initialization** - Use Dify CLI with correct flags
- 💻 **Code Implementation** - Follow exact patterns from official docs
- 🧪 **Testing & Debugging** - Local testing with comprehensive logging
- ✅ **Validation** - Verify structure and code correctness
- 📦 **Packaging** - Create distributable `.difypkg` files
- 🌐 **Publishing Guidance** - Marketplace submission assistance

## Key Features

### Mandatory Documentation Loading

⚠️ **Critical Difference:** This skill **enforces** loading official Dify documentation before writing any code. The Dify plugin framework has strict syntax requirements—exact class structures, specific method signatures, precise YAML formats. No guessing, no assumptions.

**Documentation Strategy:**
- **Embedded** quick references for offline capability
- **Dynamic** fetching of official docs for accuracy
- **Enforced** loading at specific workflow phases

### 5-Phase Workflow

1. **Setup & Planning** - Gather requirements, verify CLI
2. **Initialize Project** - Create structure with `dify plugin init`
3. **Implement Tool** - Write YAML configs and Python code
4. **Test & Debug** - Run locally, fix issues, add logging
5. **Package & Publish** - Create `.difypkg`, optionally publish

### Comprehensive References

- **doc-map.md** - What each official doc contains and when to load it
- **workflow.md** - Detailed 5-phase development process
- **cli-commands.md** - Complete Dify CLI command reference
- **troubleshooting.md** - Common errors and solutions
- **examples.md** - Real-world plugin examples

### Helper Scripts

- **fetch_doc.sh** - Quick official documentation retrieval
- **install_cli.py** - Automated Dify CLI installation with platform detection

### Automated CLI Installation

Includes a Python helper script that automatically:
- Detects your OS and architecture
- Downloads the latest Dify CLI from GitHub
- Makes it executable
- Verifies installation
- Provides PATH setup instructions

Simply run: `python scripts/install_cli.py`

## When to Use

Install this skill when you want to:

- Create custom tools for Dify
- Extend Dify with new capabilities
- Develop plugins with OAuth authentication
- Build API integrations for Dify
- Learn Dify plugin development best practices

## Installation

```bash
skilzy install your-author-name/dify-tool-developer.skill
```

## Usage Examples

### Example 1: "Create a weather tool plugin for Dify"

The agent will:

1. **Phase 1 - Planning:**
   - Ask: "Does it need API access? Which weather API?"
   - Ask: "Does it require an API key?"
   - Ask: "What inputs should users provide? (city name, units)"
   - Determine: Network permission needed

2. **Phase 2 - Initialize:**
   - Load `tool-plugin.md` documentation (MANDATORY)
   - Run: `dify plugin init --name weather-tool --allow-network --quick`
   - Verify structure created

3. **Phase 3 - Implement:**
   - Re-load `tool-plugin.md` "Developing" section (MANDATORY)
   - Edit `tools/weather.yaml` with exact syntax
   - Edit `tools/weather.py` following Tool class pattern
   - Add API key handling in `provider/weather-tool.py`

4. **Phase 4 - Test:**
   - Load `debugging-logs.md`
   - Add logging to tool
   - Run `python -m main`
   - Debug any errors using troubleshooting.md

5. **Phase 5 - Package:**
   - Run: `dify plugin package ./weather-tool`
   - Output: `weather-tool.difypkg` ready for use

### Example 2: "Build a GitHub integration with OAuth"

The agent will:

1. **Planning Phase:**
   - Identify OAuth requirement
   - Determine GitHub API scopes needed
   - Plan tool functionality (list issues, create PRs, etc.)

2. **Initialize:**
   - Load docs
   - Init with network permission

3. **Implement:**
   - Load `tool-oauth.md` (MANDATORY for OAuth)
   - Implement OAuth schema in provider YAML
   - Add OAuth methods in provider Python
   - Access tokens in tools

4. **Test OAuth flow:**
   - Test authorization
   - Verify token access
   - Test API calls with token

5. **Package and deliver**

### Example 3: "Debug my Dify plugin - it has import errors"

The agent will:

1. Load `troubleshooting.md`
2. Analyze the error message
3. Identify the issue (e.g., "Multiple Tool subclasses")
4. Provide specific solution
5. Guide through fixes
6. Re-test

## How It Works

### Documentation-First Approach

```
User Request
    ↓
Load doc-map.md (understand what docs exist)
    ↓
Phase 1: Planning → Load references/workflow.md
    ↓
Phase 2: Initialize → MANDATORY: Load tool-plugin.md
    ↓
Phase 3: Implement → MANDATORY: Re-load tool-plugin.md
    ↓
    If OAuth needed → MANDATORY: Load tool-oauth.md
    ↓
Phase 4: Test → Load debugging-logs.md
    ↓
    If errors → Load troubleshooting.md
    ↓
Phase 5: Package → Verify, package, deliver
```

### Direct CLI Usage

No Python wrappers—use `dify` CLI commands directly:

```bash
# Initialize
dify plugin init --name tool-name --quick

# Test
cd tool-name && python -m main

# Package
dify plugin package ./tool-name
```

### Enforced Best Practices

The skill enforces Dify's strict requirements:

- ⚠️ ONE Tool class per `.py` file
- ⚠️ Exact `_invoke` method signature
- ⚠️ Use `.get()` for all parameters
- ⚠️ Return with `yield`, not `return`
- ⚠️ Precise YAML structure and indentation
- ⚠️ No local file I/O (serverless environment)

## What Makes This Different

### vs. Manual Development

- **With This Skill:** Structured 5-phase workflow, mandatory doc loading, error prevention
- **Manual:** Easy to skip docs, miss requirements, make syntax errors

### vs. Automation Scripts

- **This Skill:** Teaches proper patterns, enforces learning, uses official CLI
- **Wrappers:** Black box automation, harder to debug, may not follow latest practices

### vs. Generic Coding Assistants

- **This Skill:** Dify-specific knowledge, strict syntax enforcement, official docs integration
- **Generic:** May guess or improvise, doesn't know Dify requirements

## Requirements

- **System:** `curl` (for fetching documentation)
- **Dify CLI:** Installed and accessible (skill guides installation if needed)
- **Python:** 3.12+ (for running plugins locally)
- **Network:** Access to `docs.dify.ai` for documentation

## Documentation Structure

The skill includes comprehensive reference materials:

### references/doc-map.md
Maps all official Dify docs:
- What each document contains
- When to load it (with MANDATORY markers)
- Which sections are critical
- URLs for fetching

### references/workflow.md
Complete 5-phase development workflow:
- Objectives for each phase
- Prerequisites and steps
- Success criteria
- Time estimates

### references/cli-commands.md
Dify CLI command reference:
- Initialization patterns
- Permission flags
- Testing commands
- Packaging options
- Common patterns and examples

### references/troubleshooting.md
Error catalog with solutions:
- Import errors (Multiple Tool classes, wrong names)
- Structure errors (file organization, signatures)
- Parameter errors (KeyError, validation)
- Credential errors (API keys, OAuth)
- Runtime errors (timeouts, async issues)
- Packaging errors (YAML, missing files)

### references/examples.md
Real-world plugin examples:
- Simple API tool (Weather)
- Text processing (no API)
- Multi-tool plugin (Calculator)
- OAuth tool (GitHub)
- Common patterns and testing

## Workflow Phases Explained

### Phase 1: Setup & Planning (15-30 min)
Gather requirements through structured questions. Determine tool name, permissions, dependencies, OAuth needs. Verify Dify CLI installed.

### Phase 2: Initialize Project (5-10 min)
Load official docs, construct `dify plugin init` command with appropriate flags, execute, verify structure.

### Phase 3: Implement Tool (1-3 hours)
Edit YAML configurations, implement Tool class following exact patterns, add credential validation if needed, update manifest. **MANDATORY doc loading before coding.**

### Phase 4: Test & Debug (30 min - 2 hours)
Add logging, run locally with `python -m main`, debug errors using troubleshooting guide, iterate until working.

### Phase 5: Package & Publish (10-15 min)
Final validation, create `.difypkg` with `dify plugin package`, optionally publish to marketplace.

**Total Time:** 2-6 hours depending on complexity

## Best Practices Enforced

✅ **Always do:**
- Load documentation before coding
- Follow exact syntax from docs
- Use one Tool class per file
- Handle errors comprehensively
- Test before packaging
- Add logging for debugging

❌ **Never do:**
- Guess at syntax or structure
- Skip mandatory documentation loading
- Put multiple Tool classes in one file
- Use local file I/O operations
- Assume parameters exist without checking
- Package without testing

## Troubleshooting

Common issues and quick fixes:

| Problem | Quick Fix |
|---------|-----------|
| Import error | Check spelling, use exact names from definitions |
| Multiple Tool classes error | One class per file, move extras to new files |
| KeyError for parameter | Use `.get()` method, don't access directly |
| YAML syntax error | Check indentation (spaces not tabs) |
| Package creation fails | Verify all files exist, check manifest paths |
| API timeout | Add `timeout=10` parameter to requests |
| Credential validation fails | Test API key manually first |

See `references/troubleshooting.md` for complete error catalog.

## Contributing

This skill follows the Dify official documentation. When Dify updates their docs or adds new features, this skill can be updated to reflect the latest best practices.

## License

MIT License - See LICENSE file for details.

## Support

- Official Dify Docs: https://docs.dify.ai/plugin-dev-en/
- Dify GitHub: https://github.com/langgenius/dify
- Plugin Daemon: https://github.com/langgenius/dify-plugin-daemon

## Version

**1.0.0** - Initial release

Focused on tool plugin development with mandatory documentation loading and direct CLI usage.
