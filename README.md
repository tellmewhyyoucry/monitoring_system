📘 Project Description: Equipment Monitoring System
1. Project Goal

This project is a minimal prototype of an equipment monitoring system, simulating the tasks of an Engineering and Technical Center.
The system allows you to:

upload telemetry data (temperature, pressure) from CSV files,

store the data in a PostgreSQL database,

detect anomalies (e.g., high temperature or sudden pressure spikes),

access data via a REST API,

visualize readings on a chart.

The project demonstrates skills in Python, data processing, API development, and Docker, which are relevant for corporate engineering tasks similar to those at Газпром.

2. Technology Stack

Python 3.11 – main programming language

Pandas – data processing and cleaning

SQLAlchemy + PostgreSQL – data storage

FastAPI – REST API development

Matplotlib – data visualization

Docker + Docker Compose – containerization for easy deployment

Pydantic – data validation

3. Project Structure
monitoring_system/
│
├── app/
│   ├── main.py        # FastAPI server, API routes
│   ├── database.py    # PostgreSQL connection
│   ├── models.py      # Telemetry model
│   ├── anomaly.py     # Anomaly detection
│
├── data/
│   └── telemetry.csv  # Sample sensor data
│
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container build
└── docker-compose.yml # Launch API and database together
