import pandas as pd
import matplotlib.pyplot as plt

site_orders = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Orders" : [25,  16,  23,  26,  19,  12,  24,  11, 13],
    "Drops" : [20,  10,  13,  23,  18,  2,  4,  1,  11],
    "Stocks" : [5,  6,  10,  3,  1,  10,  20,  10, 2],
    "State" : ["Texas", "Texas", "Ohio", "New York", "Texas", "Florida", "Georiga", "Minnesota", "Michigan"]
}

df_site_orders = pd.DataFrame(site_orders)
print(df_site_orders)
print()

df_site_orders_state = df_site_orders.drop(columns="Site")
df_state = df_site_orders_state.groupby("State").sum().reset_index()
df_state = df_state.sort_values("Orders", ascending=False)
print(df_state)
print()

df_state["Drops %"] = round(df_state["Drops"] / df_state["Orders"], 4) * 100
df_state["Stocks %"] = round(df_state["Stocks"] / df_state["Orders"], 4) * 100
print(df_state)

df_state_plt = df_state.plot(x="State", y=["Orders", "Drops", "Stocks"], kind="barh")
plt.show()
