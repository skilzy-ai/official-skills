# 🚀 Official Skilzy Skills Repository

**Welcome to the official collection of AI Agent Skills for the Skilzy ecosystem!**

This repository contains community-contributed skills that extend AI agents' capabilities across platforms like Claude, ChatGPT, and any AI system with sandbox integration. Skills are the "apps for your AI workforce" - self-contained capability packages that make AI agents truly specialized.

---

## 🎯 What Are Skills?

Skills are modular capabilities that transform general-purpose AI agents into specialists. Each skill packages:

- **Instructions** - Workflows and best practices for AI agents
- **Scripts** - Executable code for reliable operations
- **Resources** - Documentation, templates, and reference materials

**Key Benefits:**

- ✅ **Publish once, use everywhere** - Works across Claude, ChatGPT, and all AI platforms
- ✅ **Eliminate repetition** - Stop rewriting the same instructions
- ✅ **Progressive disclosure** - Only loads content when needed
- ✅ **Community-driven** - Grow the ecosystem together

---

## 🚀 Quick Start

### For Users: Install Skills

**Option 1: Python SDK**
```bash
# Install the SDK
pip install skilzy

# Install any skill from this repository
skilzy install skilzy-admin/pdf-processor
skilzy install skilzy-admin/excel-analyzer
```

**Option 2: Browse the Registry** Visit skilzy.ai to **discover** and **publish** skills through the web interface.

### For Developers: Publish Your Own

**Option 1: Direct Publishing**

```bash
# Install CLI tool
# Download from: https://github.com/skilzy-ai/skilzy-cli/releases

# Create a new skill
skilzy init my-awesome-skill

# Package and publish
skilzy login --api-key "your_key"
skilzy package
skilzy publish dist/my-awesome-skill-0.1.0.skill
```

**Option 2: Contribute via Pull Request** (see below)

---

## 🤝 Contributing Skills

**We welcome community contributions!** You can add your skill to this official repository in two ways:

### Method 1: Direct Publishing (Recommended)

**Best for:** Individual developers, quick publishing

1. **Create your skill** using our tools:

   - **CLI Tool**: skilzy-cli - Go binary for all platforms
   - **Python SDK**: skilzy-python - Full Python integration

2. **Publish directly** to skilzy.ai:

   ```bash
   # Using Python SDK
   pip install skilzy
   skilzy login --api-key "your_key"
   skilzy publish your-skill.skill
   
   # Or via Web UI
   # Visit https://skilzy.ai/publish and upload your .skill file
   ```

3. **Your skill goes live** immediately after approval!

### Method 2: Contribute via Pull Request


#### 📋 Contribution Process

**Step 1: Fork & Clone**

```bash
git clone https://github.com/skilzy-ai/official-skills.git
cd official-skills
git checkout -b add-my-skill
```

**Step 2: Add Your Skill**

Create your skill in the appropriate category folder:

```
skills/
  └── your-skill-name/
      ├── skill.json         # Required: Skill manifest
      ├── SKILL.md           # Required: AI agent instructions
      ├── LICENSE            # Required: License file
      ├── README.md          # Optional: Human-readable docs (visible on the skilzy.ai regestry)
      ├── scripts/           # Optional: Executable code
      ├── references/        # Optional: Documentation
      └── assets/            # Optional: Icons, templates
```

**Step 3: Follow Our Standards**

✅ **Required Files:**

- `skill.json` - Valid manifest following our schema
- `SKILL.md` - Clear instructions for AI agents
- `LICENSE` - OSI-approved license (MIT, Apache-2.0, etc.)

✅ **skill.json example:**

```json
{
  "name": "image-editor",
  "version": "1.0.0",
  "description": "This skill should be used when users want to perform image editing operations including resize, rotate, crop, flip, brightness/contrast/saturation/sharpness adjustments, blur, filters, watermarks, or format conversion.",
  "author": "skilzy-ai",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "icon": "assets/icon.svg",
  "entrypoint": "README.md",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "system": [],
    "python": [
      "Pillow>=10.0.0"
    ],
    "skills": []
  },
  "keywords": [
    "image-editor",
    "image",
    "creative"
  ]
}
```

✅ **Quality Checklist:**

- \[ \] Skill name is unique and descriptive
- \[ \] Description explains WHAT it does and WHEN to use it
- \[ \] Instructions include concrete examples
- \[ \] All dependencies are listed in `skill.json`
- \[ \] Code is well-documented and tested
- \[ \] README.md explains the skill for humans



**Step 4: Submit Pull Request**

Open a pull request with:

- **Title**: `Add [skill-name]: [brief description]`
- **Description**: What the skill does and why it's useful
- **Testing**: How you validated the skill works

#### 🔍 Review Process

2. **Manual Review** - Team reviews functionality and quality
3. **Community Feedback** - Other contributors may suggest improvements
4. **Merge & Publish** - Approved skills are published to the registry

**Timeline**: Most PRs are reviewed within 2-3 business days.

---

## 📖 Skill Development Resources

### 🛠️ Development Tools

| Tool | Purpose | Link |
| --- | --- | --- |
| **Skilzy CLI** | Create, validate, package skills | [GitHub](https://github.com/skilzy-ai/skilzy-cli/releases/) |
| **Python SDK** | Programmatic skill management | [GitHub](https://github.com/skilzy-ai/skilzy-python) or `pip install skilzy` |
| **Web Registry** | Browse, install, publish skills | [skilzy.ai](https://skilzy.ai/) |


---

## 🤝 Community

### 💬 Get Help

- **Email**: hi@skilzy.ai
- **GitHub Issues**: Report bugs or request features
- **Documentation**: [skilzy.ai/docs](skilzy.ai/docs)

---

## 📄 License

This repository is licensed under the **MIT License**. Individual skills may have their own licenses - please check each skill's LICENSE file.

By contributing to this repository, you agree that your contributions will be licensed under the same license as the project.

---

## 🚀 Ready to Build the Future of AI?

**Start contributing today:**

1. 🍴 **Fork this repository**
2. 🛠️ **Install the CLI tool** or **Python SDK**
3. 🎯 **Create your first skill** with `skilzy init`
4. 📤 **Submit a pull request** or **publish directly** to skilzy.ai

**Your skills will power AI agents across every platform and help build the future of specialized AI assistants!**

---

*Made with ❤️ by the Skilzy community*
