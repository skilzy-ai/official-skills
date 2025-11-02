#!/usr/bin/env python3
"""
Image cropping script.
"""
from PIL import Image
import argparse
import sys

def crop_image(input_path, output_path, left, top, right, bottom):
    """
    Crop an image to specified coordinates.

    Args:
        input_path: Path to input image
        output_path: Path to save cropped image
        left: Left coordinate (x1)
        top: Top coordinate (y1)
        right: Right coordinate (x2)
        bottom: Bottom coordinate (y2)
    """
    try:
        img = Image.open(input_path)
        width, height = img.size

        # Validate coordinates
        if left < 0 or top < 0 or right > width or bottom > height:
            print(f"Warning: Coordinates may be out of bounds. Image size: {width}x{height}")

        if left >= right or top >= bottom:
            raise ValueError("Invalid crop coordinates: left must be < right and top must be < bottom")

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)

        crop_width = right - left
        crop_height = bottom - top
        print(f"✓ Image cropped from {width}x{height} to {crop_width}x{crop_height}")
        print(f"✓ Coordinates: ({left}, {top}) to ({right}, {bottom})")
        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error cropping image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop an image")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("left", type=int, help="Left coordinate (x1)")
    parser.add_argument("top", type=int, help="Top coordinate (y1)")
    parser.add_argument("right", type=int, help="Right coordinate (x2)")
    parser.add_argument("bottom", type=int, help="Bottom coordinate (y2)")

    args = parser.parse_args()

    success = crop_image(args.input, args.output, args.left, args.top, args.right, args.bottom)

    sys.exit(0 if success else 1)
