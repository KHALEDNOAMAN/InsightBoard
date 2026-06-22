# InsightBoard - Interactive Data Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chart.js&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **A stunning real-time analytics dashboard with 8 interactive charts, KPI tracking, data tables, and a modern dark-themed UI.**

---

## Overview

InsightBoard is a full-stack data visualization dashboard built with Python, Flask, and Chart.js. It features **8 interactive chart types**, **animated KPI cards**, **real-time data refresh**, and a **premium dark-themed design**. All data is dynamically generated to simulate real analytics.

## Key Features

| Feature | Description |
|---------|-------------|
| **8 Chart Types** | Line, Area, Bar, Doughnut, Polar Area, Radar - all interactive |
| **KPI Cards** | Revenue, Users, Orders, Conversion - with live % change indicators |
| **Revenue Analytics** | 12-month Revenue vs Expenses vs Profit trends |
| **Traffic Analysis** | 30-day visitor and page view tracking |
| **Demographics** | Age group, device split, and geographic distribution |
| **Performance Radar** | Current vs Previous period performance scores |
| **Hourly Activity** | 24-hour user activity heatmap |
| **Products Table** | Top products with sales, revenue, and growth data |
| **Auto-Refresh** | Data updates every 60 seconds |
| **Dark Theme** | Premium glassmorphism dark design |
| **Responsive** | Works on desktop, tablet, and mobile |

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.9+ | Backend data generation and API |
| Flask | Web server and REST API |
| Chart.js 4 | Interactive chart rendering |
| HTML/CSS/JS | Responsive dashboard UI |

## Architecture

```
+---------------------------------------------+
|           InsightBoard Dashboard             |
|  +--------+ +-----------------------------+ |
|  |Sidebar | |  KPI Cards (4x)             | |
|  |  Nav   | |  Revenue Chart  | Category  | |
|  |        | |  Traffic Chart  | Demograph. | |
|  |        | |  Perf. | Hourly | Devices   | |
|  |        | |  Top Products Table         | |
|  +--------+ +------------+----------------+ |
+------------------------|--------------------+
                         | REST API
+------------------------|--------------------+
|              Flask Server                    |
|    +------------------------------------+    |
|    |         Data Generator             |    |
|    |  - KPI metrics   - Revenue data    |    |
|    |  - Traffic data   - Demographics   |    |
|    |  - Performance   - Hourly stats    |    |
|    |  - Product rankings                |    |
|    +------------------------------------+    |
+----------------------------------------------+
```

## Getting Started

### Prerequisites
```bash
Python >= 3.8
```

### Installation and Run
```bash
# Clone the repository
git clone https://github.com/KHALEDNOAMAN/InsightBoard.git
cd InsightBoard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python app.py
```

Then open **http://localhost:5002**

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard UI |
| `/api/data` | GET | All dashboard data |
| `/api/kpi` | GET | KPI metrics only |
| `/api/revenue` | GET | Revenue chart data |
| `/api/traffic` | GET | Traffic chart data |

## Project Structure

```
InsightBoard/
|-- app.py              # Main app (server + data gen + dashboard UI)
|-- requirements.txt    # Python dependencies
|-- LICENSE
+-- README.md
```

## License

This project is licensed under the MIT License.

## Author

**Khaled Noaman** - Computer Engineering Student at Istanbul Arel University

- [GitHub](https://github.com/KhaledNoaman)
- [LinkedIn](https://www.linkedin.com/in/khalednoaman1/)
