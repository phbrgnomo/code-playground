# Experimentation with Python PDF files manipulation

Playing around with Python PDF handlers to see what is their outputs and their performance.

For detail about what each package can do, check the `features` folder.

## Packages tested:

### 1. PyPDF2:
   - A pure Python library for reading and extracting text from PDF files.
   - PyPDF2 GitHub: https://github.com/mstamy2/PyPDF2

   ```python
   import PyPDF2

    with open("example.pdf", "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()

   ```

### 2. PyMuPDF (MuPDF):
   - A lightweight PDF and XPS viewer with support for text extraction.
   - PyMuPDF GitHub: https://github.com/pymupdf/PyMuPDF

   ```python
   import fitz

    pdf_document = fitz.open("example.pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()   
   ```

### 3. Tabula-py:
   - A Python wrapper for Tabula, a Java library for extracting tables from PDFs.
   - Tabula-py GitHub: https://github.com/chezou/tabula-py

    ```python
    import tabula

    tables = tabula.read_pdf("example.pdf", pages="all")

    ```
### 4. Camelot-py:
   - A Python library for extracting tables from PDFs into pandas DataFrames.
   - Camelot-py GitHub: https://github.com/camelot-dev/camelot

   ```python
    import camelot

    tables = camelot.read_pdf("example.pdf", flavor="stream", pages="all")

   ```

### 5. pdfminer.six:
   - A PDF parser and text extraction tool.
   - pdfminer.six GitHub: https://github.com/pdfminersix/pdfminer.six

    ```python
    from pdfminer.high_level import extract_text

    text = extract_text(open("example.pdf", "rb"))

    ```

### 6. PDFplumber:
   - A wrapper for the PDFMiner library, providing a high-level interface for text extraction and table parsing.
   - PDFplumber GitHub: https://github.com/jsvine/pdfplumber

   ```python
    import pdfplumber

    with pdfplumber.open("example.pdf") as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
   ```

### 7. Slate:
   - A Python package for extracting text and tables from PDFs.
   - Slate GitHub: https://github.com/timClicks/slate

   ```python
    from slate import PDF

    with open("example.pdf", "rb") as file:
        pdf = PDF(file)
        text = pdf.text()

   ```
### 8. Slate (slate3k):
   - An alternative version of Slate, a Python package for extracting text and tables from PDFs.
   - Slate (slate3k) GitHub: https://github.com/TAMU-CPT/slate

    ```python
    from slate3k import PDF

    def extract_text_from_pdf(file_path):
        with open(file_path, "rb") as file:
            pdf = PDF(file)
            text = ""
            for page in pdf:
                text += page.get_text()
        return text

    ```


### 9. PDFQuery:
   - A PDF scraping library that extends PyPDF2 and lxml.
   - PDFQuery GitHub: https://github.com/jcushman/pdfquery

   ```python
    from pdfquery import PDFQuery

    def extract_text_from_pdfquery(file_path):
        pdf = PDFQuery(file_path)
        pdf.load()
        
        # Example: Extracting text from the first page
        text = pdf.extract([
            ('with_formatter', 'text'),
            ('text', 'LTPage[pageid="1"]'),
        ])
        
        return text

   ```

### 10. PyPDFium:
   - A Python library for extracting text, images, and metadata from PDF files.
   - PyPDFium GitHub: https://github.com/rouge8/pypdfium

   ```python
    from pypdfium import PdfDocument

    def extract_text_with_pypdfium(file_path):
        with open(file_path, 'rb') as file:
            pdf_doc = PdfDocument(file)
            text = ''
            for page_num in range(pdf_doc.get_page_count()):
                page = pdf_doc.get_page(page_num)
                text += page.get_text()
        return text

   ```