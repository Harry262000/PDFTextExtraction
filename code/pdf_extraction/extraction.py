import pdfplumber
import pandas as pd
import camelot
import tabula
import cv2

def extracted_text_from_pdf(pdf_path):
    
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        # Ensure 'pages' is accessed correctly
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_tables_from_pdf_camelot(pdf_path, flavor='stream'):
    tables = camelot.read_pdf(pdf_path, flavor=flavor)
    return [table.df for table in tables]

def extract_tables_from_pdf_tabula(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all')
    return tables

if __name__ == "__main__":
    pdf_path = "/home/harry/PDFTextExtraction/data /PwC_Audit_Report_2020.pdf"
    
    # Extract text
    text = extracted_text_from_pdf(pdf_path)
    print("Extracted Text:\n", text)
    
    # Extract tables using Camelot
    tables_camelot = extract_tables_from_pdf_camelot(pdf_path)
    for i, table in enumerate(tables_camelot):
        print(f"Table {i} from Camelot:\n", table)
    
    # Extract tables using Tabula
    tables_tabula = extract_tables_from_pdf_tabula(pdf_path)
    for i, table in enumerate(tables_tabula):
        print(f"Table {i} from Tabula:\n", table)

    