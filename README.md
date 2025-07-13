# 🏥 Ethiopian Medical Business Insights – ELT Data Platform

This project builds a robust, end-to-end data platform for analyzing Ethiopian medical businesses using data scraped from public **Telegram channels**. The pipeline follows a modern **ELT architecture**, transforming raw data into valuable insights.

---

## 🚀 Project Goals

Answer key business questions like:

- 📌 What are the **top 10 most frequently mentioned medical products or drugs**?
- 🏷️ How does **product pricing or availability vary** across Telegram channels?
- 🖼️ Which channels have the most **visual content** (e.g., pills vs. creams)?
- 📈 What are the **daily/weekly trends** in health-related posts?

---

## 📦 Tech Stack

| Layer              | Tool / Technology        |
|-------------------|--------------------------|
| Data Extraction    | [Telethon](https://github.com/LonamiWebs/Telethon)            |
| Object Detection   | YOLO (via PyTorch)       |
| Data Lake Storage  | Raw JSON Files           |
| Data Warehouse     | PostgreSQL               |
| Transformation     | dbt                      |
| API Layer          | FastAPI                  |
| Containerization   | Docker, docker-compose   |
| CI/CD              | GitHub Actions           |

---

## 📁 Project Structure

