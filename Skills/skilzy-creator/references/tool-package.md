# Tool Reference: package_skill.py

## Purpose

Bundle a validated skill into a distributable `.skill` archive suitable for upload to the Skilzy registry or direct distribution to users. The packager ensures only valid skills are distributed by running automatic pre-validation.

## Command Syntax

```bash
python scripts/package_skill.py <path/to/skill-directory> [options]
```

### Arguments

- `<path/to/skill-directory>` - Path to the skill folder to package (default: current directory)
  - Can be absolute or relative path
  - Must contain a valid skill.json file

### Options

- `-o, --output-dir <directory>` - Directory to save the archive (default: `dist/`)
  - Creates the directory if it doesn't exist
  - Archive will be saved here

- `--output-name <filename>` - Custom filename for the archive
  - Default: ` {name}-{version}.skill`
  - Must include `.skill` extension

## Packaging Process

The packaging script follows a strict sequence:

### Step 1: Pre-Validation

**Automatically runs `validate_skill.py` on the target directory**

**If validation fails:**
- ❌ Packaging stops immediately
- All validation errors displayed to user
- Exit code 1 (failure)
- No package created

**If validation passes:**
- ✅ Proceeds to Step 2
- Confirmation message shown

**Why this matters:**
- Prevents distributing broken skills
- Catches errors before publication
- Ensures registry compliance

### Step 2: Archive Creation

1. **Read skill.json** to extract metadata:
   - `name` - Used in filename
   - `version` - Used in filename

2. **Create ZIP archive** using compression:
   - Format: ZIP
   - Compression: `zipfile.ZIP_DEFLATED`
   - Extension: `.skill`

3. **Name the archive**:
   - Default: `{name}-{version}.skill`
   - Example: `pdf-processor-1.0.0.skill`
   - Custom: Use `--output-name` flag

4. **Save to output directory**:
   - Default location: `dist/`
   - Creates directory if needed
   - Custom location: Use `-o` flag

### Step 3: File Inclusion

**Recursively walks the skill directory and includes:**

- ✅ skill.json
- ✅ SKILL.md
- ✅ README.md
- ✅ LICENSE (or LICENSE.txt, etc.)
- ✅ All files in `scripts/`
- ✅ All files in `references/`
- ✅ All files in `assets/`
- ✅ Any other files in the skill directory

**Preserves:**
- Complete directory structure
- File permissions (when supported)
- Relative paths

**Excludes:**
- The output directory itself (prevents recursion)
- Hidden files starting with `.` (e.g., `.git/`, `.DS_Store`)
- `__pycache__/` directories
- `.pyc` files

## Archive Structure

The packaged archive contains the skill directory as a **single root folder**:

```
pdf-processor-1.0.0.skill (ZIP archive)
└── pdf-processor/              # Root folder inside zip
    ├── skill.json
    ├── SKILL.md
    ├── README.md
    ├── LICENSE
    ├── assets/
    │   └── icon.svg
    ├── scripts/
    │   └── process_pdf.py
    └── references/
        └── api_docs.md
```

**Why this structure:**
- Maintains skill directory name
- Prevents file conflicts when extracting
- Standard expected by Skilzy registry
- Compatible with `skilzy install` command

## When to Use This Tool

Use `package_skill.py` when:

- ✅ Skill is **complete and tested**
- ✅ Validation passes successfully
- ✅ Ready to distribute or publish
- ✅ Creating a release version
- ✅ Preparing for registry upload

**Do not use when:**
- ❌ Skill has validation errors
- ❌ Still in development/testing
- ❌ Missing required files
- ❌ Incomplete documentation

## Example Workflows

### Workflow 1: Standard Packaging

**Package to default location (dist/):**

```bash
python scripts/package_skill.py web-scraper/
```

**Output:**
```
Validating skill...
✅ Validation passed

Packaging skill...
✅ Package created: dist/web-scraper-0.1.0.skill
```

**Result:**
- File created: `dist/web-scraper-0.1.0.skill`
- Ready for publication

### Workflow 2: Custom Output Directory

**Package to custom location:**

```bash
python scripts/package_skill.py data-analyzer/ -o ~/releases/
```

**Output:**
```
Validating skill...
✅ Validation passed

Packaging skill...
✅ Package created: ~/releases/data-analyzer-1.2.3.skill
```

**Result:**
- File created: `~/releases/data-analyzer-1.2.3.skill`
- Custom location used

### Workflow 3: Custom Filename

**Package with custom name:**

```bash
python scripts/package_skill.py pdf-tool/ --output-name pdf-tool-beta.skill
```

**Output:**
```
Validating skill...
✅ Validation passed

Packaging skill...
✅ Package created: dist/pdf-tool-beta.skill
```

**Result:**
- File created: `dist/pdf-tool-beta.skill`
- Custom name used (version not included)

### Workflow 4: Combined Options

**Custom directory and name:**

```bash
python scripts/package_skill.py my-skill/ -o releases/ --output-name my-skill-staging.skill
```

**Result:**
- File created: `releases/my-skill-staging.skill`

## Handling Validation Failures

**Example scenario:**

```bash
$ python scripts/package_skill.py broken-skill/

Validating skill...

--- Validation Summary ---
Schema validation failed:
  - description: 'Bad' is too short
  - version: '1.0' does not match SemVer pattern

❌ Validation failed. Cannot package skill.
```

**What to do:**
1. Review validation errors
2. Load `references/troubleshooting.md` if needed:
   ```bash
   cat references/troubleshooting.md
   ```
3. Fix each error in skill files
4. Run packaging again (validation runs automatically)

## Output Information

**Successful packaging shows:**
- Validation status
- Package location
- File size
- Success confirmation

**Example:**
```
Validating skill...
✅ Validation passed

Packaging skill 'web-scraper' version '1.0.0'...
Including 15 files...

✅ Package created: dist/web-scraper-1.0.0.skill
📦 Size: 45.2 KB
```

## After Packaging

Once the skill is packaged, you can:

### 1. Publish to Skilzy Registry

```bash
# Install Skilzy SDK
pip install skilzy

# Authenticate
skilzy login <your-api-key>

# Publish
skilzy publish dist/my-skill-1.0.0.skill
```

### 2. Distribute Directly

Share the `.skill` file with users who can install it:

```bash
skilzy install path/to/my-skill-1.0.0.skill
```

### 3. Upload via Web

Visit https://skilzy.ai/publish and upload the `.skill` file manually.

### 4. Version Control

Commit the package to releases or version control:

```bash
git tag v1.0.0
git push origin v1.0.0
# Upload dist/my-skill-1.0.0.skill to GitHub releases
```

## Common Issues

### Error: "Validation failed"

**Cause:** Skill has validation errors

**Fix:**
1. Review validation output
2. Fix each error
3. Re-run packaging command

### Error: "skill.json not found"

**Cause:** Provided path doesn't contain skill.json

**Fix:** Ensure you're pointing to the correct skill directory

### Error: "Permission denied writing to output directory"

**Cause:** No write permissions for output directory

**Fix:** Either:
- Choose a different output directory
- Fix permissions: `chmod +w dist/`

### Warning: "Output file already exists, overwriting"

**Cause:** A package with the same name already exists

**Behavior:** Automatically overwrites existing file

**To avoid:** Delete old packages or use custom names

## Best Practices

1. **Always validate first** - Though automatic, run manual validation during development
2. **Use semantic versioning** - Increment version before packaging new releases
3. **Organize output** - Use consistent output directories (e.g., `dist/`, `releases/`)
4. **Archive old versions** - Keep previous `.skill` files for rollback purposes
5. **Test installation** - Install your own package locally before publishing
6. **Document releases** - Maintain CHANGELOG.md with version notes

## Testing Your Package

**Before publishing, test locally:**

```bash
# Package the skill
python scripts/package_skill.py my-skill/ -o dist/

# Install locally for testing
skilzy install dist/my-skill-1.0.0.skill --local

# Test functionality
# (Use the skill in an AI agent environment)

# If issues found:
# 1. Fix the skill
# 2. Increment version
# 3. Re-package
# 4. Test again
```

## Package Verification

**Verify package contents:**

```bash
# List contents
unzip -l dist/my-skill-1.0.0.skill

# Extract to inspect
unzip dist/my-skill-1.0.0.skill -d temp-extract/
ls -R temp-extract/
```

**Check for:**
- ✅ All expected files present
- ✅ Correct directory structure
- ✅ No unwanted files (e.g., `.pyc`, `.DS_Store`)
- ✅ skill.json is valid