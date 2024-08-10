# Interactive PDF Analysis and Extraction Tool

## Overview
This project provides an interactive web-based tool that allows users to upload PDF documents, automatically extract tables and textual content, and interactively chat with the extracted data for insights. It aims to simplify the process of analyzing complex PDF documents such as bills or annual reports by offering automated extraction, visualization, and interactive querying.

## Live Interaction
To see the tool in action, check out the live demo on [Streamlit](https://financial-documents-extraction-harry262000.streamlit.app/). This demo showcases the interactive features of the app, including PDF uploading, data extraction, and chat functionality.

## Features
- **PDF Upload**: Easily upload PDF files through a web interface.
- **Automated Extraction**: Extract text and tables from the uploaded PDFs.
- **Data Processing**: Organize extracted data in a structured format for efficient querying.
- **Interactive Chat**: Engage with the extracted data using a natural language chatbot.
- **Data Visualization**: Generate and interact with visual representations of the extracted tables.
- **User Feedback**: Provide feedback to improve the tool's accuracy and usability.

## Installation

### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### Libraries and Tools
- `streamlit`
- `PyMuPDF`
- `pdfplumber`
- `tabula-py`
- `pandas`
- `matplotlib`
- `seaborn`
- `plotly`
- `transformers` (Hugging Face)

### Steps to Install
1. Clone the repository:
   ```bash
   https://github.com/Harry262000/PDFTextExtraction.git

2. Create a virtual enviorment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
3. install the required libraries:
   ```bash
   pip install -r requirements.txt

### Usage

1. Run the streamlit app:
   ```bash
   streamlit run app.py

2. Upload a PDF:
   - `Use the web interface to upload a PDF document.`
3. View Extracted Data:
   - `Extracted text and tables will be displayed on the interface.`
4. Interactive Chat:
   - `Engage with the chatbot to query the extracted data.`
5. Visualize Data:
   - `View visual representations of the extracted tables.`

### File Structure

- `app.py`: Main application file for Streamlit.
- `pdf_extraction.py`: Handles PDF extraction logic.
- `chatbot.py`: Manages chatbot interactions.
- `visualization.py`: Contains code for data visualization.
- `requirements.txt`: Lists required libraries and dependencies.

### Example Queries

- "Show me the revenue for Q1."
- "What are the expenses listed in the table on page 3?"
- "Summarize the main points from the financial report."

### Issues and Suggestions

- If you encounter any issues or have suggestions for improvements, please raise an issue in the `GitHub Issues section` of this repository.
