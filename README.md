# Retail Transaction Analytics Pipeline using Azure

## Project Overview

This project demonstrates an end-to-end Azure Data Engineering solution for a retail business using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Synapse Analytics and PySpark.

The objective is to collect retail transaction events from a REST API, store raw data in ADLS Gen2, clean and transform the data using PySpark, and generate daily revenue and purchase summaries.

The final Gold dataset is exposed through an Azure Synapse Serverless SQL external table so business users can query the results using SQL.

## Business Problem

A retail business wants a daily report containing:

- Total number of purchases.
- Total revenue generated each day.

The source API contains multiple event types, including purchases, refunds and cancellations. The business requires only successful purchase events for its daily sales reporting.

This project automates the complete data processing workflow to meet that requirement.

## Project Architecture

REST API (JSON)
↓
Azure Data Factory – Data Ingestion
↓
ADLS Gen2 – Bronze Layer
↓
Azure Synapse Spark – PySpark Transformations
↓
ADLS Gen2 – Silver Layer
↓
PySpark – Daily Aggregations
↓
ADLS Gen2 – Gold Layer
↓
Azure Synapse Serverless SQL – External Table
↓
Business Reporting

## Technologies Used

| Technology | Purpose |
|---|---|
| Azure Data Factory | Data ingestion and pipeline orchestration |
| Azure Data Lake Storage Gen2 | Cloud data storage |
| Azure Synapse Analytics | Spark processing and SQL querying |
| PySpark | Data cleaning and transformation |
| Python | Data processing |
| SQL | Querying Gold data |
| Parquet | Columnar data storage |
| Medallion Architecture | Bronze, Silver and Gold data organization |

## Medallion Architecture

### 1. Bronze Layer – Raw Data

- Fetch retail transaction data from a REST API using Azure Data Factory.
- Copy incoming JSON data into ADLS Gen2.
- Store the ingested data in Parquet format.
- Preserve incoming transaction events, including purchases, refunds and cancellations.

### 2. Silver Layer – Data Cleaning and Transformation

Use PySpark in Azure Synapse Spark to:

- Read data from the Bronze layer.
- Filter records where event_type = 'purchase'.
- Remove records containing null customer IDs and amounts.
- Convert event timestamps into a date column.
- Standardize payment methods to lowercase.
- Convert amount into a numeric data type.
- Select the required columns.
- Store the cleaned dataset in Parquet format in the Silver layer.

### 3. Gold Layer – Business Aggregation

Read the cleaned Silver dataset and perform daily aggregations.

Calculate:

- Daily Revenue = SUM(amount)
- Total Purchases = COUNT(*)

Group the results by event_date and store the aggregated dataset in the Gold layer.

## Azure Data Factory Pipeline

The ingestion pipeline uses the Copy Data activity.

Source:
- REST API
- JSON format
- HTTP linked service

Destination:
- Azure Data Lake Storage Gen2
- Bronze directory
- Parquet format

The pipeline transfers source data into the data lake for further processing.

## PySpark Transformations

The Silver layer performs filtering, null handling, timestamp conversion, data type conversion and standardization.

The Gold layer performs daily aggregations to calculate revenue and purchase counts.

## SQL Reporting

An external data source, external file format and external table are created in Azure Synapse Serverless SQL.

Example query:

```sql
SELECT *
FROM daily_revenue
ORDER BY event_date;
```

The external table allows business users to query the Gold dataset using SQL without loading the entire dataset into a traditional SQL table.

## Expected Output

| Event Date | Daily Revenue | Total Purchases |
|---|---:|---:|
| 2024-06-01 | 1300 | 2 |
| 2024-06-02 | 2000 | 3 |
| 2024-06-03 | 3500 | 5 |

*Illustrative output values.*

## Key Learning Outcomes

- Building end-to-end Azure data pipelines.
- Integrating REST APIs with Azure Data Factory.
- Working with Azure Data Lake Storage Gen2.
- Implementing Medallion Architecture.
- Performing data cleaning and transformation using PySpark.
- Performing aggregations using Spark DataFrames.
- Working with Parquet files.
- Creating external SQL tables in Azure Synapse.
- Making business-ready data available for reporting.

## Conclusion

This project demonstrates how raw retail transaction events can be transformed into reliable, business-ready daily sales information using Azure Data Engineering services.

It provides an end-to-end understanding of data ingestion, cloud storage, distributed data processing, data transformation and SQL-based reporting.

## Author

Neha Mahajan

Aspiring Data Engineer | Python | SQL | PySpark | Azure | Databricks | ADLS Gen2
