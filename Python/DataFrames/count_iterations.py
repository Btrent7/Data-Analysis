def partDescription_count(partList, gt1_count, gt2_count, gt3_count):
    for desc in partList.keys():
        if "GT1" in desc:
            gt1_count += 1
        elif "GT2" in desc:
            gt2_count += 1
        elif "GT3" in desc:
            gt3_count += 1
    return gt1_count, gt2_count, gt3_count

def priceDescription_total(partList, gt1_price, gt2_price, gt3_price):
    for desc, price in partList.items():
        if "GT1" in desc:
            gt1_price += float(price)
        if "GT2" in desc:
            gt2_price += float(price)
        if "GT3" in desc:
            gt3_price += float(price)
    return gt1_price, gt2_price, gt3_price

gt1_count = 0
gt2_count = 0
gt3_count = 0

gt1_price = 0
gt2_price = 0 
gt3_price = 0

rascoParts = {'RASCO,#123, GT2': 150.20, 
              'RASCO,#145, GT3' : 155.27, 
              'RASCO,#124, GT2' : 125.78, 
              'RASCO,#125, GT1': 150.20, 
              'RASCO,#1425, GT3' : 155.27, 
              'RASCO,#24, GT2' : 125.78, 
              'RASCO,#126, GT1': 150.20, 
              'RASCO,#1445, GT3' : 155.27, 
              'RASCO,#14, GT2' : 125.78, 
              'RASCO,#127, GT1': 150.20, 
              'RASCO,#1465, GT3' : 155.27, 
              'RASCO,#12, GT2' : 125.78,
              'RASCO,#123, GT2': 150.20, 
              'RASCO,#145, GT3' : 155.27, 
              'RASCO,#124, GT2' : 125.78, 
              'RASCO,#125, GT1': 150.20}

gt1_count, gt2_count, gt3_count = partDescription_count(rascoParts, gt1_count, gt2_count, gt3_count)
gt1_price, gt2_price, gt3_price = priceDescription_total(rascoParts, gt1_price, gt2_price, gt3_price)
print(f"\nPrice Totals by Item Description:")
print(f"GT1 Total Count {gt1_count} : ${round(gt1_price, 2)}")
print(f"GT2 Total Count {gt2_count} : ${round(gt2_price, 2)}")
print(f"GT3 Total Count {gt3_count} : ${round(gt3_price, 2)} \n")

# -- PN Inventory Report --
def pn_inventory_count(part_inventory, pn):
    print(f"\nInventory Report: {pn}")
    for dc, inventory in part_inventory.items():
        if inventory == 0:
            print(f"Out of Stock!:    {dc}, 0")
        elif inventory < 200:
            print(f"Iventory Low:     {dc}, {inventory}")
        elif inventory <= 1000:
            print(f"Inventory Stable: {dc}, {inventory}")
        elif inventory > 1000:
            print(f"Overstocked:      {dc}, {inventory}")


pn_6990000001 = {'NY': 1500, 'BN': 1250, 'EG': 190, 'DA': 980, 'PO': 654}
pn_6990000002 = {'NY': 150, 'BN': 950, 'EG': 2190, 'DA': 80, 'PO': 773}
pn_6990000003 = {'NY': 500, 'BN': 250, 'EG': 590, 'DA': 0, 'PO': 954}

pn_inventory_count(pn_6990000001, 'RASCO,#123,GT1 6990000001')
pn_inventory_count(pn_6990000002, 'RASCO,#234,GT2 6990000002')
pn_inventory_count(pn_6990000003, 'RASCO,#345,GT3 6990000003')

# -- DIM Invetory Report --
def dim_inventory_count(dim_inventory, dim):
    print(f"\nInventory Report: {dim}")
    for pn, inventory in dim_inventory.items():
        if inventory == 0:
            print(f"Out of Stock!:    {pn}, 0")
        elif inventory < 200:
            print(f"Iventory Low:     {pn}, {inventory}")
        elif inventory <= 1000:
            print(f"Inventory Stable: {pn}, {inventory}")
        elif inventory > 1000:
            print(f"Overstocked:      {pn}, {inventory}")


dim_ny = {'6990000001': 1500, '6990002378': 1250, '6990000201': 190, '6990000076': 980, '6990002301': 654}
dim_da = {'6990000001': 120, '6990002378': 220, '6990000201': 1190, '6990000076': 2980, '6990002301': 54}
dim_hn = {'6990000001': 1320, '6990002378': 20, '6990000201': 122, '6990000076': 80, '6990002301': 754}

dim_inventory_count(dim_ny, 'NY')
dim_inventory_count(dim_da, 'DA')
dim_inventory_count(dim_hn, 'HN')