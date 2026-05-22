import pandas as pd
import matplotlib.pyplot as plt

site_orders1 = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Orders" : [25,  16,  23,  26,  19,  12,  24,  11, 13],
    "Drops" : [20,  10,  13,  23,  18,  2,  4,  1,  11],
    "Stocks" : [5,  6,  10,  3,  1,  10,  20,  10, 2],
    "State" : ["Texas", "Texas", "Ohio", "New York", "Texas", "Florida", "Georiga", "Minnesota", "Michigan"],
    "Date" : ['1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025', '1/1/2025']
}

site_orders2 = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Orders" : [36,  19,  23,  26,  19,  12,  24,  11, 21],
    "Drops" : [20,  13,  13,  23,  18,  2,  4,  1,  11],
    "Stocks" : [16,  6,  10,  3,  1,  10,  20,  10, 10],
    "State" : ["Texas", "Texas", "Ohio", "New York", "Texas", "Florida", "Georiga", "Minnesota", "Michigan"],
    "Date" : ['2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025', '2/1/2025']
}

site_orders3 = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Orders" : [25,  16,  23,  29,  19,  1,  24,  11, 13],
    "Drops" : [20,  10,  13,  29,  18,  1,  4,  1,  11],
    "Stocks" : [5,  6,  10,  0,  1,  0,  20,  10, 2],
    "State" : ["Texas", "Texas", "Ohio", "New York", "Texas", "Florida", "Georiga", "Minnesota", "Michigan"],
    "Date" : ['3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025', '3/1/2025']
}

site_orders4 = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Orders" : [25,  7,  23,  26,  28,  12,  20,  11, 13],
    "Drops" : [20,  1,  13,  23,  18,  2,  0,  1,  11],
    "Stocks" : [5,  6,  10,  3,  10,  10,  20,  10, 2],
    "State" : ["Texas", "Texas", "Ohio", "New York", "Texas", "Florida", "Georiga", "Minnesota", "Michigan"],
    "Date" : ['4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025', '4/1/2025']
}

orders1 = pd.DataFrame(site_orders1)
orders2 = pd.DataFrame(site_orders2)
orders3 = pd.DataFrame(site_orders3)
orders4 = pd.DataFrame(site_orders4)

concat_table_keys = pd.concat([orders1, orders2, orders3, orders4], ignore_index=False, keys=['Jan', 'Feb', 'Mar', 'Apr'])

concat_table_noKeys = pd.concat([orders1, orders2, orders3, orders4], ignore_index=True, keys=['Jan', 'Feb', 'Mar', 'Apr'])
print(concat_table_keys)
print(concat_table_noKeys)

site_revenue = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Spend" : [24750, 16000, 25000, 26500,  18760,  12209,  24050,  12400, 10030],
    "Net Revenue" : [200000,  100000,  130000,  230000,  180000,  20000,  40000,  10000,  110000]
}

site_supervisors = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Name" : ["Bob", "Jeff", "Bill", "Kyle", "George", "Jerry", "Terry", "Harley", "David"],
    "Salary" : [70000,  70000,  39000,  42000,  80000,  52000,  40000,  56000,  60000],
    "DOB" : ['1/1/1996', '1/1/1976', '1/1/1966', '1/7/1976', '12/1/1986', '1/5/1976', '3/1/1976', '7/22/1996', '1/9/1977']
}

site_inventory = {
    "Site" : ["DA", "HN", "CL", "NY", "SA", "OL", "GA", "MN", "MI"],
    "Item ID" : [699001, 699002, 699003, 699004, 699005, 699006,699007, 699008, 699009],
    "Item Qty" : [2000,  1000,  300,  230,  18000,  200,  40,  100,  110]
}

orders = pd.DataFrame(concat_table_noKeys)
revenue = pd.DataFrame(site_revenue)
supervisors = pd.DataFrame(site_supervisors)
inventory = pd.DataFrame(site_inventory)

orders_revenue_sups = orders.merge(revenue, on='Site') \
    .merge(supervisors, on='Site') \
    .merge(inventory, on='Site')

orders_revenue_sups = orders_revenue_sups.sort_values('Orders', ascending=False)

index_test = ((orders_revenue_sups["Orders"] >= 20) & (orders_revenue_sups["Stocks"] < 10))

print(orders_revenue_sups)
print()
print(orders_revenue_sups[index_test])