import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_file = r"C:\Users\melt.xlsx"
df = pd.read_excel(df_file, sheet_name="Sheet1")
print(df)
print()

df_NaN_any = df.isna().any()
df_NaN_sum = df.isna().sum()

print(df_NaN_any, df_NaN_sum)

fill_NaN = df.fillna(0.0)

groupby_df = df.drop(columns="Date")
groupby_df = groupby_df.groupby("Site").sum().reset_index()
print(groupby_df)
print()

site_pivot_table = df.pivot_table("HN", index="Site", columns="Date")
print(site_pivot_table)

site_pivot_table_mean = site_pivot_table.mean(axis="index")
print(site_pivot_table_mean)

site_pivot_table_mean2 = site_pivot_table.mean(axis="columns")
print(site_pivot_table_mean2)

df_plt = df["DA"].hist(bins=5)
# plt.show()

orders_dallas = site_pivot_table.plot(kind="bar", title="Dallas Orders by Date")
orders_dallas.legend(loc="upper left", bbox_to_anchor=(.75, .75))
# plt.show()

site_pivot_table_line = site_pivot_table.plot(x="Date", y="Site", kind="line")
# plt.show()

site_pivot_table_scatter = site_pivot_table.plot(x="2025-01-02", y="2025-01-01", kind="scatter")
# plt.show()