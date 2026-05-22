# To run this code:
# Change line 17 for Excel worksheet name
# Change line 18 for SQL query month
# Change line 19 for SQL query year 

import pyodbc
import pandas as pd
import openpyxl as op

temp_file = r'C:\Users\btrent\Cost_template.xlsx'
test_file = r'C:\Users\btrent\test_query.xlsx'
calc_table = r'C:\Users\btrent\CostOutCalculator.xlsx'



# Change Worksheet & SQL Query to Previous Month
month      = input('Name the Worksheet: ')
month_num  = int(input('Month (Number 1-12): '))
year       = int(input('Year: '))

# Create New Worksheet 
workbook = op.load_workbook(temp_file)



#Step 1: Server Connection
connection = pyodbc.connect(
    'DRIVER= ---;'
    'SERVER= ---;'
    'DATABASE= --- ;'
    'Trusted_Connection= --;'
)

#Step 2: SQL Query
query = f'''
SELECT cim.ITMDESC, vch3.ITMID, SUM(vch3.ITMQTY) AS VCHQTY
  FROM [SYSCOMP].[dbo].[DPHVCH3] vch3

INNER JOIN dbo.DPHVCH1 vch1
ON vch3.VCHNO = vch1.VCHNO

INNER JOIN dbo.DimDate dte
ON vch1.VCHDTE = dte.mdyDate

INNER JOIN dbo.DCSCIM cim
ON cim.ITMID = vch3.ITMID

JOIN dbo.DCSDIM dim
ON vch3.ITMID = dim.ITMID AND vch1.PLT = dim.PLT

WHERE vch3.ITMID IN ('7M99001921','7M99001922','6990010526','6990010527','6990010528','6990010529','6990010590',
					 '6990010530','6990010531','7M99001923','6990010532','7M99001924','7M99001933','7M99001934',
					 '7M99001900','7M99001901','7M99001902','7M99001903','7M99001904','7M99001905','7M99001906',
					 '7M99001907','7M99001908','7M99001909','7M99001910','7M99001911','7M99001912','7M99001913',
					 '7M99001914','7M99001915','7M99001916','7M99001917','7M99001918','7M99001919')

AND dte.calendarYear =  '{year}'
AND dte.calendarMonth = '{month_num}'

GROUP BY cim.ITMDESC, vch3.ITMID
ORDER BY itmid DESC;
'''

#Step 3: Read SQL in DataFrame 
sql_df = pd.read_sql(query, connection)
sql_df = pd.DataFrame(sql_df)

sql_df = sql_df.drop(columns='ITMDESC')
sql_df['ITMID'] = sql_df['ITMID'].str.strip()



# Read CostOutCalc_temp_file Workbook
copy = pd.read_excel(temp_file, sheet_name='PyCopy', header=0)
copy = pd.DataFrame(copy, dtype=str)


# Merge Excel with SQL Query
table = pd.merge(copy, sql_df, on='ITMID', how='left')


# Format Table
table['PC1'] = table['PC1'].astype(float)
table['PC2'] = table['PC2'].astype(float)
table['CO1'] = table['CO1'].astype(float)
table['ITMID'] = table['ITMID'].replace('nan','')
table['PHD - Savings Calculator'] = table['PHD - Savings Calculator'].replace('nan','')
table['costTotal'] = table['CO1'] * table['VCHQTY']


# Check Formatting CO1 (should be negative, not 'NaN')
print(table)


# table.to_excel(test_file, sheet_name='test', index=False)


# Write table to Excel Main Table
with pd.ExcelWriter(calc_table, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    table.to_excel(writer, sheet_name=month, index=False)

workbook.save(temp_file)
workbook.close()
