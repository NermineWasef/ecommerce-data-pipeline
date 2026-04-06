# E-Commerce Data Pipeline

## Overview
This project implements an end-to-end data engineering pipeline for processing and analyzing e-commerce transactional data.

The pipeline ingests raw sales data, performs data cleaning and validation, transforms it into an analysis-ready format, and loads it into a relational database for downstream querying.

---

## Problem
Raw e-commerce datasets often contain:
- Missing customer identifiers
- Invalid transactions (negative quantities/prices)
- Inconsistent date formats

These issues make direct analysis unreliable.

This project addresses these challenges by building a structured ETL pipeline.

---

## Pipeline Architecture
1. Extract raw CSV data from `/data/raw`
2. Transform:
   - Remove invalid records (negative quantity/price)
   - Handle missing values
   - Convert date formats
   - Compute revenue per transaction
3. Load cleaned data into SQLite database
4. Run analytical SQL queries

---

## Technologies
- Python (Pandas)
- SQLite
- SQLAlchemy
- Jupyter Notebook

---

## Key Engineering Features
- Modular ETL scripts (`extract_transform.py`, `load_to_sql.py`)
- Separation of raw vs processed data layers
- Reproducible pipeline execution
- SQL-based analytical layer

---

## Dataset Summary
- ~500K transactions
- Cleaned dataset after filtering invalid records
- Revenue column engineered from quantity × price

---

## Example Insights
- Total revenue: ~8.8M
- Top 5 countries by revenue identified
- Best-selling products analyzed
- Monthly revenue trends visualized

---

## How to Run
```bash
python scripts/extract_transform.py
python scripts/load_to_sql.py
python scripts/run_queries.py

