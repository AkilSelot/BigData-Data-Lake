# 🌊 Scalable Data Lake & Big Data Ecosystem

This repository demonstrates a modern **Data Lake architecture** built using Python and the Hadoop ecosystem. It showcases the transition from traditional MapReduce processing to a multi-layered **Medallion Architecture** (Bronze, Silver, Gold) for scalable, high-performance data analytics.

## ✨ Key Features
* **Medallion Architecture:** Implementation of logical data zones (Bronze, Silver, Gold) to manage data quality.
* **Hadoop MapReduce:** Custom Python-based distributed processing jobs using `MRJob`.
* **Schema-on-Read:** Dynamic schema definition and data evolution using Pandas and PyArrow.
* **Optimized Storage:** Automated conversion of raw CSV datasets to **Apache Parquet** format for 10x faster query performance.
* **ETL Automation:** End-to-end bash and Python pipelines for data ingestion, cleaning, and curation.

## 🛠️ Tech Stack
* **Languages:** Python, SQL, Bash
* **Big Data Tools:** HDFS, MapReduce (Hadoop), Apache Spark (Basics)
* **Libraries:** Pandas, PyArrow (Columnar Storage), MRJob

## 🏗️ Data Lake Architecture (Medallion)

| Layer | Type | Description | Format |
| :--- | :--- | :--- | :--- |
| **Bronze** | **Raw** | The landing zone. Stores data in its original, unaltered state. | CSV / JSON |
| **Silver** | **Cleansed** | Standardized data. Filtered, joined, and missing values handled. | CSV |
| **Gold** | **Curated** | Business-ready. Aggregated and optimized for BI and ML. | **Parquet** |

---

## 📂 Project Structure
```text
.
├── data/
│   ├── bronze/          # Raw data landing zone
│   ├── silver/          # Standardized and cleaned data
│   └── gold/            # Final optimized analytics tables (Parquet)
├── scripts/
│   ├── data_lake_etl.py # Main Python ETL Pipeline logic
│   └── word_count.py    # Hadoop MapReduce logic (unstructured data)
├── run_pipeline.sh      # Shell script to automate the entire lake
├── raw_data.csv         # Sample raw input dataset
├── input_data.txt       # Sample text for MapReduce processing
├── requirements.txt     # Python dependencies
└── README.md            # Project Documentation
