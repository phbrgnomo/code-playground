import PyPDF2
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
    pdf_reader = filehandler.open_file(filepath)
    
    # Create a PDFFileReader object to read the pdf content
    pdf_reader = PyPDF2.PdfReader(pdf_reader)
    
    # Initialize an empty string to store extracted text
    text = ''

    # Iterate through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()

    # Save the text to a TXT file
    filehandler.save_to_txt(text, "pypdf2-full-text")
    
    # Record the ending time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Time to extract text using pypdf2: %s" % elapsed_time)
    
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
        The extracted metadata.
    
    """
    # Record the starting time
    start_time = time.time()
    
    # Open the PDF file
    pdf_reader = filehandler.open_file(filepath)
    
    # Create a PDFFileReader object to read the pdf content
    pdf_reader = PyPDF2.PdfReader(pdf_reader)
    
    # Extract Metadata from the PDF file
    md = pdf_reader.metadata
    
    # Save the text to a TXT file
    filehandler.save_to_txt(str(md), "pypdf2-metadata")
    
    
    # Record the ending time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Time to extract metadata using pypdf2: %s" % elapsed_time)
    
    return md