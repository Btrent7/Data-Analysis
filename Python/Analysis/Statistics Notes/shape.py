import pandas as pd
import numpy as np

pd.set_option('display.float_format', '{:2.4f}'.format)
np.set_printoptions(precision=4, suppress=True)

excel_path = "C:/Users/btrent//vendor_revenue.xlsx"

df = pd.read_excel(excel_path, sheet_name='Revenue by Vendor')

counts = df['VNDNAM'].value_counts()
vnd_percentage = counts / df.shape[0] # .shape[0] to get total rows in df

print(counts)
print(vnd_percentage)