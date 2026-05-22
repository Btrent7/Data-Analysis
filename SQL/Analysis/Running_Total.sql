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
