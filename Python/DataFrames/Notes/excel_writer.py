import pandas as pd
import numpy as np

main = "C:/Users//Comparison.xlsx"
usage = "C:/Users//Usages.xlsx"

main1 = pd.read_excel(main, sheet_name="all_Items")
usage1 = pd.read_excel(usage, sheet_name="all_Usage")

usage1 = usage1[["Item ID", "Total Usage", "Production Usage"]]

merge_usage = pd.merge(main1, usage1, on='Item ID', how='left')

print(merge_usage)

comparison_final = "C:/Users//Comparison.xlsx"


# Write to a new sheet in the same Excel file
with pd.ExcelWriter(comparison_final, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    merge_usage.to_excel(writer, sheet_name="new_sheet", index=False)

print("Data written to 'new_sheet' in Comparison.xlsx.")