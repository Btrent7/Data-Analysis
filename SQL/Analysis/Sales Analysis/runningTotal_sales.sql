--RUNNING TOTAL SINGLE ITEM SALES
SELECT invoiceDate, qtyShip, 
		sum(qtyShip * unitPrice) OVER(ORDER BY invoiceDate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as RT_Sales

FROM dbo.InvSales INV

WHERE item = '123456789';


--RUNNING TOTAL ALL SALES
WITH SALES AS(
SELECT INV.orderNum, INV.invoiceDate, INV.Item, INV.fiscalYear, INV.customerNumber,
    SUM(INV.qtyShip * INV.unitPrice) as Revenue,
	SUM(INV.costperiodEndReturn * qtyShip) as COGS
FROM dbo.InvSales INV

GROUP BY INV.orderNum, INV.invoiceDate, INV.Item, INV.fiscalYear, INV.customerNumber
)

SELECT *, 
	SUM(Revenue) OVER (
        PARTITION BY customerNumber
        ORDER BY invoiceDate
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS RunningTotal_SALES
FROM SALES
WHERE fiscalYear = '2025'
;



WITH table1 AS(
SELECT
	SUM(qtyship*unitprice) as sales,
	invoicedate,
	orderwarehouse

FROM InvoiceDetailHistory
GROUP BY invoiceDate, orderWarehouse
)

SELECT 
	invoiceDate, 
	orderwarehouse,
	SUM(sales) OVER (
		PARTITION BY ORDERWAREHOUSE
		ORDER BY INVOICEDATE
	) AS SalesRunningTotal
FROM table1
WHERE orderwarehouse = 'DA' AND invoiceDate >= DATEADD(YEAR, 0, '1/1/2026')
;



SELECT 
	SLSTRTY,
	SLSNAME,
	COUNT(*) AS Count_of_Sales
FROM InvoiceDetailHistory
WHERE 
	invoiceDate >= DATEADD(YEAR, 0, '1/1/2026')
	AND orderType = 'RG'
	AND SLSTRTY IN('25', '03', '05')
GROUP BY SLSTRTY, ROLLUP(SLSNAME)
ORDER BY SLSTRTY, SLSNAME 
; 



SELECT
  SLSTRTY,
  COALESCE(SLSNAME, 'Territory Total') AS SLSNAME,
  COUNT(*) AS Count_of_Sales
FROM InvoiceDetailHistory
WHERE
  invoiceDate >= '2026-01-01'
  AND orderType = 'RG'
  AND SLSTRTY IN ('25', '03', '05')
GROUP BY SLSTRTY, ROLLUP(SLSNAME)
ORDER BY SLSTRTY, SLSNAME 
;
