import pandas as pd

def load_test_cases(file_path):
    test_cases = {}
    
    try:
        # Load the entire Excel file
        xls = pd.ExcelFile(file_path)
        
        # Iterate over each sheet
        for sheet_name in xls.sheet_names:
            # Read each sheet into a DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            # Convert the DataFrame to a list of dictionaries
            test_cases[sheet_name] = df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return test_cases

if _name_ == "_main_":
    file_path = 'test_cases.xlsx'
    test_cases = load_test_cases(file_path)
    
    # Print the test cases for each sheet
    for sheet, cases in test_cases.items():
        print(f"Sheet: {sheet}")
        for case in cases:
            print(case)
        print("\n")
