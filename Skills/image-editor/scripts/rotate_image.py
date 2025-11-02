#!/usr/bin/env python3
"""
Image rotation and flipping script.
"""
from PIL import Image
import argparse
import sys

def rotate_image(input_path, output_path, angle=0, flip_horizontal=False, flip_vertical=False, expand=True):
    """
    Rotate and/or flip an image.

    Args:
        input_path: Path to input image
        output_path: Path to save transformed image
        angle: Rotation angle in degrees (positive = counter-clockwise)
        flip_horizontal: Whether to flip horizontally
        flip_vertical: Whether to flip vertically
        expand: Whether to expand image to fit rotated content
    """
    try:
        img = Image.open(input_path)

        # Apply flips first
        if flip_horizontal:
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            print("✓ Flipped horizontally")

        if flip_vertical:
            img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            print("✓ Flipped vertically")

        # Apply rotation
        if angle != 0:
            img = img.rotate(angle, expand=expand, resample=Image.Resampling.BICUBIC)
            print(f"✓ Rotated {angle}°")

        img.save(output_path)
        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error transforming image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rotate and flip an image")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--angle", type=float, default=0, help="Rotation angle in degrees")
    parser.add_argument("--flip-h", action="store_true", help="Flip horizontally")
    parser.add_argument("--flip-v", action="store_true", help="Flip vertically")
    parser.add_argument("--no-expand", action="store_true", help="Don't expand canvas to fit rotation")

    args = parser.parse_args()

    success = rotate_image(
        args.input,
        args.output,
        angle=args.angle,
        flip_horizontal=args.flip_h,
        flip_vertical=args.flip_v,
        expand=not args.no_expand
    )

    sys.exit(0 if success else 1)
