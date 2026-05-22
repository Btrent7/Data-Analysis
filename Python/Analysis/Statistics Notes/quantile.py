import pandas as pd
import numpy as np

pd.set_option('display.float_format', '{:2.2f}'.format)
np.set_printoptions(precision=3, suppress=True)

excel_path = "C:/Users/btrent//vendor_revenue.xlsx"

df = pd.read_excel(excel_path, sheet_name='Revenue by Vendor')
df["VNDID"] = df['VNDID'].str.strip()
df["VNDNAM"] = df['VNDNAM'].str.strip()
df["perUnit"] = round((df['Revenue'] / df['QTY']), 2)
df = df.dropna()
print(df)

sales_by_item = df.groupby('Item')['QTY'].sum()
q1 = np.quantile(sales_by_item, 0.25)
q3 = np.quantile(sales_by_item, 0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = sales_by_item[(sales_by_item < lower) | (sales_by_item > upper)]
print(sales_by_item)
print(outliers)