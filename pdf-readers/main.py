from gui import dialogs
from pdfparsers import pypdf2parser, pymupdfparser

def main():
    file_type = "pdf"
    file_paths = dialogs.select_files(file_type)
    print(file_paths)
    
    # Text Extraction
    # --------------------
    for f in file_paths:
        print(f"File: {f}")
        # Extract text from the file using PyPDF2
        pypdf2parser.extract_full_text(f)
        # Extract text from the file using pymupdf    
        pymupdfparser.extract_full_text(f)
        
    # ---------------------
    
    # Metadata Extraction
    # ---------------------
    for f in file_paths:
        # Extract the metadata using PyPDF2
        meta = pypdf2parser.extract_metadata(f)
        # print(meta)
        # Extract the metadata using PyPDF2
        meta = pymupdfparser.extract_metadata(f)
        # print(meta)
        
    # ---------------------
        
    
    
if __name__ == "__main__":
    main()