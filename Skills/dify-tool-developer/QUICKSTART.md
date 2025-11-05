# Quick Start Guide

## Installation

```bash
skilzy install dify-tool-developer-1.1.0.skill
```

## First Use

### Step 1: Install Dify CLI (if needed)

**Option A: Automated (Recommended)**
```bash
python scripts/install_cli.py
```

**Option B: Manual**
```bash
# Load official instructions
bash scripts/fetch_doc.sh init

# Follow platform-specific instructions from the doc
```

### Step 2: Create Your First Plugin

Tell your AI agent:
> "Create a simple calculator tool plugin for Dify"

The agent will:
1. Ask clarifying questions about functionality
2. Install/verify CLI with helper script
3. Load official documentation (mandatory)
4. Initialize project with `dify plugin init`
5. Generate code following official patterns
6. Test and debug
7. Package to .difypkg file

### Step 3: Use Your Plugin

Install the generated plugin in Dify:
```bash
# Copy to Dify plugins directory
cp your-plugin-name.difypkg ~/dify/plugins/
```

## Features You Get

- ✅ Automated CLI installation
- ✅ Structured 5-phase workflow
- ✅ Mandatory official doc loading
- ✅ Error prevention & troubleshooting
- ✅ Real-world examples
- ✅ Complete CLI reference

## Helper Scripts

### Install Dify CLI
```bash
python scripts/install_cli.py
python scripts/install_cli.py --version 0.4.0
python scripts/install_cli.py --path ~/bin
```

### Fetch Documentation
```bash
bash scripts/fetch_doc.sh tool    # Tool plugin guide
bash scripts/fetch_doc.sh oauth   # OAuth guide
bash scripts/fetch_doc.sh debug   # Debugging guide
bash scripts/fetch_doc.sh init    # CLI installation guide
```

## Reference Files

Load these as needed:
- `references/doc-map.md` - What each official doc contains
- `references/workflow.md` - Complete development process
- `references/cli-commands.md` - CLI command reference
- `references/troubleshooting.md` - Error solutions
- `references/examples.md` - Working plugin examples

## Support

- Dify Docs: https://docs.dify.ai/plugin-dev-en/
- Dify GitHub: https://github.com/langgenius/dify
