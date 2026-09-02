-- Superstore E-commerce Analytics
-- Business Analysis SQL Queries

-- 1. Overall Business Performance
-- Calculate overall sales, profit, and profit margin

SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin_Percent
FROM superstore_clean;

-- 2. Sales and profit by year

SELECT
    strftime('%Y', "Order Date") AS Year,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore_clean
GROUP BY strftime('%Y', "Order Date")
ORDER BY Year;

-- 3. Sales by region

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM superstore_clean
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 4. Profit by category

SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM superstore_clean
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 5. Profit margin by region

SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin_Percent
FROM superstore_clean
GROUP BY Region
ORDER BY Profit_Margin_Percent DESC;

-- 6. Average discount and profit by discount level

SELECT
    Discount,
    AVG(Profit) AS Average_Profit,
    SUM(Profit) AS Total_Profit
FROM superstore_clean
GROUP BY Discount
ORDER BY Discount;

-- 7. Loss-making products

SELECT
    "Product Name",
    SUM(Profit) AS Total_Profit
FROM superstore_clean
GROUP BY "Product Name"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;

-- 8. Profit by sub-category

SELECT
    "Sub-Category",
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore_clean
GROUP BY "Sub-Category"
ORDER BY Total_Profit DESC;