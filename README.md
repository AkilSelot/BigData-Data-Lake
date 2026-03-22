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
🚀 How to Run the Project1. Setup EnvironmentEnsure you have the required libraries installed:Bashpip install -r requirements.txt
2. Execute the Data Lake PipelineRun the main ETL script to process data through the Bronze, Silver, and Gold layers:Bashpython scripts/data_lake_etl.py
3. Run MapReduce JobTo process unstructured text data (WordCount) locally:Bashpython scripts/word_count.py input_data.txt
4. Full Automation (One-Click)Execute the entire Big Data workflow with the provided Bash script:Bashbash run_pipeline.sh
📊 Sample Output (Gold Layer)The pipeline aggregates raw data into the Gold Layer for business intelligence. Below is a preview of the processed analytics stored in .parquet:ProductTotal QuantityTotal Revenue ($)Laptop450540,000Monitor32096,000Mouse89022,250Result: Data is now optimized for 10x faster querying in tools like Power BI or SQL Server.📧 ContactAkil Selot 📧 selotatik@gmail.comData Analyst | Big Data & Hadoop Specialist
