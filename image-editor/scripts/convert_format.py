#!/usr/bin/env python3
"""
Image format conversion script.
"""
from PIL import Image
import argparse
import sys
import os

def convert_format(input_path, output_path, quality=95):
    """
    Convert image to a different format.

    Args:
        input_path: Path to input image
        output_path: Path to save converted image
        quality: Quality for JPEG/WebP (1-100, higher = better quality)
    """
    try:
        img = Image.open(input_path)

        # Get input and output formats
        input_format = img.format or os.path.splitext(input_path)[1][1:].upper()
        output_format = os.path.splitext(output_path)[1][1:].upper()

        # Handle RGBA to RGB conversion for JPEG
        if output_format == 'JPG':
            output_format = 'JPEG'

        if img.mode == 'RGBA' and output_format in ['JPEG', 'JPG']:
            # Create white background for transparent images
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            img = rgb_img

        # Save with appropriate options
        save_kwargs = {}
        if output_format in ['JPEG', 'JPG', 'WEBP']:
            save_kwargs['quality'] = quality

        img.save(output_path, format=output_format, **save_kwargs)

        print(f"✓ Converted from {input_format} to {output_format}")
        if 'quality' in save_kwargs:
            print(f"✓ Quality: {quality}")
        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error converting image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image format")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path (format determined by extension)")
    parser.add_argument("--quality", type=int, default=95, help="Quality for JPEG/WebP (1-100)")

    args = parser.parse_args()

    success = convert_format(args.input, args.output, quality=args.quality)

    sys.exit(0 if success else 1)
