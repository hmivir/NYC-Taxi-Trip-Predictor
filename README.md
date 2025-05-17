## NYC Taxi Trip Predictor
A full-stack machine learning system to predict taxi fare price and trip duration in New York City using historical trip data.

Built to empower riders and drivers with real-time insights for smarter, cost-effective travel.

## 🚀 Motivation
**For riders:**

Transparent pricing before the trip starts
Better planning and time management

**For drivers:**

Optimized routing and pricing strategies
Customer behavior insights

## 🎯 Project Objective
**Develop a real-time predictive model for:**

🕒 Trip duration (in seconds)
💵 Fare amount (USD)

**Using features available at the start of the trip:**
Pickup & dropoff location
Distance
Date & time
Passenger count
Rate type (e.g., airport rate)

## 🧠 Key Features
🔄 Automated data pipeline (raw to clean)
📊 Exploratory Data Analysis (Jupyter)
⚙️ ML Models: XGBoost, RandomForest, Linear Regression
🌐 REST API using FastAPI
🐳 Fully containerized with Docker
🧪 Testing scripts and modularized code
📍 Optional: Neighborhood and demand mapping

## 📦 Dataset Overview

Source: NYC Taxi and Limousine Commission Open Data [2018–2025]
Used sample: ~3.5 million rows from May 2022
Key columns:
    pickup_datetime, dropoff_datetime
    trip_distance, fare_amount
    payment_type, passenger_count

## 🔧 Data issues and solutions
Issue	Solution
Missing values	Cleaning & filtering
Temporal inconsistencies	Timestamp validation
Location IDs only (no lat/lon)	Used GeoJSON with neighborhood polygons
Sparse location data	Dropped or grouped into broader zones

## Project Structure
```
nyc-taxi-predictor/
├── .gitignore
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── predictions.py
│   └── schemas/
│       ├── __init__.py
│       └── prediction.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── download_data.py
├── notebooks/
│   ├── 01_initial_data_exploration.ipynb
│   └── 02_feature_engineering.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── feature_engineering.py
│   └── models/
│       ├── __init__.py
│       └── predictor.py
└── tests/
    └── __init__.py 
```

## 🔍 EDA Highlights
Temporal patterns: fare and duration vary by hour/day
Trip distribution visualized with heatmaps (pickup/dropoff)
Feature engineering: rush hour, weekend flag, rate codes, zones
Correlation analysis between distance and fare/duration

## 🧪 Model Training & Evaluation
| Target        | Best Model        | MAE       | Notes                         |
| ------------- | ----------------- | --------- | ----------------------------- |
| Trip Duration | XGBoost           | \~230 sec | Good on outliers              |
| Fare Amount   | Linear Regression | \~\$1.97  | Simple, robust, interpretable |


Trained on May 2022 sample for faster iteration
80/20 train-test split
Optional grid search & XGBoost tuning

## 📡 API Usage
**Once Docker is running:**
    Main URL: http://localhost:8000
    Docs (Swagger): http://localhost:8000/docs
    Health check: http://localhost:8000/health
    Jupyter: http://localhost:8888 (token: taxi)

## 🐳 Run with Docker
**Run entire system**
docker-compose up --build

**Run specific service**
docker-compose up api
docker-compose up notebook

## 🚧 Challenges
Irregularities and outliers in trip data
Geolocation mapping via neighborhood zones
Data volume → required downsampling for local modeling
Prediction drift for extreme cases (long trips, heavy traffic)

## 🔭 Next Steps
🌦 Add weather and traffic data (e.g., OpenWeather API)
📈 Expand to predict taxi demand by region and hour
☁️ Deploy on cloud (GCP/AWS)
📱 Build interactive dashboard with Streamlit


## 👨‍💻 About the Author
**Héctor Maximiliano Ivir**
PhD in Biochemistry · Machine Learning Engineer · Data Science in Biotech
https://www.linkedin.com/in/hmivir/

## 🤝 Contributions Welcome
Want to extend this project for your city or use case?
Fork the repo
Create a new branch: git checkout -b feature/name
Commit your changes: git commit -m "Add feature"
Push: git push origin feature/name
Open a Pull Request 🚀