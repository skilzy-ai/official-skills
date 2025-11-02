

# Image Editor

This skill provides comprehensive image editing capabilities through a collection of Python scripts designed for deterministic, repeatable image manipulation tasks.

## Purpose

The image-editor skill enables reliable image processing operations without rewriting the same code repeatedly. It handles common image editing tasks that users request, from basic transformations (resize, rotate, crop) to advanced adjustments (brightness, contrast, color) and format conversions.

## When to Use This Skill

Use this skill when users request any of the following image operations:

- **Resizing** - "Make this image 800x600", "Scale this down by 50%"
- **Rotation** - "Rotate this 90 degrees", "Flip this image horizontally"
- **Cropping** - "Crop this to remove the borders", "Cut out the center portion"
- **Adjustments** - "Make this brighter", "Increase the contrast", "Make it more vibrant"
- **Effects** - "Blur this image", "Apply an edge detection filter", "Sharpen this photo"
- **Watermarks** - "Add my name to the bottom right", "Put a copyright notice on this"
- **Format conversion** - "Convert this PNG to JPEG", "Save this as WebP"

Do NOT use this skill for:
- Background removal or cutout operations
- Object detection or recognition tasks
- AI-based image generation or enhancement

## How to Use This Skill

### Available Scripts

All scripts are located in the `scripts/` directory and can be executed directly. Each script is self-contained with proper error handling and informative output.

#### 1. Resize Images (`scripts/resize_image.py`)

Resize images by dimensions or scale factor while optionally maintaining aspect ratio.

**Usage:**
```bash
# Resize to specific width (maintains aspect ratio)
python scripts/resize_image.py input.jpg output.jpg --width 800

# Resize to specific height (maintains aspect ratio)
python scripts/resize_image.py input.jpg output.jpg --height 600

# Resize to exact dimensions (may distort)
python scripts/resize_image.py input.jpg output.jpg --width 800 --height 600 --no-aspect

# Scale by factor (e.g., 50% or 200%)
python scripts/resize_image.py input.jpg output.jpg --scale 0.5
```

**Parameters:**
- `--width`: Target width in pixels
- `--height`: Target height in pixels
- `--scale`: Scale factor (e.g., 0.5 for 50%, 2.0 for 200%)
- `--no-aspect`: Don't maintain aspect ratio (allows distortion)

#### 2. Rotate and Flip (`scripts/rotate_image.py`)

Rotate images by any angle and flip horizontally or vertically.

**Usage:**
```bash
# Rotate 90 degrees counter-clockwise
python scripts/rotate_image.py input.jpg output.jpg --angle 90

# Flip horizontally
python scripts/rotate_image.py input.jpg output.jpg --flip-h

# Flip vertically
python scripts/rotate_image.py input.jpg output.jpg --flip-v

# Rotate and flip (operations can be combined)
python scripts/rotate_image.py input.jpg output.jpg --angle 45 --flip-h

# Rotate without expanding canvas
python scripts/rotate_image.py input.jpg output.jpg --angle 30 --no-expand
```

**Parameters:**
- `--angle`: Rotation angle in degrees (positive = counter-clockwise)
- `--flip-h`: Flip horizontally (mirror left-right)
- `--flip-v`: Flip vertically (mirror top-bottom)
- `--no-expand`: Don't expand canvas to fit rotated content

#### 3. Crop Images (`scripts/crop_image.py`)

Crop images to specific rectangular coordinates.

**Usage:**
```bash
# Crop to coordinates (left, top, right, bottom)
python scripts/crop_image.py input.jpg output.jpg 100 100 500 400
```

**Parameters:**
- `left`: Left x-coordinate
- `top`: Top y-coordinate
- `right`: Right x-coordinate
- `bottom`: Bottom y-coordinate

**Note:** To determine crop coordinates, first check the image dimensions. Coordinates are in pixels from the top-left corner (0,0).

#### 4. Adjust Images (`scripts/adjust_image.py`)

Adjust brightness, contrast, saturation (color), and sharpness.

**Usage:**
```bash
# Increase brightness
python scripts/adjust_image.py input.jpg output.jpg --brightness 1.3

# Increase contrast
python scripts/adjust_image.py input.jpg output.jpg --contrast 1.5

# Increase saturation (more vibrant colors)
python scripts/adjust_image.py input.jpg output.jpg --saturation 1.4

# Sharpen image
python scripts/adjust_image.py input.jpg output.jpg --sharpness 2.0

# Combine multiple adjustments
python scripts/adjust_image.py input.jpg output.jpg --brightness 1.2 --contrast 1.3 --saturation 1.1
```

**Parameters:**
- `--brightness`: Brightness factor (1.0 = original, <1.0 = darker, >1.0 = brighter)
- `--contrast`: Contrast factor (1.0 = original, <1.0 = less, >1.0 = more)
- `--saturation`: Color saturation (1.0 = original, 0.0 = grayscale, >1.0 = more vibrant)
- `--sharpness`: Sharpness (1.0 = original, <1.0 = blur, >1.0 = sharper)

#### 5. Apply Effects (`scripts/apply_effects.py`)

Apply blur and various artistic filters to images.

**Usage:**
```bash
# Apply Gaussian blur
python scripts/apply_effects.py input.jpg output.jpg --blur 5.0

# Apply edge enhancement filter
python scripts/apply_effects.py input.jpg output.jpg --filter EDGE_ENHANCE

# Combine blur and filter
python scripts/apply_effects.py input.jpg output.jpg --blur 2.0 --filter SHARPEN
```

**Parameters:**
- `--blur`: Gaussian blur radius (e.g., 2.0, 5.0, 10.0)
- `--filter`: Filter type (see available filters below)

**Available Filters:**
- `CONTOUR` - Outline contours
- `DETAIL` - Enhance detail
- `EDGE_ENHANCE` - Enhance edges
- `EDGE_ENHANCE_MORE` - Strongly enhance edges
- `EMBOSS` - Emboss effect
- `FIND_EDGES` - Find and highlight edges
- `SHARPEN` - Sharpen image
- `SMOOTH` - Smooth/blur slightly
- `SMOOTH_MORE` - Smooth/blur more

#### 6. Add Watermarks (`scripts/add_watermark.py`)

Add text watermarks to images with customizable position, opacity, and font size.

**Usage:**
```bash
# Add watermark to bottom-right (default)
python scripts/add_watermark.py input.jpg output.jpg "© 2025 My Company"

# Add watermark to top-left
python scripts/add_watermark.py input.jpg output.jpg "CONFIDENTIAL" --position top-left

# Adjust opacity and font size
python scripts/add_watermark.py input.jpg output.jpg "© Copyright" --opacity 100 --font-size 48
```

**Parameters:**
- `text`: Watermark text (required positional argument)
- `--position`: Position (top-left, top-right, bottom-left, bottom-right, center)
- `--opacity`: Text opacity 0-255 (default: 128)
- `--font-size`: Font size in pixels (default: 36)

#### 7. Convert Format (`scripts/convert_format.py`)

Convert images between different formats (JPEG, PNG, WebP, GIF, BMP, TIFF).

**Usage:**
```bash
# Convert PNG to JPEG
python scripts/convert_format.py input.png output.jpg --quality 90

# Convert JPEG to PNG (lossless)
python scripts/convert_format.py input.jpg output.png

# Convert to WebP with quality
python scripts/convert_format.py input.jpg output.webp --quality 85
```

**Parameters:**
- `--quality`: Quality for JPEG/WebP (1-100, default: 95)

**Important Notes:**
- Transparent images (PNG/WebP) converted to JPEG will have white backgrounds
- Format is determined by output file extension
- Refer to `references/formats_guide.md` for format selection best practices

### Reference Material

The `references/` directory contains detailed documentation:

- **`formats_guide.md`** - Comprehensive guide on image formats, quality settings, conversion best practices, and recommended workflows

Load this reference when users ask about:
- Which format to use for specific purposes
- Quality settings and their effects
- Format conversion best practices
- Transparency handling
- Processing order for multiple operations

## Workflow Recommendations

### For Single Operations
Execute the appropriate script directly with user-specified parameters.

### For Multiple Operations
Apply operations in this recommended order for best results:
1. Crop (remove unwanted areas first)
2. Rotate/Flip (correct orientation)
3. Resize (scale to target dimensions)
4. Adjust (brightness, contrast, saturation, sharpness)
5. Effects (blur, filters)
6. Watermark (add overlays last)
7. Convert Format (final step for delivery)

### Processing Chain Example
When a user requests multiple operations like "resize this to 800px wide, increase brightness, and convert to JPEG":

```bash
# Step 1: Resize
python scripts/resize_image.py input.png temp_resized.png --width 800

# Step 2: Adjust brightness
python scripts/adjust_image.py temp_resized.png temp_adjusted.png --brightness 1.3

# Step 3: Convert format
python scripts/convert_format.py temp_adjusted.png output.jpg --quality 90
```

## Script Execution Notes

- All scripts use the Pillow (PIL) library which must be available in the Python environment
- Scripts exit with code 0 on success, 1 on failure
- Error messages are printed to stderr
- Success messages and progress are printed to stdout
- Scripts validate input parameters and provide helpful error messages
- File paths can be relative or absolute

## Common User Request Patterns

When users make requests, translate them to appropriate script calls:

**"Make this image smaller"** → Use `resize_image.py` with `--scale` or `--width`/`--height`

**"Rotate this 180 degrees"** → Use `rotate_image.py --angle 180`

**"Make this brighter and more colorful"** → Use `adjust_image.py` with `--brightness` and `--saturation`

**"Add my name to this photo"** → Use `add_watermark.py` with appropriate text and position

**"Convert this to JPEG"** → Use `convert_format.py` with `.jpg` extension

**"Crop out the middle section"** → First determine image dimensions, then use `crop_image.py` with calculated coordinates

**"Apply a blur effect"** → Use `apply_effects.py --blur` with appropriate radius
