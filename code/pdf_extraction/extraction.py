import pdfplumber
import camelot
import tabula
import fitz
from PIL import Image
import pytesseract

def is_scanned(pdf_path):
    """Check if the PDF pages are scanned or text-based."""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img)
        if text.strip():
            return False
    return True

def extracted_text_from_pdf(pdf_path):
    """Extract text from a PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_tables_from_pdf_camelot(pdf_path, flavor='stream'):
    """Extract tables from a PDF using Camelot."""
    tables = camelot.read_pdf(pdf_path, flavor=flavor)
    return [table.df for table in tables]

def extract_tables_from_pdf_tabula(pdf_path):
    """Extract tables from a PDF using Tabula."""
    tables = tabula.read_pdf(pdf_path, pages='all')
    return tables
