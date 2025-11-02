#!/usr/bin/env python3
"""
Image adjustment script for brightness, contrast, saturation, and sharpness.
"""
from PIL import Image, ImageEnhance
import argparse
import sys

def adjust_image(input_path, output_path, brightness=1.0, contrast=1.0, saturation=1.0, sharpness=1.0):
    """
    Adjust image properties.

    Args:
        input_path: Path to input image
        output_path: Path to save adjusted image
        brightness: Brightness factor (1.0 = original, <1.0 = darker, >1.0 = brighter)
        contrast: Contrast factor (1.0 = original, <1.0 = less contrast, >1.0 = more contrast)
        saturation: Saturation factor (1.0 = original, 0.0 = grayscale, >1.0 = more saturated)
        sharpness: Sharpness factor (1.0 = original, <1.0 = blurred, >1.0 = sharper)
    """
    try:
        img = Image.open(input_path)

        adjustments_made = []

        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)
            adjustments_made.append(f"brightness: {brightness}")

        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)
            adjustments_made.append(f"contrast: {contrast}")

        if saturation != 1.0:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(saturation)
            adjustments_made.append(f"saturation: {saturation}")

        if sharpness != 1.0:
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpness)
            adjustments_made.append(f"sharpness: {sharpness}")

        img.save(output_path)

        if adjustments_made:
            print(f"✓ Applied adjustments: {', '.join(adjustments_made)}")
        else:
            print("ℹ No adjustments applied (all values at default 1.0)")

        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error adjusting image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adjust image brightness, contrast, saturation, and sharpness")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--brightness", type=float, default=1.0, help="Brightness factor (default: 1.0)")
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast factor (default: 1.0)")
    parser.add_argument("--saturation", type=float, default=1.0, help="Saturation factor (default: 1.0)")
    parser.add_argument("--sharpness", type=float, default=1.0, help="Sharpness factor (default: 1.0)")

    args = parser.parse_args()

    success = adjust_image(
        args.input,
        args.output,
        brightness=args.brightness,
        contrast=args.contrast,
        saturation=args.saturation,
        sharpness=args.sharpness
    )

    sys.exit(0 if success else 1)
