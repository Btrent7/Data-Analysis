-- FACT SALES TABLE
SELECT 
    item AS ITMID, -- DCSCIM Table
    customerNumber AS CUSTNUM, -- Customer Table
    SLSMAN AS SLSMANNUM, -- Salesman Table
    sum(qtyship) AS QTYSOLD, 
    sum(qtyship*unitprice) AS SALES_TOTAL,
    sum(qtyship*costperiodendreturn) AS COGS,
    orderWarehouse,
    SLSTRTY, -- Region Table
    orderType,
    SUPERGRP,
    GMGROUP, -- Group Table
    invoiceDate -- Date Table

FROM InvoiceDetailHistory

GROUP BY 
    ITEM, 
    customerNumber, 
    SLSMAN, 
    orderWarehouse, 
    SLSTRTY, 
    orderType, 
    SUPERGRP, 
    GMGROUP, 
    invoiceDate

;


-- JOIN TO ITMID
SELECT ITMID, ITMDESC, VNDID, PRDGRP, PRDCTG, TRGTPUR
FROM DCSCIM
;


-- JOIN TO CUSTNUM
SELECT DISTINCT
    customerNumber AS CUSTNUM, 
    CSTNAM,
    CUST_CTRY, 
    CUST_CTRYDSC, 
    CUST_MCCODE

FROM InvoiceDetailHistory

;


-- JOIN TO SLSMANNUM
SELECT DISTINCT
    SLSMAN AS SLSMANNUM,
    SLSNAME,
    SLSTRTY

FROM InvoiceDetailHistory

;


-- JOIN TO SLSTRTY
SELECT DISTINCT
    SLSTRTY,
    REGIONNAME AS TRTRY_NAME,
    TRTYDSC AS TRTRY_DESC,
    SLSTRTY AS SALES_TRTRY,
    TRTYDSC_LONG,
    RASCOTRTY

FROM InvoiceDetailHistory

;


-- JOIN TO INVOICEDATE
SELECT 
    calendarDate,
    calendarYear,
    fiscalPeriod,
    fiscalYear,
    calendarMonth,
    monthName,
    businessDay,
    daysInPeriod,
    calendarDayOfYear

FROM DimDate

WHERE calendarYear >= '2019'

;


-- JOIN TO GMGROUP 
SELECT Distinct
    gmgroup,
    CASE gmgroup
        WHEN '6A6A100' THEN 'Steel Pipe'
        WHEN '6A6A110' THEN 'Plastic Pipe'
		WHEN '6A6A120' THEN 'Grooved'
        WHEN '6A6A130' THEN 'Cast Iron'
		WHEN '6A6A140' THEN 'Hangers'
        WHEN '6A6A150' THEN 'Branchlets'
		WHEN '6A6A160' THEN 'Electrical'
        WHEN '6A6A170' THEN 'Air Compressors'
		WHEN '6A6A180' THEN 'OSY Chck Vlvs'
        WHEN '6A6A190' THEN 'Butterfly Vlvs'
		WHEN '6A6A200' THEN 'Backflow Vlvs'
        WHEN '6A6A210' THEN 'Black Steel Nipples'
		WHEN '6A6A220' THEN 'Trim Vlvs'
        WHEN '6A6A230' THEN 'FDE'
		WHEN '6A6A240' THEN 'Misc'
        WHEN '6A6A250' THEN 'Flex Products'
		WHEN '6A6A260' THEN 'FAB'
        WHEN '6A6A270' THEN 'Pex'
		WHEN '6A6A280' THEN 'Foam'
        WHEN '6A6A290' THEN 'Nitro'
        ELSE 'Undefined'
    END AS GroupTitle
FROM dbo.InvoiceDetailHistory
WHERE GMGROUP <> ''
;
