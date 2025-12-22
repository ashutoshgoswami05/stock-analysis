
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

