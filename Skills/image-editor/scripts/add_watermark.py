#!/usr/bin/env python3
"""
Image watermark script.
"""
from PIL import Image, ImageDraw, ImageFont
import argparse
import sys

def add_watermark(input_path, output_path, text, position='bottom-right', opacity=128, font_size=36):
    """
    Add a text watermark to an image.

    Args:
        input_path: Path to input image
        output_path: Path to save watermarked image
        text: Watermark text
        position: Position (top-left, top-right, bottom-left, bottom-right, center)
        opacity: Text opacity (0-255, where 255 is fully opaque)
        font_size: Font size for watermark text
    """
    try:
        img = Image.open(input_path)

        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Create transparent overlay
        txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        # Try to use a default font, fall back to basic if unavailable
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # Get text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate position
        margin = 20
        if position == 'top-left':
            x, y = margin, margin
        elif position == 'top-right':
            x, y = img.width - text_width - margin, margin
        elif position == 'bottom-left':
            x, y = margin, img.height - text_height - margin
        elif position == 'bottom-right':
            x, y = img.width - text_width - margin, img.height - text_height - margin
        elif position == 'center':
            x, y = (img.width - text_width) // 2, (img.height - text_height) // 2
        else:
            raise ValueError(f"Unknown position: {position}")

        # Draw text with opacity
        draw.text((x, y), text, fill=(255, 255, 255, opacity), font=font)

        # Composite the watermark onto the image
        watermarked = Image.alpha_composite(img, txt_layer)

        # Convert back to original mode if needed
        if watermarked.mode != img.mode:
            watermarked = watermarked.convert('RGB')

        watermarked.save(output_path)

        print(f"✓ Added watermark: '{text}'")
        print(f"✓ Position: {position}, Opacity: {opacity}")
        print(f"✓ Saved to: {output_path}")
        return True

    except Exception as e:
        print(f"✗ Error adding watermark: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a text watermark to an image")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("text", help="Watermark text")
    parser.add_argument("--position", default="bottom-right",
                       help="Position: top-left, top-right, bottom-left, bottom-right, center")
    parser.add_argument("--opacity", type=int, default=128, help="Text opacity (0-255)")
    parser.add_argument("--font-size", type=int, default=36, help="Font size")

    args = parser.parse_args()

    success = add_watermark(
        args.input,
        args.output,
        args.text,
        position=args.position,
        opacity=args.opacity,
        font_size=args.font_size
    )

    sys.exit(0 if success else 1)
