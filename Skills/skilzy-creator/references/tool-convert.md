# Tool Reference: convert_skill.py

## Purpose

Migrate a skill from the Claude format (YAML frontmatter only in SKILL.md) to the modern Skilzy format (skill.json + SKILL.md + README.md) while maintaining full backwards compatibility with Claude systems.

## Command Syntax

```bash
python scripts/convert_skill.py <path/to/claude-skill.zip>
```

### Arguments

- `<path/to/claude-skill.zip>` - Path to the Claude skill archive (required)
  - Can be `.zip` or `.skill` file
  - Must contain a SKILL.md with YAML frontmatter

## Conversion Process

The conversion script performs these operations in order:

### Step 1: Extract and Analyze

1. **Unzip the archive** to a temporary directory
2. **Locate SKILL.md** in the extracted files
3. **Parse YAML frontmatter** to extract:
   - `name` (required)
   - `description` (required)
   - `license` (optional, defaults to "MIT")
   - Any other frontmatter fields
4. **Validate frontmatter** - Fails if `name` or `description` missing

### Step 2: Generate Skilzy Structure

1. **Create output directory** named after the skill (from frontmatter `name`)
2. **Copy all original files** unchanged (preserves complete Claude skill)
3. **Preserve SKILL.md completely intact** (including frontmatter for backwards compatibility)
4. **Generate new skill.json** from frontmatter metadata
5. **Create new README.md** with placeholder content

### Step 3: Handle License Files

1. **Search for existing license files**: `LICENSE`, `LICENSE.txt`, `LICENSE.md`
2. **If found**: Reference the existing file in skill.json `licenseFile` field
3. **If not found**: Create a placeholder `LICENSE` file with MIT license

### Step 4: Finalize Manifest

1. **Set defaults**:
   - `version`: "1.0.0" (first converted version)
   - `entrypoint`: "README.md" (for registry display)
   - `runtime.type`: "python"
   - `runtime.version`: ">=3.9"
2. **Preserve from frontmatter**:
   - `name`
   - `description`
   - `license` (or default to "MIT")
3. **Leave empty for manual completion**:
   - `keywords: []`
   - `dependencies: {}`
   - `author`: "Unknown"

## What Gets Preserved vs Created

### Preserved from Claude Skill (Unchanged)

- ✅ **SKILL.md** - Completely unchanged, including YAML frontmatter
- ✅ **All bundled files** - scripts/, references/, assets/, everything
- ✅ **Directory structure** - Original organization maintained
- ✅ **Existing LICENSE** - If present, referenced in skill.json

### Created by Conversion

- ➕ **skill.json** - New manifest generated from frontmatter
- ➕ **README.md** - New human documentation with TODO placeholders
- ➕ **LICENSE** - Created if not present in original

## Backwards Compatibility

The converted skill **works in both systems**:

**In Claude:**
- SKILL.md frontmatter provides metadata
- Claude reads frontmatter as before
- All bundled resources accessible
- No changes to agent behavior

**In Skilzy:**
- skill.json provides rich metadata
- README.md displays on registry
- Enhanced discovery via keywords
- Full Skilzy features available

## Handling Edge Cases

### Missing or Incomplete Frontmatter

**If `name` is missing:**
- ❌ Conversion fails with error
- Error message: "SKILL.md missing required 'name' field in frontmatter"

**If `description` is missing:**
- ❌ Conversion fails with error
- Error message: "SKILL.md missing required 'description' field in frontmatter"

**If `license` is missing:**
- ✅ Defaults to "MIT"
- Warning message: "No license specified, defaulting to MIT"

**If `author` is missing:**
- ✅ Defaults to "Unknown"
- Set in skill.json as `"author": "Unknown"`

### Multiple Files Named LICENSE

If the Claude skill contains:
- `LICENSE`
- `LICENSE.txt`
- `LICENSE.md`

**Behavior:**
- Uses the first one found (in order: LICENSE, LICENSE.txt, LICENSE.md)
- Sets `licenseFile` field to point to that file
- All files are preserved in the output

### No License File Present

**Behavior:**
- Creates a new `LICENSE` file with MIT license template
- Sets `licenseFile: "LICENSE"` in skill.json
- Populates with copyright year and author from frontmatter

## Example Conversions

### Example 1: Simple Claude Skill

**Input (claude-pdf-skill.zip):**
```
pdf-editor/
├── SKILL.md
└── scripts/
    └── rotate_pdf.py
```

**SKILL.md frontmatter:**
```yaml
---
name: pdf-editor
description: Rotate and manipulate PDF files
license: MIT
---
```

**Output (after conversion):**
```
pdf-editor/
├── skill.json          # NEW
├── SKILL.md            # UNCHANGED
├── README.md           # NEW
├── LICENSE             # NEW
└── scripts/
    └── rotate_pdf.py   # UNCHANGED
```

**Generated skill.json:**
```json
{
  "name": "pdf-editor",
  "version": "1.0.0",
  "description": "Rotate and manipulate PDF files",
  "author": "Unknown",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {},
  "keywords": []
}
```

### Example 2: Claude Skill with Existing License

**Input:**
```
bigquery-skill/
├── SKILL.md
├── LICENSE.txt
└── references/
    └── schema.md
```

**SKILL.md frontmatter:**
```yaml
---
name: bigquery-helper
description: Query BigQuery databases with schema assistance
license: Apache-2.0
author: Data Team
---
```

**Output:**
```
bigquery-helper/
├── skill.json          # NEW
├── SKILL.md            # UNCHANGED
├── README.md           # NEW
├── LICENSE.txt         # UNCHANGED (preserved)
└── references/
    └── schema.md       # UNCHANGED
```

**Generated skill.json:**
```json
{
  "name": "bigquery-helper",
  "version": "1.0.0",
  "description": "Query BigQuery databases with schema assistance",
  "author": "Data Team",
  "license": "Apache-2.0",
  "licenseFile": "LICENSE.txt",
  "entrypoint": "README.md",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {},
  "keywords": []
}
```

## After Conversion

Once the skill is converted, complete these steps:

1. **Update skill.json metadata**:
   - Add `keywords` for discoverability
   - Add `dependencies` (Python packages, system tools)
   - Update `author` if set to "Unknown"
   - Add `repository` URL if applicable

2. **Update README.md**:
   - Replace [TODO] placeholders
   - Add features, installation, usage examples
   - Write for human registry users

3. **Optionally update SKILL.md**:
   - Keep frontmatter for Claude compatibility
   - Can add more detailed instructions
   - Reference new resources if added

4. **Validate the converted skill**:
   ```bash
   python scripts/validate_skill.py bigquery-helper/
   ```

5. **Package for Skilzy registry**:
   ```bash
   python scripts/package_skill.py bigquery-helper/ -o dist/
   ```

## Common Issues

### Error: "Archive does not contain SKILL.md"

**Cause:** The zip file doesn't have a SKILL.md file

**Fix:** Ensure the Claude skill archive contains SKILL.md at the root or in a subdirectory

### Error: "SKILL.md missing required 'name' field"

**Cause:** SKILL.md frontmatter doesn't have a `name` field

**Fix:** Add `name:` to the YAML frontmatter before conversion

### Error: "Invalid YAML frontmatter in SKILL.md"

**Cause:** YAML syntax error in frontmatter

**Fix:** Check frontmatter for:
- Proper YAML syntax
- Matching opening/closing `---` delimiters
- Correct indentation

### Warning: "No license specified, defaulting to MIT"

**Cause:** SKILL.md frontmatter doesn't specify a license

**Fix:** Either:
- Add `license: MIT` to frontmatter before conversion
- Accept the default and update skill.json after conversion

## Best Practices

1. **Backup original** - Keep the Claude .zip file before converting
2. **Review output** - Check that all files were preserved correctly
3. **Complete metadata** - Update skill.json immediately after conversion
4. **Validate** - Run validation to catch any issues
5. **Test in both systems** - Ensure it works in Claude and Skilzy
6. **Update README** - Don't leave placeholder content