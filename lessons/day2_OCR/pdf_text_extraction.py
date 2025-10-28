"""
Text extraction from PDF
"""
# import sys
import os
# import PyPDF2
from PyPDF2 import PdfReader, errors
# import pdf2image
from pdf2image import convert_from_path
# import PIL
from PIL import ImageEnhance
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

def extract_text_from_single_page(page_image, page_num):
    """
    Extract text from a single page image using OCR with enhancements
    
    Args:
        page_image: PIL Image object of the PDF page
        page_num: Page number (for display purposes)
    
    Returns: string with OCR-extracted text from this page
    """
    try:
        print(f"  → Running OCR on page {page_num}...")
        # Apply enhancements (grayscale, contrast, brightness)
        greyscaled_image = convert_to_greyscale(page_image)
        contrasted_image = adjust_contrast(greyscaled_image, 2)
        enhanced_image = adjust_brightness(contrasted_image, 2)
        enhanced_image.save(f"edited_images/brightened_image{page_num}.png")

        # Run pytesseract on enhanced image
        page_text = pytesseract.image_to_string(enhanced_image)
        return page_text.strip()

    except Exception as e:
        print(f"  ✗ OCR failed on page {page_num}: {e}")
        return ""


def extract_text_hybrid(pdf_path):
    """
    Hybrid extraction: For EACH page, extract both text layer AND run OCR
    This handles PDFs with mixed content (typed text + embedded images)
    
    Returns: string with all extracted text
    """
    try:
        # Open PDF for text extraction
        reader = PdfReader(pdf_path)
        # Convert PDF to images for OCR
        print("Converting PDF to images...")
        image_pages = convert_from_path(pdf_path, dpi=400)

        all_pages_text = []

        # Process each page individually
        for page_num, (page, page_image) in enumerate(zip(reader.pages, image_pages), start=1):
            print(f"\n📄 Processing Page {page_num}...")
            page_results = []

            # Step 1: Try text layer extraction
            text_layer = page.extract_text()
            if text_layer and len(text_layer.strip()) > 0:
                print(f"  ✓ Text layer found ({len(text_layer)} chars)")
                page_results.append(text_layer.strip())
            else:
                print("  ✗ No text layer")

            # Step 2: ALWAYS run OCR (to catch embedded images/scans)
            ocr_text = extract_text_from_single_page(page_image, page_num)
            if ocr_text and len(ocr_text) > 0:
                print("  ✓ OCR found content ({len(ocr_text)} chars)")
                page_results.append(ocr_text)
            else:
                print("  ✗ No OCR content")

            # Combine results for this page
            if page_results:
                combined_page_text = "\n".join(page_results)
                all_pages_text.append(f"--- Page {page_num} ---\n{combined_page_text}")
            else:
                all_pages_text.append(f"--- Page {page_num} ---\n[No content extracted]")

        # Join all pages
        return '\n\n'.join(all_pages_text)

    except FileNotFoundError:
        print(f"Error: the PDF ({pdf_path}) is not found!")
        return ""
    except errors.EmptyFileError:
        print(f"Cannot read ({pdf_path})")
        return ""
    except errors.PdfReadError:
        print(f"Cannot read ({pdf_path})")
        return ""
    except Exception as e:
        print(f"Error: ({e})")
        return ""


def pdf_extraction(pdf_path):
    """
    Intelligent hybrid PDF text extraction:
    - For EACH page: extracts both text layer AND runs OCR
    - Handles mixed content (typed text + embedded images)
    - Combines results from both methods per page
    
    Returns: tuple (text, method_used)
    """
    print("Starting hybrid extraction (text layer + OCR per page)...\n")
    extracted_text = extract_text_hybrid(pdf_path)

    if extracted_text and len(extracted_text.strip()) > 0:
        print("\n✅ Extraction complete!")
        return (extracted_text, "hybrid")
    else:
        print("\n⚠️ No content extracted from PDF")
        return ("", "none")


# Test the function
if __name__ == "__main__":
    # Replace with your test PDF path
    PDF_FILE = "42Asia-Team-Meeting.pdf"
    text, method = pdf_extraction(PDF_FILE)
    print(f"\n{'='*50}")
    print(f"Extraction method: {method}")
    print(f"{'='*50}")
    print(text)  # Print first 500 characters
