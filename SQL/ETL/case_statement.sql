SELECT DISTINCT
    GROUP_ID,
    CASE GROUP_ID
        WHEN '101' THEN 'Steel'
        WHEN '112' THEN 'Plastic'
		    WHEN '123' THEN 'Graved'
        WHEN '134' THEN 'Cast'
		    WHEN '145' THEN 'Hangers'
        WHEN '156' THEN 'Lets'
		    WHEN '167' THEN 'Electronics'
        WHEN '178' THEN 'Comp'
		    WHEN '189' THEN 'Vlvs 1'
        WHEN '190' THEN 'Vlvs 2'
		    WHEN '201' THEN 'Vlvs 3'
        WHEN '212' THEN 'Black Steel'
		    WHEN '223' THEN 'Vlvs 4'
        WHEN '234' THEN 'Eqpt'
		    WHEN '245' THEN 'Misc'
        WHEN '256' THEN 'Products'
		    WHEN '267' THEN 'Fob'
        WHEN '278' THEN 'Pox'
		    WHEN '289' THEN 'Foam'
        WHEN '290' THEN 'Oxygen'
        ELSE 'Unknown'
    END AS GROUP_TITLE
FROM dbo.ItemDetail
