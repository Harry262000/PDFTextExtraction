# PDF Text Extraction

## Description
This project extracts text from PDF files using OCR (Optical Character Recognition) with Tesseract and pdf2image.

## Directory Structure
```

PDFTextExtraction/
├── data/
│ ├── raw_pdfs/
│ ├── extracted_images/
│ ├── extracted_text/
├── logs/
├── scripts/
│ └── extract_text.py
├── README.md
└── requirements.txt

```

## Setup
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Harry262000/PDFTextExtraction.git
    cd PDFTextExtraction
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv pdf
    source pdf/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install system dependencies**:
    ```bash
    sudo apt update
    sudo apt install tesseract-ocr poppler-utils
    ```

## Usage
1. **Place your PDF files** in the `data/raw_pdfs` directory.
2. **Run the extraction script or Jupyter notebook**:
    ```bash
    cd scripts
    jupyter notebook extract_text.ipynb
    ```

3. The extracted text will be saved in the `data/extracted_text` directory, and the images will be saved in the `data/extracted_images` directory.

## Dependencies
- pdf2image
- pytesseract
- Pillow
- Jupyter
- Tesseract OCR
- Poppler-utils

## Notes
Ensure Tesseract OCR and Poppler-utils are installed on your system.
