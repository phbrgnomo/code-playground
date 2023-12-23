import re
import os
import PyPDF2


from . import pdfhandler


def select_reports():
    files = pdfhandler.select_pdfs()
    return files

def extract_data(pdf_path):
    """
    Extracts table data from a PDF file and returns the extracted data.

    Parameters:
    - pdf_path (str): The path to the PDF file.

    Returns:
    - dict: A dictionary containing the extracted data.
    """
    
    # Extract filename from the path
    file_name = os.path.basename(pdf_path)

    # Define a regex pattern for the filename standard
    pattern = r'(?P<company>[\w]+)-(?P<asset_type>[\w]+)-(?P<report_name>[\w]+)-(?P<year>\d{4})-(?P<month>\d{2})\.pdf'

    # Match the pattern against the filename
    match = re.match(pattern, file_name)

    if match:
        # Extract values from the matched groups
        groups = match.groupdict()
        year = groups['year']
        month = groups['month']
        asset_type = groups['asset_type']
        company = groups['company']
        report_name = groups['report_name']

        # Create the nested dictionary structure for the specific report
        report_data = {
            year: {
                month: {
                    asset_type: {
                        company: {
                            report_name: {
                                'allocation': {}
                            }
                        }
                    }
                }
            }
        }

        company_extract = {
            'XP': data_XP,
        }
        
        if company in company_extract:
            asset_data = company_extract[company](report_data, pdf_path)
            # Include the 'asset_data' in the 'allocation' section
            report_data[year][month][asset_type][company][report_name]['allocation'] = asset_data
            
        
        # Your code to extract allocation data from the PDF goes here
        # For demonstration purposes, let's assume asset data is provided as a dictionary
        # asset_data = {'asset_a': 0.1, 'asset_b': 0.3, 'asset_c': 0.1}

        # Update the 'allocation' dictionary with asset data
        # report_data[year][month][asset_type][company][report_name]['allocation'] = asset_data

        return report_data
    else:
        print(f"Filename '{file_name}' does not match the expected pattern.")
        return None

def data_XP(report_data, pdf_path):
    # Create a PDF reader object
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
    # Extract text from the first page (you might need to adjust the page number)
        page = pdf_reader.pages[0]
        report_content = page.extract_text()
    
    print("report_content", report_content)

    # Use regex to find the pattern XXXX11 or XXXX1 along with the entire line
    line_pattern = re.compile(r'(\d+(?:,\d{1,3})*(?:\.\d+)?)% .*?([A-Za-z]+[1-9]\d*(?:\d{2})?)\b.*?(?:\n|$)')

    # Find all matches in the report content
    matches = line_pattern.findall(report_content)
    
    # Print the matches
    print("Matches:")
    for match in matches:
        print(match)

    # Extract percentage and ticker from matches
    table_data = []
    for match in matches:
        # Print the match tuple
        print("Match Tuple:", match)

        # Assign the first element to percentage and the second element to ticker
        percentage, ticker = match

        # Append to the table_data list
        table_data.append({'Percentage': percentage, 'Ticker': ticker})


    # Print the extracted data
    print("table_data:", table_data)

    # Return the 'asset_data' as a dictionary
    return {entry['Ticker']: entry['Percentage'] for entry in table_data}

def convert_month_name_to_number(month_name):
    # Replace this with your logic to convert month names to numbers
    month_mapping = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}
    return month_mapping.get(month_name.lower(), 0)  # Default to 0 if the month name is not found


def merge_data(final_structure, extracted_data):
    """
    Merges extracted data into the final structure.

    Parameters:
    - final_structure (dict): The final structure to update.
    - extracted_data (dict): The extracted data from a single report.

    Returns:
    - dict: The updated final structure.
    """
    for year, year_data in extracted_data.items():
        if year not in final_structure:
            final_structure[year] = {}

        for month, month_data in year_data.items():
            if month not in final_structure[year]:
                final_structure[year][month] = {}

            for asset_type, asset_type_data in month_data.items():
                if asset_type not in final_structure[year][month]:
                    final_structure[year][month][asset_type] = {}

                for company, company_data in asset_type_data.items():
                    if company not in final_structure[year][month][asset_type]:
                        final_structure[year][month][asset_type][company] = {}

                    for report_name, report_data in company_data.items():
                        if report_name not in final_structure[year][month][asset_type][company]:
                            final_structure[year][month][asset_type][company][report_name] = {}

                        # Merge the 'allocation' data
                        final_structure[year][month][asset_type][company][report_name].update(report_data.get('allocation', {}))

    return final_structure
