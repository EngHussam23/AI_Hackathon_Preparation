"""
Text extraction from PDF
"""
import sys
import os
import PyPDF2
from PyPDF2 import PdfReader
import pdf2image
from pdf2image import convert_from_path
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

def exctract
