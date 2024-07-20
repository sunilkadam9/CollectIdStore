import pandas as pd


class Excel:
    # File path to your Excel file
    @staticmethod
    def create_test_sheet(file_path, test_sheet_name, test_case_data):
        #file_path = 'output/your_excel_file.xlsx'
        test_case = []
        #test_case.append(test_case_data)
        test_case = test_case_data

        print(test_case)
        # Read the Excel file
        excel_data = pd.read_excel(file_path, sheet_name=None)  # sheet_name=None reads all sheets

        # Print the sheet names
        print(excel_data.keys())

        data11=test_case_data
        # Data to append (example data)
        #data to append =test_case_data
        #data_to_append={'Column1': [test_case[0]], 'Column2': [data11[1]}
        data_to_append = {'Column1': [1, 2, 3], 'Column2': [2, 4,6 ]}

        df = pd.DataFrame(test_case,
                          columns=['Column1', 'Column2'])
        new_data = pd.DataFrame(data_to_append)
        new_data = df


        # Name of the sheet to which you want to append data
        target_sheet = test_sheet_name

        # Append the data
        if target_sheet in excel_data:
            # Concatenate existing data with new data
            updated_data = pd.concat([excel_data[target_sheet], new_data], ignore_index=True)
        else:
            # If the target sheet does not exist, use the new data as the initial data
            updated_data = new_data

        # Update the dictionary with the new data
        excel_data[target_sheet] = updated_data

        # Write the updated data back to the Excel file
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            for sheet_name, data in excel_data.items():
                data.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Test Case appended to {target_sheet} and Excel file updated.")


Excel.create_test_sheet('output/your_excel_file.xlsx', 'Sheet2', [[30, 39], [20, 29]])
