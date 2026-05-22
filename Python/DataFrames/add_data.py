import pandas as pd
from openpyxl import writer

master_file = r"C:\Users\master.xlsx"
asc_file = r"C:\Users\qty.xlsx"
updated_final = r"C:\Users\update.xlsx"

# Master SKU file DataFrame
master = pd.read_excel(master_file, sheet_name="Master", dtype={'Vendor SKU': str})
master = pd.DataFrame(master)
master['Vendor SKU'] = master['Vendor SKU'].str.strip()


# Vendor Data for Update
ascQty = pd.read_excel(asc_file, sheet_name="ASC Combo", dtype={'Vendor SKU': str})
ascqty = pd.DataFrame(ascQty)
aqty = ascQty.drop_duplicates(subset='Vendor SKU', keep='first').reset_index()

final = master.merge(aqty[['Vendor SKU', 'CRTQTY',  'PLTQTY', 'MSTRQTY']], on='Vendor SKU', how='left', suffixes=['', '_update'])

# Fill blank columns
final['CRTQTY'] = final['CRTQTY'].fillna(final['CRTQTY_update'])
final['PLTQTY'] = final['PLTQTY'].fillna(final['PLTQTY_update'])
final['MSTRQTY'] = final['MSTRQTY'].fillna(final['MSTRQTY_update'])

# Drop SKU update column
final.drop(columns=['CRTQTY_update', 'PLTQTY_update', 'MSTRQTY_update'], inplace=True)


# print(final)
final.to_excel(updated_final, index=False)