-- 1) Total revenue
SELECT ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_data;

-- 2) Total number of transactions
SELECT COUNT(DISTINCT InvoiceNo) AS total_transactions
FROM sales_data;

-- 3) Top 10 products by revenue
SELECT Description, ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_data
GROUP BY Description
ORDER BY total_revenue DESC
LIMIT 10;

-- 4) Top 10 countries by revenue
SELECT Country, ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_data
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- 5) Monthly revenue trend
SELECT 
    strftime('%Y-%m', InvoiceDate) AS month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM sales_data
GROUP BY month
ORDER BY month;

-- 6) Top 10 customers by revenue
SELECT CustomerID, ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_data
GROUP BY CustomerID
ORDER BY total_revenue DESC
LIMIT 10;