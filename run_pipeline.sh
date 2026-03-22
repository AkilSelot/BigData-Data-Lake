#!/bin/bash

echo "--- Starting Big Data Workflow ---"

# Step 1: Execute Python ETL (Medallion Architecture)
echo "Running Medallion Pipeline (Bronze -> Silver -> Gold)..."
python scripts/data_lake_etl.py

# Step 2: Execute MapReduce
echo "Running MapReduce on unstructured data..."
python scripts/word_count.py input_data.txt > word_count_results.txt

echo "--- Workflow Complete ---"
echo "Check 'data/gold' for optimized Parquet files."
echo "Check 'word_count_results.txt' for MapReduce output."
