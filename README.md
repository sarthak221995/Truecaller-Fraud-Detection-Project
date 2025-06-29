# Truecaller Fraud Detection Project

## Overview
This project aims to detect fraudulent users on a communication platform using advanced anomaly detection techniques. The solution leverages both classical machine learning (Isolation Forest) and deep learning (Autoencoder) models, along with extensive feature engineering and data analysis.

## Table of Contents
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Feature Engineering](#feature-engineering)
- [Modeling Approach](#modeling-approach)
- [Analysis & Visualization](#analysis--visualization)
- [Scalability & Future Work](#scalability--future-work)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Contact](#contact)

## Project Structure
```
truecaller_assignment/
├── config.py
├── data/
│   ├── call_data.csv
│   ├── message_data.csv
│   ├── search_data.csv
│   └── signup_data.csv
├── notebooks/
│   ├── eda.ipynb
│   ├── all.ipynb
│   └── data_analysis.ipynb
├── docs/
├── ...
```

## Data Sources
- **Call, Message, Search, Signup Data:** Raw user activity logs in CSV format.
- **Feature Engineered Data:** Processed features for modeling.

## Feature Engineering
- Activity counts, rates, and spans
- Search-to-communication ratio
- Immediate activity after signup
- Activity concentration
- Temporal and interval features

## Modeling Approach
- **Isolation Forest:** Fast, interpretable anomaly detection for tabular data.
- **Autoencoder:** Deep learning model to capture complex, non-linear user behaviors.
- **Ensemble:** Combines multiple models (Isolation Forest, DBSCAN, Local Outlier Factor, Autoencoder) for robust detection.

## Analysis & Visualization
- Exploratory data analysis and feature statistics
- Visualizations of user activity, anomaly distribution, and country-wise patterns
- Comparative analysis of normal vs. anomalous users

## Scalability & Future Work
- Models can be distributed using Spark, Dask, or TensorFlow for 100M+ users
- Future directions: graph-based detection, temporal models, explainable AI, and real-time streaming

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Update `config.py` with correct data paths
3. Run notebooks in `notebooks/` for EDA, modeling, and analysis

## Requirements
- Python 3.8+
- pandas, numpy, scikit-learn, matplotlib, seaborn, torch, etc. (see `requirements.txt`)

## Contact
For questions or collaboration, contact the project maintainer.
