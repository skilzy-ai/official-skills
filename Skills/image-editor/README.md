# Image Editor Skill

## Overview

A comprehensive image editing skill that provides reliable, deterministic image manipulation capabilities through a collection of Python scripts. This skill enables AI agents to perform common image editing tasks without rewriting code repeatedly.

## Description

The **image-editor** skill is designed for AI agents to handle a wide range of image processing operations requested by users. It provides ready-to-use scripts for transformations, adjustments, effects, and format conversions - all optimized for reliability and repeatability.

### ✨ Key Features

**Transformations:**
- 📏 **Resize** - Scale images by dimensions or percentage while maintaining aspect ratio
- 🔄 **Rotate & Flip** - Rotate images to any angle and flip horizontally or vertically
- ✂️ **Crop** - Extract specific regions using pixel coordinates

**Adjustments:**
- ☀️ **Brightness** - Make images lighter or darker
- 🎨 **Contrast** - Adjust the difference between light and dark areas
- 🌈 **Saturation** - Control color vibrancy (from grayscale to highly saturated)
-  🔍 **Sharpness** - Sharpen or soften image details

**Effects:**
- 🌫️ **Blur** - Apply Gaussian blur with customizable radius
- 🎭 **Filters** - Apply artistic filters (contour, emboss, edge enhance, sharpen, smooth, and more)

**Overlays & Conversion:**
- 💧 **Watermarks** - Add text watermarks with customizable position, opacity, and font size
- 🔁 **Format Conversion** - Convert between JPEG, PNG, WebP, GIF, BMP, and TIFF with quality control

## When to Use This Skill

Use this skill when users request:

- Image resizing or scaling
- Rotation or flipping operations
- Cropping or cutting out portions
- Brightness, contrast, or color adjustments
- Blur effects or artistic filters
- Adding text watermarks or copyright notices
- Converting between image formats

**This skill does NOT handle:**
- Background removal or cutout operations
- Object detection or recognition
- AI-based image generation or enhancement
- OCR or text extraction from images

## Installation

```bash
# Using Skilzy Python SDK
skilzy install skilzy-ai/image-editor

```

## Quick Start Examples

### Resize an image to 800px wide
```bash
python scripts/resize_image.py photo.jpg resized.jpg --width 800
```

### Rotate 90 degrees and flip horizontally
```bash
python scripts/rotate_image.py photo.jpg rotated.jpg --angle 90 --flip-h
```

### Increase brightness and saturation
```bash
python scripts/adjust_image.py photo.jpg adjusted.jpg --brightness 1.3 --saturation 1.2
```

### Add a watermark
```bash
python scripts/add_watermark.py photo.jpg watermarked.jpg "© 2025 MyCompany" --position bottom-right
```

### Convert PNG to JPEG
```bash
python scripts/convert_format.py image.png image.jpg --quality 90
```

## Technical Details

**Runtime:** Python 3.9+  
**Dependencies:** Pillow (PIL)  10.0.0+  
**Scripts:** 7 specialized Python scripts for different operations  
**References:** Comprehensive image format guide included

All scripts include:
- Robust error handling
- Informative output messages
- Parameter validation
- Support for various image formats

## Advanced Usage

For complex workflows involving multiple operations, the skill supports chaining operations in the recommended order:

1. Crop (remove unwanted areas)
2. Rotate/Flip (correct orientation)
3. Resize (scale to target dimensions)
4. Adjust (brightness, contrast, saturation, sharpness)
5. Effects (blur, filters)
6. Watermark (add overlays)
7. Convert Format (final delivery format)

## License

MIT License - See LICENSE file for details

## Author

skilzy-ai

## Support

For issues, questions, or contributions, please visit the Skilzy registry or contact the author.