from utils import process_reports
import json

def main():
    
    data = {}
    
    reports = process_reports.select_reports()
        
    print(reports)
    
    for r in reports:
        extracted_data = process_reports.extract_data(r)
        
        if extracted_data:
            process_reports.merge_data(data, extracted_data)
    
    print("Final Data:")
    print(json.dumps(data, indent=4))
    # print(json.dumps(data['2023']['12']['FIIs'], indent=4))
        

if __name__ == '__main__':
    main()