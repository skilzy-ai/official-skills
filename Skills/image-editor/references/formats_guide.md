# Image Formats Guide

This guide provides information about supported image formats and best practices for the image-editor skill.

## Supported Formats

### Common Formats

#### JPEG / JPG
- **Use for:** Photographs, complex images with many colors
- **Compression:** Lossy
- **Transparency:** Not supported
- **Best quality setting:** 90-95 for high quality, 80-85 for web
- **Notes:** Does not support transparency; RGBA images will be converted to RGB with white background

#### PNG
- **Use for:** Graphics, logos, images requiring transparency
- **Compression:** Lossless
- **Transparency:** Supported (RGBA)
- **Notes:** Larger file sizes than JPEG, ideal for images with text or sharp edges

#### WebP
- **Use for:** Modern web applications
- **Compression:** Both lossy and lossless
- **Transparency:** Supported
- **Quality setting:** 80-90 recommended
- **Notes:** Better compression than JPEG/PNG, but less universal support

#### GIF
- **Use for:** Simple animations, very simple graphics
- **Compression:** Lossless (limited palette)
- **Transparency:** Supported (binary - on/off only)
- **Color limit:** 256 colors
- **Notes:** Not recommended for photographs

#### BMP
- **Use for:** Uncompressed image storage
- **Compression:** None (or minimal)
- **Transparency:** Limited support
- **Notes:** Very large file sizes, rarely used for web

#### TIFF
- **Use for:** High-quality archival, professional photography
- **Compression:** Multiple options (lossless/lossy)
- **Transparency:** Supported
- **Notes:** Large file sizes, excellent for archival but not for web

## Format Conversion Best Practices

### Converting TO JPEG
- Best for: Photographs, complex color images
- Always specify quality (recommended: 85-95)
- Transparent areas will be filled with white
- Use when file size is a concern and transparency isn't needed

### Converting TO PNG
- Best for: Graphics, logos, screenshots, images with transparency
- No quality parameter needed (lossless)
- Larger file sizes than JPEG
- Use when transparency or lossless quality is required

### Converting TO WebP
- Best for: Modern web applications
- Specify quality (recommended: 80-90)
- Supports both transparency and high compression
- Use for web delivery when browser support is adequate

## Quality Guidelines

### For Web Use
- JPEG: 80-85 (good balance of quality and size)
- WebP: 75-85 (better compression than JPEG)
- PNG: No quality setting (lossless)

### For Print/Archival
- JPEG: 90-95 (minimal compression artifacts)
- PNG: Always lossless
- TIFF: Lossless compression preferred

### For Screenshots/Graphics
- PNG: Preferred (lossless, supports transparency)
- WebP: Alternative for web (quality 90+)

## Image Processing Order

When applying multiple operations, follow this recommended order for best results:

1. **Crop** - Remove unwanted areas first
2. **Rotate/Flip** - Correct orientation
3. **Resize** - Scale to target dimensions
4. **Adjust** - Brightness, contrast, saturation, sharpness
5. **Effects** - Apply blur or filters
6. **Watermark** - Add text overlays last
7. **Convert Format** - Final step for delivery

## Common Pitfalls

### Transparency Loss
- Converting from PNG/WebP (with transparency) to JPEG will replace transparent areas with white
- Always check if transparency is needed before converting to JPEG

### Quality Degradation
- Repeatedly saving as JPEG degrades quality (lossy compression)
- For iterative editing, work with PNG and convert to JPEG as final step

### Color Mode Issues
- Some formats require specific color modes (e.g., JPEG requires RGB)
- The scripts automatically handle common conversions

### File Size Surprises
- PNG files of photographs can be very large
- Use JPEG or WebP for photos unless transparency is essential
- Quality settings dramatically affect file size

## Recommended Workflows

### Photo Editing Workflow
1. Open image (any format)
2. Apply adjustments (brightness, contrast, etc.)
3. Resize if needed
4. Save as JPEG (quality 85-90) or WebP (quality 80-85)

### Logo/Graphics Workflow
1. Open image (preferably PNG)
2. Apply operations (crop, resize, etc.)
3. Save as PNG to preserve quality and transparency

### Batch Processing Workflow
1. Standardize format (convert all to same format)
2. Apply consistent operations
3. Save with appropriate quality settings
