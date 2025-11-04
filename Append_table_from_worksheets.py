import pandas as pd
from openpyxl import writer 

# Load the Excel workbook
input_file = r"C:\Users\btrent\vendorData.xlsx"
output_file = r"C:\Users\btrent\vendorComboQty.xlsx"

# Create an empty DataFrame to store combined results
combined_df = pd.DataFrame()

# Load the Excel file
xls = pd.ExcelFile(input_file)

# Iterate through each sheet
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=1, dtype=str) # dtype=str for leading 0 in Part Number
    
    required_columns = ["Part Number", "Product Line", "Figure No.", "Description", "PalletQty", "Weight", "Length", "Width", "Height", "Price List", "Box Program"]
    available_columns = [col for col in required_columns if col in df.columns]
    
    if available_columns:
        # Extract only the required columns
        extracted_df = df[available_columns].copy()
        extracted_df['Sheet Name'] = sheet_name
        combined_df = pd.concat([combined_df, extracted_df], ignore_index=True)

# Test data output
print(combined_df)

combined_df.to_excel(output_file, index=False)
