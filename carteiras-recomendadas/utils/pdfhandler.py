import PyPDF2
from tkinter import Tk, filedialog

def process_multiple_pdfs(pdf_paths):
    """
    Processes multiple PDF files by extracting table data from each.

    Parameters:
    - pdf_paths (list): A list of paths to PDF files.

    Returns:
    - None
    """
    for pdf_path in pdf_paths:
        extract_table_data(pdf_path)

def select_pdfs():
    """
    Opens a file dialog to allow the user to select multiple PDF files.

    Returns:
    - list: A list of selected PDF file paths.
    """
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    return file_paths
