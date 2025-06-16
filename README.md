# 🛒 Retail Analytics Platform

**A personal end-to-end data platform project** designed to simulate the architecture, tooling, and workflows of a modern retail analytics stack. This project demonstrates best practices across the full data lifecycle: ingestion, orchestration, transformation, API exposure, and deployment.

### Overview

This platform processes simulated point-of-sale (POS) and inventory data through a complete pipeline:

- Ingests batch data into **Google Cloud Storage** and loads into **BigQuery**
- Applies data quality checks and transformations using **dbt**
- Orchestrates workflows with **Airflow**
- Exposes endpoints via a **FastAPI** microservice
- Deploys to **GKE** with full CI/CD, observability, and infrastructure as code via **Terraform** using **Githun Actions**.

📌 **Stack**: Python · BigQuery · dbt · Airflow · FastAPI · GCP · Kubernetes · Terraform · GitHub Actions · Redis · Docker · Kafka · Grafana

---

## Project Structure

| Folder | Description |
|--------|-------------|
| [`data-ingestion/`](./data-ingestion/) | Python scripts or DAGs for ingesting simulated retail data into GCS and BigQuery |
| [`dbt/`](./dbt/) | dbt project containing models, seeds, tests, macros and documentation |
| [`airflow/`](./airflow/) | Airflow DAGs and configuration, including Cosmos integration |
| [`api/`](./api/) | FastAPI service exposing endpoints for product, customer, and sales analytics |
| [`terraform/`](./terraform/) | Infrastructure as code for provisioning GCP resources and GKE clusters |
| [`monitoring/`](./monitoring/) | Observability setup using Prometheus, Grafana, and GCP Cloud Operations |
| [`docs/`](./docs/) | Rendered documentation (e.g. dbt docs, architectural diagrams, OpenAPI schemas) |
| [`scripts/`](./scripts/) | Utility scripts for testing, local development, and data simulation |

---

## 🔍 Project Goals

This repository supports a structured **4-month personal development plan** focused on:

1. **Data Engineering Foundations** – modelling, warehousing, Airflow, BigQuery, CDC
2. **Backend Engineering** – API design, auth, testing, caching, async processing
3. **Software Engineering** – design patterns, system design, Kafka integration, TDD
4. **DevOps & Cloud** – CI/CD, Terraform, Kubernetes, observability

---

## Component-Level Documentation

Each module contains its own `README.md` with implementation-specific details and usage guides:

- 📦 [`dbt/`](./dbt/) – dbt project setup with model definitions.
- ⏱️ [`airflow/`](./airflow/) – DAG definitions, Cosmos setup
- ⚙️ [`api/`](./api/) – FastAPI endpoints, OpenAPI, authentication
- ☁️ [`terraform/`](./terraform/) – GCP provisioning, GKE setup
- 📈 [`monitoring/`](./monitoring/) – Metrics scraping and dashboards

---

## Additional Resources

- **[dbt Documentation](https://docs.getdbt.com/)** – Modelling and transformation
- **[Astronomer Cosmos](https://astronomer.github.io/astronomer-cosmos/)** – Airflow-dbt integration
- **[BigQuery Docs](https://cloud.google.com/bigquery/docs/)** – Serverless warehousing
- **[FastAPI Docs](https://fastapi.tiangolo.com/)** – Modern Python web APIs
- **[Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)** – Infrastructure provisioning

---

## Status

🛠️ **In Progress** – Iteratively built as part of a continuous learning journey. Major components are implemented in phases and tracked via internal planning.

---
