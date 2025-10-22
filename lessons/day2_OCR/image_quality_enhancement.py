"""
This module uses:
# sys for system-specific parameters and functions.
in this case: stderr
# PIL for image processing
"""
import sys
import os
import PIL
from PIL import Image, ImageEnhance
import pytesseract

def convert_to_greyscale(image):
    """
    Converting the passed image to greyscale
    """
    return image.convert('L')

def adjust_contrast(image, factor):
    """
    Adjusting the contrast for the passed image to greyscale
    """
    return ImageEnhance.Contrast(image).enhance(factor)

def adjust_brightness(image, factor):
    """
    Adjusting the brightness for the passed image to greyscale
    """
    return ImageEnhance.Brightness(image).enhance(factor)

def enhance_quality(image_path):
    """
    This function is responsible for enhancing the image
    for OCR purposes; the recognition may not be accurate
    if the image was not clear enough...
    """
    try:
        with Image.open(image_path) as img:
            print("Image opened!")
            print(f"Original text extracted:\n{pytesseract.image_to_string(img)}")
            file_name = os.path.basename(image_path)
            name, ext = os.path.splitext(file_name)
            # resize
            resized_image = img.resize((600, 200))
            resized_image.save(f"edited_images/resized_{name}{ext}")
            # Brightness
            print("Adjusting image brightness...")
            brightened_image = adjust_brightness(resized_image, 1.25)
            brightened_image.save(f"edited_images/brightened_{name}{ext}")
            print(f"Text extracted:\n{pytesseract.image_to_string(brightened_image)}")
            # Contrast
            print("Adjusting image contrast...")
            contrasted_image = adjust_contrast(brightened_image, 1.5)
            contrasted_image.save(f"edited_images/contrasted_{name}{ext}")
            print(f"Text extracted:\n{pytesseract.image_to_string(contrasted_image)}")
            # Greyscale
            print("converting to greyscale...")
            greyscaled_image = convert_to_greyscale(contrasted_image)
            greyscaled_image.save(f"edited_images/greyscaled_{name}{ext}")
            print(f"Text extracted:\n{pytesseract.image_to_string(greyscaled_image)}")
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

enhance_quality("assets/image_2.png")
