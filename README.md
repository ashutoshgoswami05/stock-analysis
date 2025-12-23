## Project Summary

This project implements a fully automated, end-to-end real-time data pipeline for stock market analytics. Stock data is fetched from the Finnhub API, streamed through Confluent Cloud Kafka, and stored in Amazon S3 as a raw data lake (Bronze layer). The data is then automatically ingested into Snowflake using Snowpipe, where it is cleaned, transformed, and modeled using dbt into Silver (refined) and Gold (analytics-ready) layers.

The transformed Gold-layer data in Snowflake is directly consumed by Power BI dashboards, enabling near real-time visualization and analysis of stock market trends. The entire pipeline—including ingestion, transformation, and deployment—is fully automated using GitHub Actions, requiring no manual intervention.

## Tech Stack

- **Data Source:** Finnhub Stock Market API
- **Streaming Platform:** Confluent Cloud (Apache Kafka)
- **Object Storage:** Amazon S3
- **Data Warehouse:** Snowflake
- **Ingestion Tool:** Snowpipe
- **Transformation Framework:** dbt
- **CI/CD & Automation:** GitHub Actions
- **Languages:** Python, SQL

---

## Key Features

- 📊 Real-time stock data ingestion
- 🚀 Streaming architecture using managed Kafka
- 🪣 Scalable raw data storage in Amazon S3
- ❄️ Automated ingestion into Snowflake via Snowpipe
- 🧱 Analytics-ready transformations using dbt
- 🤖 Fully automated CI/CD pipeline
- 🔄 End-to-end hands-off execution

---

## Data Flow

1. **API Ingestion**
   - Stock data is fetched from the Finnhub API.
   - Data is published to Kafka topics hosted on Confluent Cloud.

2. **Streaming to S3**
   - Kafka consumers write streaming data to Amazon S3.
   - Data is stored in a raw, append-only format.

3. **Snowflake Ingestion**
   - Snowpipe continuously monitors the S3 bucket.
   - New files are automatically loaded into Snowflake tables.

4. **Data Transformation**
   - dbt models transform raw data into clean, analytics-ready tables.
   - Includes testing, documentation, and modular modeling.

5. **Automation**
   - GitHub Actions orchestrates and automates the entire workflow.
   - Pipelines trigger on code changes or scheduled runs.

---

## Monitoring prometheus und grafana


-  Snowflake credit used for ingestion
-  No. of files ingested last 15mins
-  Bytes billed snowflake
<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/10b9b75c-69ff-4018-9f8e-3d6d1e5d8fc0" />

<img width="1550" height="871" alt="image" src="https://github.com/user-attachments/assets/a4916bbb-8aee-48aa-a667-1789e2f4535d" />



Prometheus server

<img width="1920" height="1080" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/066aba9b-71b4-439b-82da-0d532533068d" />
