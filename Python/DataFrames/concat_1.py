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
