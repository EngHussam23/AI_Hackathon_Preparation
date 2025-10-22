"""
This module uses:
# sys for system-specific parameters and functions.
in this case: stderr
# PIL for image processing
"""
import sys
import os
import PIL
from PIL import Image
import pytesseract

def convert_print_size(size_bytes):
    print("converting...")
    if size_bytes < 1024:
        print(f"{size_bytes} Bytes")
    elif size_bytes < 1024**2:
        print(f"{size_bytes / 1024:.2f} KB")
    elif size_bytes < 1024**3:
        print(f"{size_bytes / (1024**2):.2f} MB")
    else:
        print(f"{size_bytes / (1024**3):.2f} GB")

def compare_format(jpeg_path, png_path):
    try:
        print("## Image 1\n\n")
        with Image.open(jpeg_path) as jpeg_img:
            # confirmation
            print(f"image opened: {jpeg_path}")
            # printing details
            convert_print_size(os.path.getsize(jpeg_path))
            print(f"size (width, height): {jpeg_img.size}")
            print(f"format: {jpeg_img.format}")
            print(f"mode: {jpeg_img.mode}")
            print(f"extracted text:\n\n{pytesseract.image_to_string(jpeg_img)}")
            print("\n\n## Image 2\n\n")
        with Image.open(png_path) as png_img:
            # confirmation
            print(f"image opened: {png_path}")
            # printing details
            convert_print_size(os.path.getsize(png_path))
            print(f"size (width, height): {png_img.size}")
            print(f"format: {png_img.format}")
            print(f"mode: {png_img.mode}")
            print(f"extracted text:\n\n{pytesseract.image_to_string(png_img)}")
    except FileNotFoundError:
        print("## Image not found", file=sys.stderr)
    except PIL.UnidentifiedImageError:
        print("## Pillow cannot recognize the image format, check your image file.", sys.stderr)
    except OSError:
        print("## Cannot read image, try checking the image permissions.", sys.stderr)
    except pytesseract.TesseractError as e:
        print(f"## OCR failed: {e}", file=sys.stderr)
    except Exception as e:
        print(f"## Unexpected OCR error: {e}", file=sys.stderr)

print("# OCR Day 2\n\n")
print("Comparing JPEG and PNG images in the terms of: size, properties, and OCR quality\n\n")
compare_format("image_1.jpeg", "image_2.png")
