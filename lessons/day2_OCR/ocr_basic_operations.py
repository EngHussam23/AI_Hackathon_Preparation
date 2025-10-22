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

# write a function to load an image
def load_image(image_path):
    """
    This function loads an image
    """
    try:
        with Image.open(image_path) as img:
            # confirm image opening
            print("Image opened!")
            # print some image details
            print(f"Image size: {img.size}")
            print(f"Image format: {img.format}")
            print(f"Image mode: {img.mode}")
            print(f"Text extracted:\n{pytesseract.image_to_string(img)}")
            # get the path of the image and save is in name & ext
            name, ext = os.path.splitext(image_path)
            print(f"Path: {name}{ext}\n")
            # rotate the image and save it
            rotated_img = img.rotate(45, expand=True)
            rotated_img.save(f"edited_images/new_{name}{ext}")
            # resize the image and save it
            resized_img = img.resize((400, 400))
            resized_img.save(f"edited_images/new_resized_{name}{ext}")
            print(f"New image size: {resized_img.size}")
            # confirm the image editing
            print(f"{name} is edited successfully! 🎉")
    except FileNotFoundError:
        print("Image not found", file=sys.stderr)
    except PIL.UnidentifiedImageError:
        print("Pillow cannot recognize the image format, check your image file.", sys.stderr)
    except OSError:
        print("Cannot read image, try checking the image permissions.", sys.stderr)
    except pytesseract.TesseractError as e:
        print(f"OCR failed: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected OCR error: {e}", file=sys.stderr)

load_image("image_1.jpeg")
