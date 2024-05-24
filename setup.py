from setuptools import setup, find_packages
import os

# Directory structure to create
directories = [
    'data',
    'data/raw_pdfs',
    'data/extracted_images',
    'data/extracted_text',
    'logs',
    'scripts'
]

def create_directories():
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    print("Directories created.")

# Run the directory creation function
create_directories()

# Define the setup
setup(
    name='PDFTextExtraction',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pdf2image',
        'pytesseract',
        'Pillow',
        'jupyter'
    ],
    entry_points={
        'console_scripts': [
            'create_directories=setup:create_directories',
        ],
    },
)

print("Setup complete.")
