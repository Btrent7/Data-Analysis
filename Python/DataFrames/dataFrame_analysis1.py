import pandas as pd
import numpy as np

pivot_table = r"C:\Users\btrent\analysis1.xlsx"
powerBi_table = r"C:\Users\btrent\analysis2.xlsx"
analysis_table = r"C:\Users\btrent\analysis3.xlsx"

df = pd.read_excel(pivot_table, sheet_name = "Sheet1")

pivot_df = df.melt(id_vars=["Date", "Site"], var_name= "Location", value_name="Value")
pivot_df = pivot_df.rename(columns = {"Site" : "Type", "Value" : "Qty"})

unpivoted_df = pivot_df.pivot_table(index=["Date", "Location"], columns="Type", values="Qty")
unpivoted_df = unpivoted_df.reset_index()
unpivoted_df = unpivoted_df.rename(columns = {"Location" : "Site"})

unpivoted_df.to_excel(powerBi_table, index=False)
print("PowerBi data table updated!")

overall_table = unpivoted_df.groupby("Site")[["Orders", "Stocks", "Drops", "W/C", "Quotes", "Closed"]].agg(['min', 'max', 'sum'])

overall_table.columns = ["_".join(col).strip() for col in overall_table.columns.values]

overall_table = overall_table.reset_index()

overall_table["Stock Ratio"] = overall_table["Stocks_sum"] / overall_table["Orders_sum"]
overall_table["Drop Ratio"] = overall_table["Drops_sum"] / overall_table["Orders_sum"]
overall_table["W/C Ratio"] = overall_table["W/C_sum"] / overall_table["Orders_sum"]
overall_table["Range %"] = ((overall_table["Orders_max"] - overall_table["Orders_min"]) / overall_table["Orders_sum"] )
overall_table["Closed %"] = np.where(overall_table["Quotes_sum"] == 0, 0, overall_table["Closed_sum"] / overall_table["Quotes_sum"] )

Closed_bins = [0.0, 0.25, 0.40, 0.50, 0.60, 1]
Closed_labes = [1, 2, 3, 4, 5]
overall_table["Closed_bins"] = pd.cut(overall_table["Closed %"], bins=Closed_bins, labels=Closed_labes, include_lowest=True)

Range_bins = [0.0, 0.07, 0.14, 0.21, 0.28, 0.50]
Range_lables = [1, 2, 3, 4, 5]
overall_table["Range_bins"] = pd.cut(overall_table["Range %"], bins=Range_bins, labels=Range_lables, include_lowest=True)

overall_table = overall_table.drop(["Orders_max", "Orders_min", "Stocks_min", "Stocks_max", "Drops_min", "Drops_max", 
                              "W/C_min", "W/C_max", "Quotes_min", "Quotes_max", "Closed_min", "Closed_max"], axis=1)

Closed_orders = overall_table.groupby("Closed_bins", observed=False)["Closed_sum"].agg(['sum', 'max'])
Closed_Avg =  overall_table.groupby("Closed_bins", observed=False)["Closed %"].mean()
Closed_Site = overall_table.groupby("Closed_bins", observed=False)["Site"].count()
Range_orders = overall_table.groupby("Range_bins", observed=False)["Orders_sum"].agg(['min', 'max'])
Range_Avg = overall_table.groupby("Range_bins", observed=False)["Range %"].mean()
Range_Site = overall_table.groupby("Range_bins", observed=False)["Site"].count()

Summary_Closed = pd.concat([Closed_orders, Closed_Avg, Closed_Site], axis=1) 
Summary_Range = pd.concat([Range_orders, Range_Avg, Range_Site], axis=1)

Summary_Closed = Summary_Closed.reset_index()
Summary_Range = Summary_Range.reset_index()

print(f""" 
{overall_table}

{Summary_Closed}

{Summary_Range}""")

with pd.ExcelWriter (analysis_table) as write:
    overall_table.to_excel(write, sheet_name="Overall_summary", index=False)
    Summary_Closed.to_excel(write, sheet_name="Closed_%_Summmary", index=False)
    Summary_Range.to_excel(write, sheet_name="Order_Range_Summary", index=False)