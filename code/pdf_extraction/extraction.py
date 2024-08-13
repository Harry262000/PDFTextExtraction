import pdfplumber
import camelot
import tabula
import fitz
from PIL import Image
import pytesseract
import pandas as pd

def is_scanned_page(page):
    """Check if a PDF page is scanned by looking for extractable text."""
    text = page.extract_text()  # Use extract_text for pdfplumber
    return len(text.strip()) == 0

def is_scanned(pdf_path):
    """Check if the PDF pages are scanned or text-based."""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        text = pytesseract.image_to_string(img)
        if text.strip():
            return False
    return True

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text with pdfplumber: {e}")
    return text

def extract_tables_from_pdf_camelot(pdf_path, flavor='stream'):
    """Extract tables from a PDF using Camelot."""
    tables = []
    try:
        tables = camelot.read_pdf(pdf_path, flavor=flavor, pages='all')  # Added pages='all'
        tables = [table.df for table in tables]
    except Exception as e:
        print(f"Error extracting tables with Camelot: {e}")
    return tables

def extract_tables_from_pdf_tabula(pdf_path):
    """Extract tables from a PDF using Tabula."""
    tables = []
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    except Exception as e:
        print(f"Error extracting tables with Tabula: {e}")
    return tables

def extract_text_from_scanned_pdf(pdf_path):
    """Extract text from a scanned PDF using OCR."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            text += pytesseract.image_to_string(img)
    except Exception as e:
        print(f"Error extracting text from scanned PDF: {e}")
    return text

def process_pdf(pdf_path):
    if is_scanned(pdf_path):
        print("The PDF is scanned. Extracting text using OCR...")
        text = extract_text_from_scanned_pdf(pdf_path)
    else:
        print("The PDF is text-based. Extracting text directly...")
        text = extract_text_from_pdf(pdf_path)

    print("Extracted Text:")
    print(text[:1000])  # Print only the first 1000 characters for brevity

    print("Extracting tables using Camelot...")
    tables_camelot = extract_tables_from_pdf_camelot(pdf_path)
    if not tables_camelot:
        print("Camelot failed. Trying Tabula...")
        tables_tabula = extract_tables_from_pdf_tabula(pdf_path)
        if not tables_tabula:
            print("Both Camelot and Tabula failed to extract tables.")
        else:
            print("Tables extracted using Tabula:")
            for i, table in enumerate(tables_tabula):
                print(f"Table {i}:\n", table)
    else:
        print("Tables extracted using Camelot:")
        for i, table in enumerate(tables_camelot):
            print(f"Table {i}:\n", table)