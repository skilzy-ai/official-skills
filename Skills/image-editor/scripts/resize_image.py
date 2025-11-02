#!/usr/bin/env python3
"""
Image resizing script with multiple scaling options.
"""
from PIL import Image
import argparse
import sys

def resize_image(input_path, output_path, width=None, height=None, scale=None, maintain_aspect=True):
    """
    Resize an image with various options.

    Args:
        input_path: Path to input image
        output_path: Path to save resized image
        width: Target width in pixels
        height: Target height in pixels
        scale: Scale factor (e.g., 0.5 for 50%, 2.0 for 200%)
        maintain_aspect: Whether to maintain aspect ratio
    """
    try:
        img = Image.open(input_path)
        original_width, original_height = img.size

        if scale:
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
        elif width and height:
            new_width = width
            new_height = height
        elif width:
            new_width = width
            new_height = int(original_height * (width / original_width)) if maintain_aspect else original_height
        elif height:
            new_height = height
            new_width = int(original_width * (height / original_height)) if maintain_aspect else original_width
        else:
            raise ValueError("Must specify width, height, or scale")

        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(output_path)

        print(f"✓ Image resized from {original_width}x{original_height} to {new_width}x{new_height}")
        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error resizing image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--width", type=int, help="Target width in pixels")
    parser.add_argument("--height", type=int, help="Target height in pixels")
    parser.add_argument("--scale", type=float, help="Scale factor (e.g., 0.5 or 2.0)")
    parser.add_argument("--no-aspect", action="store_true", help="Don't maintain aspect ratio")

    args = parser.parse_args()

    success = resize_image(
        args.input,
        args.output,
        width=args.width,
        height=args.height,
        scale=args.scale,
        maintain_aspect=not args.no_aspect
    )

    sys.exit(0 if success else 1)
