import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_data.csv")

# Create SQLite database connection
engine = create_engine("sqlite:///ecommerce.db")

# Load data into SQL table
df.to_sql("sales_data", con=engine, if_exists="replace", index=False)

print("Data loaded successfully into SQLite database: ecommerce.db")
print("Table name: sales_data")
print("Number of rows loaded:", len(df))