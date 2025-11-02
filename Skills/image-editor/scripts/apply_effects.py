#!/usr/bin/env python3
"""
Image effects script for blur and filters.
"""
from PIL import Image, ImageFilter
import argparse
import sys

def apply_effects(input_path, output_path, blur=None, filter_type=None):
    """
    Apply effects to an image.

    Args:
        input_path: Path to input image
        output_path: Path to save processed image
        blur: Blur radius (higher = more blur)
        filter_type: Type of filter to apply (CONTOUR, DETAIL, EDGE_ENHANCE, 
                     EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE)
    """
    try:
        img = Image.open(input_path)
        effects_applied = []

        if blur:
            img = img.filter(ImageFilter.GaussianBlur(radius=blur))
            effects_applied.append(f"Gaussian blur (radius: {blur})")

        if filter_type:
            filter_map = {
                'CONTOUR': ImageFilter.CONTOUR,
                'DETAIL': ImageFilter.DETAIL,
                'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
                'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
                'EMBOSS': ImageFilter.EMBOSS,
                'FIND_EDGES': ImageFilter.FIND_EDGES,
                'SHARPEN': ImageFilter.SHARPEN,
                'SMOOTH': ImageFilter.SMOOTH,
                'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            }

            if filter_type.upper() not in filter_map:
                raise ValueError(f"Unknown filter type: {filter_type}. Available: {', '.join(filter_map.keys())}")

            img = img.filter(filter_map[filter_type.upper()])
            effects_applied.append(f"{filter_type} filter")

        img.save(output_path)

        if effects_applied:
            print(f"✓ Applied effects: {', '.join(effects_applied)}")
        else:
            print("ℹ No effects applied")

        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error applying effects: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply effects to an image")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--blur", type=float, help="Blur radius (e.g., 2.0, 5.0)")
    parser.add_argument("--filter", dest="filter_type", 
                       help="Filter type: CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, "
                            "EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE")

    args = parser.parse_args()

    success = apply_effects(args.input, args.output, blur=args.blur, filter_type=args.filter_type)

    sys.exit(0 if success else 1)
