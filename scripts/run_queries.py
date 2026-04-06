import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///ecommerce.db")

queries = {
    "Total Revenue": """
        SELECT ROUND(SUM(Revenue), 2) AS total_revenue
        FROM sales_data;
    """,
    
    "Total Transactions": """
        SELECT COUNT(DISTINCT InvoiceNo) AS total_transactions
        FROM sales_data;
    """,
    
    "Top 10 Products by Revenue": """
        SELECT Description, ROUND(SUM(Revenue), 2) AS total_revenue
        FROM sales_data
        GROUP BY Description
        ORDER BY total_revenue DESC
        LIMIT 10;
    """,
    
    "Top 10 Countries by Revenue": """
        SELECT Country, ROUND(SUM(Revenue), 2) AS total_revenue
        FROM sales_data
        GROUP BY Country
        ORDER BY total_revenue DESC
        LIMIT 10;
    """,
    
    "Monthly Revenue Trend": """
    SELECT 
        strftime('%Y-%m', InvoiceDate) AS month,
        ROUND(SUM(Revenue), 2) AS monthly_revenue
    FROM sales_data
    GROUP BY month
    ORDER BY month;
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    result = pd.read_sql(query, engine)
    print(result)