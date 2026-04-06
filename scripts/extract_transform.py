import pandas as pd


print("=== Starting Data Pipeline ===")

# =========================
# EXTRACT
# =========================
print("Loading raw data...")
df = pd.read_csv("data/raw/ecommerce_data.csv", encoding="utf-8-sig")

print("Initial shape:", df.shape)


# =========================
# TRANSFORM
# =========================
print("Cleaning data...")

# Fix column names
df.columns = df.columns.str.replace("ï»¿", "", regex=False).str.strip()

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna(subset=["Description", "CustomerID"])

# Convert types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    format="%m/%d/%Y %H:%M",
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["Quantity", "UnitPrice", "InvoiceDate"])
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Clean text
df["Description"] = df["Description"].str.strip()
df["Country"] = df["Country"].str.strip()

# Create new feature
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("After cleaning:", df.shape)



# =========================
# LOAD PREP
# =========================
print("Saving cleaned data...")
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("=== Pipeline completed successfully ===")