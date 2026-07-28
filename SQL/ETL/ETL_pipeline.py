from sys import path
import pyodbc
import pandas as pd
import numpy as np
import datetime


# ============================================================
# Step 1: Add ADOMD / SSMS path
# ============================================================

path.append(
    r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE"
)

from pyadomd import Pyadomd


# ============================================================
# Step 2: Power BI XMLA connection
# ============================================================

pbi_conn_str = (
    "Provider=MSOLAP;"
    "Data Source=powerbi://api.powerbi.com/v1.0/myorg/<Workspace>;"
    "Initial Catalog=<Dataset>;"
)


# ============================================================
# Step 3: Inventory DAX query
# Pull all listed columns
# ============================================================

query = """
EVALUATE
SELECTCOLUMNS(
    'VW_D365_INVENTORY',
    "ITEM_ID", 'VW_D365_INVENTORY'[ITEM_ID],
    "LEGAL_ENTITY", 'VW_D365_INVENTORY'[LEGAL_ENTITY],
    "SITE_ID", 'VW_D365_INVENTORY'[SITE_ID],
    "WAREHOUSE_ID", 'VW_D365_INVENTORY'[WAREHOUSE_ID],
    "PHYSICAL_INVENT", 'VW_D365_INVENTORY'[PHYSICAL_INVENT],
    etc...
)
"""


# ============================================================
# Step 4: Extract data from Power BI semantic model
# ============================================================

# print("Connecting to Power BI Inventory semantic model...")

with Pyadomd(pbi_conn_str) as conn:
    print("Connected to Power BI.")

    with conn.cursor().execute(query) as cur:
        rows = cur.fetchall()
        cols = [c.name for c in cur.description]

df = pd.DataFrame(rows, columns=cols)

# Clean Power BI / ADOMD column names
df.columns = (
    df.columns
    .str.replace("[", "", regex=False)
    .str.replace("]", "", regex=False)
)

print("Power BI Inventory data extraction complete.")
print(f"Rows extracted: {len(df):,}")
print(f"Columns extracted: {len(df.columns):,}")
# print(df.head())
# print(df.dtypes)
# print(df.columns.tolist())


# ============================================================
# Step 5: Stop script if no rows returned
# ============================================================

if df.empty:
    raise ValueError("No rows returned from Power BI Inventory query. SQL load cancelled.")


# ============================================================
# Step 6: Define business columns and load columns
# ============================================================

business_columns = [
    "ITEM_ID",
    "LEGAL_ENTITY",
    "SITE_ID",
    "WAREHOUSE_ID",
    "PHYSICAL_INVENT",
    "POSTED_QTY",
    ## etc...
]

metadata_columns = [
    "SNAPSHOT_DATE",
    "LOAD_TIMESTAMP"
]

load_columns = business_columns + metadata_columns

missing_columns = [col for col in business_columns if col not in df.columns]

if missing_columns:
    raise KeyError(f"Missing expected columns from DataFrame: {missing_columns}")

df_load = df[business_columns].copy()


# ============================================================
# Step 6B: Add daily snapshot metadata
# ============================================================

snapshot_date = datetime.date.today()
load_timestamp = datetime.datetime.now()

df_load["SNAPSHOT_DATE"] = snapshot_date
df_load["LOAD_TIMESTAMP"] = load_timestamp

print(f"Snapshot date for this load: {snapshot_date}")
print(f"Load timestamp for this load: {load_timestamp}")


# ============================================================
# Step 7: SQL-safe value conversion
# ============================================================

def sql_safe_value(value):
    """
    Convert pandas/numpy values into pyodbc-safe Python values.
    Handles NaN, NaT, inf, numpy floats, numpy ints, dates, and timestamps.
    """

    if pd.isna(value):
        return None

    if isinstance(value, pd.Timestamp):
        return value.to_pydatetime()

    if isinstance(value, np.datetime64):
        return pd.Timestamp(value).to_pydatetime()

    if isinstance(value, datetime.datetime):
        return value

    if isinstance(value, datetime.date):
        return value

    if isinstance(value, (np.floating, float)):
        if not np.isfinite(value):
            return None
        return float(value)

    if isinstance(value, (np.integer, int)):
        return int(value)

    if isinstance(value, str):
        value = value.strip()
        return value if value != "" else None

    return value


# ============================================================
# Step 8: Basic type cleanup
# ============================================================

date_columns = [
    "SNAPSHOT_DATE",
    "LOAD_TIMESTAMP"
]

numeric_columns = [
    "PHYSICAL_INVENT",
    "POSTED_QTY",
    "AVAIL_PHYSICAL",
    ## etc...
]

text_columns = [
    col for col in load_columns
    if col not in date_columns and col not in numeric_columns
]

for col in date_columns:
    if col in df_load.columns:
        df_load[col] = pd.to_datetime(df_load[col], errors="coerce")

for col in numeric_columns:
    if col in df_load.columns:
        df_load[col] = pd.to_numeric(df_load[col], errors="coerce")

for col in text_columns:
    if col in df_load.columns:
        df_load[col] = df_load[col].apply(
            lambda x: None if pd.isna(x) else str(x).strip()
        )
        df_load[col] = df_load[col].apply(
            lambda x: None if x == "" else x
        )

# Force final DataFrame column order to match SQL insert order
df_load = df_load[load_columns].copy()


# ============================================================
# Step 9: Diagnostics before SQL load
# ============================================================

# print("\n================ DF_LOAD DTYPES ================")
# print(df_load.dtypes)

# print("\n================ NUMERIC COLUMN DIAGNOSTICS ================")

# for col in numeric_columns:
#     if col in df_load.columns:
#         print(
#             f"{col}: "
#             f"dtype={df_load[col].dtype}, "
#             f"nulls={df_load[col].isna().sum()}, "
#             f"min={df_load[col].min()}, "
#             f"max={df_load[col].max()}"
#         )

# print("\n================ DATE COLUMN DIAGNOSTICS ================")

# for col in date_columns:
#     if col in df_load.columns:
#         print(
#             f"{col}: "
#             f"dtype={df_load[col].dtype}, "
#             f"nulls={df_load[col].isna().sum()}, "
#             f"min={df_load[col].min()}, "
#             f"max={df_load[col].max()}"
#         )

# print("\n================ ACTUAL PYTHON TYPES BY COLUMN BEFORE RECORD BUILD ================")

for col in df_load.columns:
    non_null_values = df_load[col].dropna()

    # if non_null_values.empty:
    #     print(f"{col}: ALL NULL")
    # else:
    #     sample_value = non_null_values.iloc[0]
    #     print(f"{col}: value={sample_value!r}, python_type={type(sample_value)}")


# ============================================================
# Step 10: Build SQL-safe records
# ============================================================

records = [
    tuple(sql_safe_value(value) for value in row)
    for row in df_load.itertuples(index=False, name=None)
]

print(f"\nPrepared {len(records):,} SQL-safe records.")


# ============================================================
# Step 11: SQL Server connection
# ============================================================

# print("\nConnecting to SQL Server...")

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=<Server>;"
    "DATABASE=<Database>;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

print("Connected to SQL Server.")
# print("Installed ODBC drivers:")
# print(pyodbc.drivers())


# ============================================================
# Step 12: Create SQL table if it does not exist
# ============================================================

create_table_sql = """
IF OBJECT_ID('dbo.INVENTORY','U') IS NULL
BEGIN
    CREATE TABLE dbo.INVENTORY (
        INVENTORY_SNAPSHOT_ID BIGINT IDENTITY(1,1) PRIMARY KEY,

        ITEM_ID NVARCHAR(100),
        LEGAL_ENTITY NVARCHAR(100),
        SITE_ID NVARCHAR(100),
        WAREHOUSE_ID NVARCHAR(100),

        PHYSICAL_INVENT FLOAT NULL,
        POSTED_QTY FLOAT NULL,
        AVAIL_PHYSICAL FLOAT NULL,

        ITEM_NUMBER NVARCHAR(100),
        ITEM_GROUP NVARCHAR(100),
        ITEM_GROUP_NAME NVARCHAR(255),
        PRODUCT_GROUP NVARCHAR(100),
        PRODUCT_GROUP_NAME NVARCHAR(255),
        MODULETYPE NVARCHAR(100),

        PRICE FLOAT NULL,
        MARKUP FLOAT NULL,
        PRICE_UNIT FLOAT NULL,
        PRICE_QTY FLOAT NULL,
        BASE_PRICE FLOAT NULL,
        MARKUP_VALUE FLOAT NULL,
        STANDARD_COST FLOAT NULL,

        NAME NVARCHAR(255),
        WAREHOUSE_NAME NVARCHAR(255),
        RS_SUPER_GROUP NVARCHAR(100),
        RS_SUPER_GROUP_DESCRIPTION NVARCHAR(255),

        SNAPSHOT_DATE DATE NOT NULL,
        LOAD_TIMESTAMP DATETIME2 NOT NULL DEFAULT SYSDATETIME()
    );

    CREATE INDEX IX_INVENTORY_SNAPSHOT_DATE
    ON dbo.INVENTORY (SNAPSHOT_DATE);

    CREATE INDEX IX_INVENTORY_ITEM_SITE_WH_DATE
    ON dbo.INVENTORY (
        ITEM_ID,
        SITE_ID,
        WAREHOUSE_ID,
        SNAPSHOT_DATE
    );
END;
"""

cursor.execute(create_table_sql)
connection.commit()

# print("SQL table check/create complete.")


# ============================================================
# Step 12B: Patch existing table if snapshot columns do not exist
# This prevents upload errors if dbo.PBI_INVENTORY already exists
# ============================================================

alter_table_sql = """
IF COL_LENGTH('dbo.INVENTORY', 'SNAPSHOT_DATE') IS NULL
BEGIN
    ALTER TABLE dbo.INVENTORY
    ADD SNAPSHOT_DATE DATE NULL;
END;

IF COL_LENGTH('dbo.INVENTORY', 'LOAD_TIMESTAMP') IS NULL
BEGIN
    ALTER TABLE dbo.INVENTORY
    ADD LOAD_TIMESTAMP DATETIME2 NULL;
END;
"""

cursor.execute(alter_table_sql)
connection.commit()

# print("SQL table alter/check complete.")


# ============================================================
# Step 12C: Create helpful indexes if they do not already exist
# ============================================================

create_indexes_sql = """
IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = 'IX_INVENTORY_SNAPSHOT_DATE'
      AND object_id = OBJECT_ID('dbo.PBI_INVENTORY')
)
BEGIN
    CREATE INDEX IX_INVENTORY_SNAPSHOT_DATE
    ON dbo.INVENTORY (SNAPSHOT_DATE);
END;

IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = 'IX_INVENTORY_ITEM_SITE_WH_DATE'
      AND object_id = OBJECT_ID('dbo.PBI_INVENTORY')
)
BEGIN
    CREATE INDEX IX_INVENTORY_ITEM_SITE_WH_DATE
    ON dbo.INVENTORY (
        ITEM_ID,
        SITE_ID,
        WAREHOUSE_ID,
        SNAPSHOT_DATE
    );
END;
"""

cursor.execute(create_indexes_sql)
connection.commit()

print("SQL index check/create complete.")


# ============================================================
# Step 13: Print SQL table schema
# ============================================================

cursor.execute("""
SELECT 
    ORDINAL_POSITION,
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_SCALE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo'
  AND TABLE_NAME = 'INVENTORY'
ORDER BY ORDINAL_POSITION;
""")

print("\n================ SQL TABLE SCHEMA ================")

for row in cursor.fetchall():
    print(row)


# ============================================================
# Step 14: Build dynamic insert statement
# ============================================================

column_list_sql = ",\n    ".join(load_columns)
placeholder_sql = ",".join(["?"] * len(load_columns))

insert_sql = f"""
INSERT INTO dbo.INVENTORY (
    {column_list_sql}
)
VALUES ({placeholder_sql})
"""

# print("\n================ INSERT SQL ================")
# print(insert_sql)


# ============================================================
# Step 15: Daily append / same-day replacement transaction
# ============================================================

try:
    print("\nBeginning SQL transaction...")

    connection.autocommit = False

    cursor.execute("""
        SELECT MAX(SNAPSHOT_DATE)
        FROM dbo.INVENTORY;
    """)

    max_snapshot_date = cursor.fetchone()[0]

    print(f"Max SNAPSHOT_DATE currently in SQL: {max_snapshot_date}")
    print(f"Current pipeline SNAPSHOT_DATE: {snapshot_date}")

    if max_snapshot_date == snapshot_date:
        print(
            f"Snapshot date {snapshot_date} already exists. "
            "Deleting existing rows for this date before reloading..."
        )

        cursor.execute("""
            DELETE FROM dbo.PBI_INVENTORY
            WHERE SNAPSHOT_DATE = ?;
        """, snapshot_date)

        print(f"Deleted {cursor.rowcount:,} existing rows for {snapshot_date}.")

    else:
        print(
            f"No existing snapshot for {snapshot_date}. "
            "Appending new daily inventory snapshot."
        )

    print(f"\nLoading {len(records):,} rows into SQL Server...")

    cursor.fast_executemany = True

    batch_size = 20000

    for start in range(0, len(records), batch_size):
        batch = records[start:start + batch_size]

        cursor.executemany(insert_sql, batch)

        print(f"Loaded {min(start + batch_size, len(records)):,} / {len(records):,}")

    connection.commit()

    print("SQL transaction committed successfully.")

except Exception as e:
    connection.rollback()
    print("SQL transaction rolled back due to error.")
    raise e


# ============================================================
# Step 16: Verify current snapshot row count in SQL Server
# ============================================================

cursor.execute("""
SELECT COUNT(*)
FROM dbo.PBI_INVENTORY
WHERE SNAPSHOT_DATE = ?;
""", snapshot_date)

sql_snapshot_row_count = cursor.fetchone()[0]

print(f"\nRows loaded for snapshot date {snapshot_date}: {sql_snapshot_row_count:,}")

if sql_snapshot_row_count != len(df_load):
    print("WARNING: SQL snapshot row count does not match DataFrame row count.")
else:
    print("Success: SQL snapshot row count matches extracted DataFrame row count.")


# ============================================================
# Step 16B: Inventory history summary
# ============================================================

cursor.execute("""
SELECT 
    COUNT(*) AS TOTAL_ROWS,
    MIN(SNAPSHOT_DATE) AS EARLIEST_SNAPSHOT_DATE,
    MAX(SNAPSHOT_DATE) AS LATEST_SNAPSHOT_DATE,
    COUNT(DISTINCT SNAPSHOT_DATE) AS SNAPSHOT_DAY_COUNT
FROM dbo.PBI_INVENTORY;
""")

summary = cursor.fetchone()

print("\n================ INVENTORY HISTORY SUMMARY ================")
print(f"Total rows in table: {summary[0]}")
print(f"Earliest snapshot date: {summary[1]}")
print(f"Latest snapshot date: {summary[2]}")
print(f"Distinct snapshot days: {summary,}")


# ============================================================
# Step 16C: Check for rows with NULL SNAPSHOT_DATE
# Useful if table existed before this pipeline change
# ============================================================

cursor.execute("""
SELECT COUNT(*)
FROM dbo.INVENTORY
WHERE SNAPSHOT_DATE IS NULL;
""")

null_snapshot_count = cursor.fetchone()[0]

if null_snapshot_count > 0:
    print(
        f"WARNING: Found {null_snapshot_count:,} historical rows with NULL SNAPSHOT_DATE. "
        "These may be rows loaded before the snapshot logic was added."
    )
else:
    print("No NULL SNAPSHOT_DATE rows found.")


# ============================================================
# Step 17: Close SQL resources
# ============================================================

cursor.close()
connection.close()

print("\nInventory pipeline process complete.")
