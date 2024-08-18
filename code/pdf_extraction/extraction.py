#from models import TableTransformer
import pdfplumber
import camelot
import tabula
import fitz
from PIL import Image
import pytesseract

def open_pdf(pdf_path, password=None):
    try:
        doc = fitz.open(pdf_path)
        if doc.needs_pass:
            if password is not None:
                if doc.authenticate(password):
                    return doc
                else:
                    return None
            else:
                return None
        return doc
    except Exception as e:
        return None

def is_scanned_page(page):
    text = page.extract_text()
    return text is None or text.strip() == ""

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text with pdfplumber: {e}")
    return text

def extract_tables_from_pdf_camelot(pdf_path, flavor='stream'):
    tables = []
    try:
        tables = camelot.read_pdf(pdf_path, flavor=flavor, pages='all')
        tables = [table.df for table in tables]
    except Exception as e:
        print(f"Error extracting tables with Camelot: {e}")
    return tables

def extract_tables_from_pdf_tabula(pdf_path):
    tables = []
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    except Exception as e:
        print(f"Error extracting tables with Tabula: {e}")
    return tables

def extract_text_from_scanned_pdf_page(page):
    text = ""
    try:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        text = pytesseract.image_to_string(img)
    except Exception as e:
        print(f"Error extracting text from scanned PDF page: {e}")
    return text

def extract_text_from_scanned_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += extract_text_from_scanned_pdf_page(page)
    except Exception as e:
        print(f"Error extracting text from scanned PDF: {e}")
    return text
