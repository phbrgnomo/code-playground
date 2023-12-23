import fitz
from utils import filehandler
import time

def extract_full_text(filepath):
    """
    Extracts the text from a PDF file.

    Parameters
    ----------
    filepath : str
        The path to the PDF file.

    Returns
    -------
    text : str
        The extracted text.
    """
    # Record the starting time
    start_time = time.time()

    # Open the PDF file
    pdf_document = fitz.open(filepath)

    # Initialize an empty string to store extracted text
    text = ''
    
    # Iterate through each page and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()

    filehandler.save_to_txt(text, "pymupdf-full-text")
    
    # Record the ending time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Time to extract text using pymupdf: %s" % elapsed_time)
    
    return text

def extract_metadata(filepath):
    """
    Extracts the metadata from a PDF file.

    Parameters
    ----------
    filepath : str
        The path to the PDF file.

    Returns
    -------
    md : dict
    """
    # Record the starting time
    start_time = time.time()

    # Open the PDF file
    pdf_document = fitz.open(filepath)
    
    try:
        # Extract Metadata from the PDF file
        md = pdf_document.metadata

        # Save metadata to a TXT file
        filehandler.save_to_txt(str(md), "pymupdf-metadata")
    
    finally:
        # Close PFF file
        pdf_document.close()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time to extract metadata using pymupdf: %s" % elapsed_time)
    
    return md

