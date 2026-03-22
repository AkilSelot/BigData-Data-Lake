import pandas as pd
import os

def run_pipeline():
    print("🚀 Initializing Medallion Data Lake Pipeline...")
    # Layers configuration
    BRONZE, SILVER, GOLD = "data/bronze", "data/silver", "data/gold"
    for folder in [BRONZE, SILVER, GOLD]: os.makedirs(folder, exist_ok=True)

    # 1. BRONZE: Ingest Raw CSV
    df = pd.read_csv("raw_data.csv")
    df.to_csv(f"{BRONZE}/raw_ingest.csv", index=False)
    print("✔ Bronze Layer: Raw data ingested.")

    # 2. SILVER: Clean & Standardize
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    df_clean = df.drop_duplicates().dropna()
    df_clean.to_csv(f"{SILVER}/cleaned_data.csv", index=False)
    print("✔ Silver Layer: Data cleaned and standardized.")

    # 3. GOLD: Curate & Optimize (Parquet)
    if 'quantity' in df_clean.columns and 'price' in df_clean.columns:
        df_clean['total_revenue'] = df_clean['quantity'] * df_clean['price']
    df_clean.to_parquet(f"{GOLD}/analytics_final.parquet", index=False)
    print(f"✔ Gold Layer: Optimized Parquet created at {GOLD}/")

if __name__ == "__main__":
    run_pipeline()
