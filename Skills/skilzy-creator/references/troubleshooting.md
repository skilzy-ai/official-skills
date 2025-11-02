# Troubleshooting Guide

This guide covers common errors encountered during skill creation, validation, and packaging, along with solutions.

## Validation Errors

### Schema Validation Errors

#### Error: "description is too short"

**Full error:**
```
Schema validation failed:
  - description: 'Short desc' is too short
```

**Cause:** The description field is under 20 characters.

**Example of problematic skill.json:**
```json
{
  "description": "Processes PDFs"
}
```

**Fix:** Expand the description to at least 20 characters and include WHEN to use the skill:

```json
{
  "description": "Extracts text and metadata from PDF documents. Use when users upload PDFs for analysis or content extraction."
}
```

**Best practice:** Aim for 80-150 characters with specific triggers.

---

#### Error: "description is too long"

**Full error:**
```
Schema validation failed:
  - description: '...' is too long
```

**Cause:** The description field exceeds 250 characters.

**Fix:** Condense the description to under 250 characters. Move details to README.md:

**Before (too long):**
```json
{
  "description": "This comprehensive skill provides advanced data processing capabilities including CSV parsing, Excel file analysis, statistical computations, data visualization with multiple chart types, export to various formats, and integration with external data sources. Use when users need any kind of data analysis or processing."
}
```

**After (concise):**
```json
{
  "description": "Processes CSV and Excel files with statistical analysis and visualization. Use when users upload tabular data requesting insights, trends, or charts."
}
```

---

#### Error: "name does not match pattern"

**Full error:**
```
Schema validation failed:
  - name: 'MySkill' does not match '^[a-z0-9]+(-[a-z0-9]+)*$'
```

**Cause:** Skill name contains uppercase letters, underscores, spaces, or special characters.

**Invalid examples:**
- `"MySkill"` (camelCase)
- `"my_skill"` (underscore)
- `"my skill"` (space)
- `"my-skill!"` (special character)

**Fix:** Use only lowercase letters, numbers, and hyphens:

```json
{
  "name": "my-skill"
}
```

**If the directory name doesn't match:**
```bash
# Rename the directory to match
mv MySkill my-skill
```

---

#### Error: "version does not match SemVer pattern"

**Full error:**
```
Schema validation failed:
  - version: '1.0' does not match SemVer pattern
```

**Cause:** Version is not in MAJOR.MINOR.PATCH format.

**Invalid examples:**
- `"1.0"` (missing PATCH)
- `"v1.0.0"` (has 'v' prefix)
- `"1.0.0.0"` (too many parts)
- `"1.0.0-Beta"` (uppercase in pre-release)

**Fix:** Use proper Semantic Versioning:

```json
{
  "version": "1.0.0"
}
```

**Valid variations:**
```json
{"version": "1.0.0"}         // Standard release
{"version": "0.1.0"}         // Initial development
{"version": "1.0.0-alpha"}   // Pre-release
{"version": "2.0.0-beta.1"}  // Numbered pre-release
```

---

#### Error: "keywords contain invalid characters"

**Full error:**
```
Schema validation failed:
  - keywords[0]: 'PDF' does not match '^[a-z0-9-]+$'
  - keywords[1]: 'Data Analysis' does not match '^[a-z0-9-]+$'
```

**Cause:** Keywords contain uppercase letters or spaces.

**Invalid:**
```json
{
  "keywords": ["PDF", "Data Analysis", "ML_Tools"]
}
```

**Fix:** Use lowercase and hyphens only:

```json
{
  "keywords": ["pdf", "data-analysis", "ml-tools"]
}
```

---

#### Error: "required field missing"

**Full error:**
```
Schema validation failed:
  - 'author' is a required property
```

**Cause:** One of the required fields is not present in skill.json.

**Required fields:**
- `name`
- `version`
- `description`
- `author`
- `license`
- `entrypoint`

**Fix:** Add the missing field:

```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "description": "Does something useful. Use when needed.",
  "author": "John Doe",
  "license": "MIT",
  "entrypoint": "README.md"
}
```

---

#### Error: "runtime.type must be 'python'"

**Full error:**
```
Schema validation failed:
  - runtime.type: 'nodejs' is not one of ['python']
```

**Cause:** Currently only Python runtime is supported.

**Invalid:**
```json
{
  "runtime": {
    "type": "nodejs"
  }
}
```

**Fix:** Use Python:

```json
{
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  }
}
```

---

### Filesystem Validation Errors

#### Error: "Directory name does not match skill name"

**Full error:**
```
Filesystem checks failed:
  - Directory name 'pdf_editor' does not match skill name 'pdf-editor'
```

**Cause:** The parent folder name doesn't match the `name` field in skill.json.

**Example:**
- Directory: `pdf_editor/`
- skill.json: `"name": "pdf-editor"`

**Fix:** Rename the directory to match:

```bash
mv pdf_editor pdf-editor
```

**Or update skill.json** (not recommended, use hyphens not underscores):

```json
{
  "name": "pdf-editor"
}
```

---

#### Error: "Entrypoint file does not exist"

**Full error:**
```
Filesystem checks failed:
  - File 'README.md' declared in 'entrypoint' field does not exist
```

**Cause:** skill.json references an entrypoint file that isn't in the directory.

**Example:**
- skill.json: `"entrypoint": "README.md"`
- Missing file: `README.md`

**Fix:** Create the missing file:

```bash
touch README.md
# Then edit README.md to add content
```

**Or change entrypoint** to an existing file:

```json
{
  "entrypoint": "DOCUMENTATION.md"
}
```

---

#### Error: "Icon file does not exist"

**Full error:**
```
Filesystem checks failed:
  - File 'assets/icon.svg' declared in 'icon' field does not exist
```

**Cause:** skill.json references an icon file that isn't present.

**Example:**
- skill.json: `"icon": "assets/logo.png"`
- Missing file: `assets/logo.png`

**Fix:** Add the icon file:

```bash
mkdir -p assets
cp ~/my-icon.png assets/logo.png
```

**Or remove the icon field** temporarily:

```json
{
  "_comment": "Remove icon field until icon is ready"
}
```

---

#### Error: "License file does not exist"

**Full error:**
```
Filesystem checks failed:
  - File 'LICENSE' declared in 'licenseFile' field does not exist
```

**Cause:** skill.json references a license file that isn't present.

**Fix:** Create the license file:

```bash
# For MIT license
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy...
EOF
```

**Or update licenseFile** to point to existing file:

```json
{
  "licenseFile": "LICENSE.txt"
}
```

---

#### Error: "skill.json is not valid JSON"

**Full error:**
```
Error: Failed to parse skill.json
Expecting property name enclosed in double quotes: line 5 column 3
```

**Cause:** JSON syntax error in skill.json.

**Common JSON errors:**

**Missing comma:**
```json
{
  "name": "my-skill"
  "version": "1.0.0"  ← Missing comma after previous line
}
```

**Trailing comma:**
```json
{
  "name": "my-skill",
  "version": "1.0.0",  ← Trailing comma not allowed
}
```

**Unquoted keys:**
```json
{
  name: "my-skill"  ← Keys must be quoted: "name"
}
```

**Single quotes:**
```json
{
  'name': 'my-skill'  ← Must use double quotes
}
```

**Fix:** Use a JSON validator to find the error:

```bash
# Validate JSON
python -m json.tool skill.json

# Or use jq
jq . skill.json
```

**Or use an online validator:** https://jsonlint.com

---

## Initialization Errors

#### Error: "Skill directory already exists"

**Full error:**
```
Error: Directory 'my-skill' already exists
```

**Cause:** A directory with that name already exists in the output location.

**Fix options:**

**1. Choose a different name:**
```bash
python scripts/init_skill.py my-skill-v2 --non-interactive
```

**2. Delete the existing directory:**
```bash
rm -rf my-skill/
python scripts/init_skill.py my-skill --non-interactive
```

**3. Use a different output path:**
```bash
python scripts/init_skill.py my-skill --path ~/projects/skills/
```

---

#### Error: "Invalid skill name format"

**Full error:**
```
Error: Skill name 'My_Skill' is invalid. Use lowercase letters, numbers, and hyphens only.
```

**Cause:** Provided skill name contains invalid characters.

**Invalid names:**
- `My_Skill` (uppercase, underscore)
- `my skill` (space)
- `my.skill` (period)

**Fix:** Use valid format:

```bash
python scripts/init_skill.py my-skill --non-interactive
```

---

## Conversion Errors

#### Error: "Archive does not contain SKILL.md"

**Full error:**
```
Error: No SKILL.md file found in archive
```

**Cause:** The Claude skill ZIP file doesn't contain SKILL.md.

**Fix:** Verify archive contents:

```bash
# List contents
unzip -l claude-skill.zip

# Ensure SKILL.md exists
```

**If SKILL.md is in a subdirectory**, extract and repack:

```bash
unzip claude-skill.zip
# Move SKILL.md to root if needed
zip -r claude-skill-fixed.zip .
```

---

#### Error: "SKILL.md missing required 'name' field"

**Full error:**
```
Error: SKILL.md frontmatter missing required field: name
```

**Cause:** SKILL.md YAML frontmatter doesn't have a `name` field.

**Invalid SKILL.md:**
```markdown
---
description: Processes PDFs
---
```

**Fix:** Add name field to frontmatter:

```markdown
---
name: pdf-processor
description: Processes PDFs
---
```

---

#### Error: "Invalid YAML frontmatter in SKILL.md"

**Full error:**
```
Error: Failed to parse YAML frontmatter
mapping values are not allowed here
```

**Cause:** YAML syntax error in SKILL.md frontmatter.

**Common YAML errors:**

**Missing space after colon:**
```yaml
---
name:pdf-processor  ← Need space after colon
---
```

**Wrong delimiter:**
```yaml
***  ← Should be ---
name: pdf-processor
***  ← Should be ---
```

**Fix:** Correct YAML syntax:

```yaml
---
name: pdf-processor
description: Processes PDF files
license: MIT
---
```

---

## Packaging Errors

#### Error: "Validation failed. Cannot package skill."

**Full error:**
```
Validating skill...

--- Validation Summary ---
Schema validation failed:
  - description is too short

❌ Validation failed. Cannot package skill.
```

**Cause:** Skill has validation errors. Packaging is blocked until validation passes.

**Fix:**
1. Review validation errors
2. Fix each error in skill files
3. Re-run packaging (validation runs automatically)

```bash
# Fix errors in skill.json
nano my-skill/skill.json

# Try packaging again (includes validation)
python scripts/package_skill.py my-skill/
```

---

#### Error: "skill.json not found"

**Full error:**
```
Error: No skill.json found in directory 'my-skill'
```

**Cause:** Provided path doesn't contain skill.json.

**Fix:** Ensure you're in the correct directory:

```bash
# Check directory contents
ls my-skill/

# Should contain skill.json
# If not, you may be pointing to wrong directory
```

---

#### Error: "Permission denied writing to output directory"

**Full error:**
```
Error: Permission denied: dist/
```

**Cause:** No write permissions for the output directory.

**Fix options:**

**1. Choose a different output directory:**
```bash
python scripts/package_skill.py my-skill/ -o ~/packages/
```

**2. Fix permissions:**
```bash
chmod +w dist/
```

**3. Use sudo** (not recommended):
```bash
sudo python scripts/package_skill.py my-skill/
```

---

## Runtime Errors (When Using Skills)

#### Error: "Module not found"

**Error in execution:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Cause:** Skill dependencies are not installed.

**Fix:** Install dependencies listed in skill.json:

```bash
# Check skill.json for dependencies
cat skill.json | grep -A 5 dependencies

# Install Python dependencies
pip install pandas numpy matplotlib

# Or install from requirements.txt if provided
pip install -r requirements.txt
```

**Prevention:** Always list dependencies in skill.json:

```json
{
  "dependencies": {
    "python": ["pandas>=2.0", "numpy>=1.20"]
  }
}
```

---

#### Error: "Command not found"

**Error in execution:**
```
bash: ffmpeg: command not found
```

**Cause:** System dependency is not installed.

**Fix:** Install the system tool:

**On Mac:**
```bash
brew install ffmpeg
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**On Windows:**
```bash
choco install ffmpeg
```

**Prevention:** List system dependencies in skill.json:

```json
{
  "dependencies": {
    "system": ["ffmpeg", "imagemagick"]
  }
}
```

---

## General Troubleshooting Tips

### Debugging Checklist

When encountering errors, work through this checklist:

1. **Read the complete error message** - Often contains the exact issue
2. **Check file paths** - Ensure files exist where referenced
3. **Validate JSON syntax** - Use `python -m json.tool skill.json`
4. **Check naming consistency** - Directory name must match skill name
5. **Verify required fields** - All required fields in skill.json present
6. **Review file permissions** - Ensure read/write access
7. **Check dependencies** - All listed dependencies installed
8. **Use validation** - Run `validate_skill.py` to catch issues early

### Getting Help

If you're still stuck:

1. **Run validation** with verbose output (if available)
2. **Check the schema reference** - `references/schema-reference.md`
3. **Review examples** - `references/examples.md`
4. **Check Skilzy documentation** - https://docs.skilzy.ai
5. **Ask the community** - https://community.skilzy.ai

### Common Workflow Issues

**Issue:** Made changes but validation still fails

**Solution:** Ensure you saved the files after editing

```bash
# Re-validate after saving
python scripts/validate_skill.py my-skill/
```

---

**Issue:** Package created but skill doesn't work

**Solution:** Test the skill before publishing

```bash
# Install locally
skilzy install dist/my-skill-1.0.0.skill --local

# Test functionality
# Make fixes if needed
# Increment version
# Re-package and test again
```

---

**Issue:** Validation passes but packaging fails

**Solution:** Check file permissions and disk space

```bash
# Check disk space
df -h

# Check output directory permissions
ls -la dist/

# Try different output location
python scripts/package_skill.py my-skill/ -o ~/temp/
```