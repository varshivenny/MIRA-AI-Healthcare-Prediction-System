# MIRA-AI-Healthcare-Prediction-System
AI-powered healthcare prediction application using Python, Streamlit, Machine Learning, and SQLite with patient CRUD management, analytics dashboard, and intelligent health risk prediction.

## Overview

MIRA AI predicts patient health risk using blood test parameters and provides AI-generated medical remarks.

## Features

- Patient CRUD Management
- Machine Learning Prediction
- AI Generated Health Remarks
- SQLite Database Storage
- Analytics Dashboard
- Patient Search
- Report Download
- Secure Admin Access


## Technology Stack

- Python
- Streamlit
- Scikit-Learn
- Random Forest Classifier
- SQLite
- Pandas
- Plotly


## ML Inputs

- Glucose Level
- Haemoglobin Level
- Cholesterol Level


## Prediction Output

- Healthy
- Medium Risk
- High Risk


## Project Structure
```
MIRA_AI_Healthcare/

│
├── app.py
├── database.py
├── ml_model.py
├── train_model.py
├── validation.py
│
├── models/
│     └── health_model.pkl
│
├── data/
│     └── health_data.csv
│
├── database/
│     └── mira.db
│
├── requirements.txt
├── README.md
└── .gitignore
```


## How to Run

Install dependencies:

pip install -r requirements.txt


Train model:

python train_model.py


Run application:

streamlit run app.py

http://localhost:8501

Output :

<img width="1907" height="770" alt="image" src="https://github.com/user-attachments/assets/356c679c-bf85-4b14-afb7-edfbb7f508db" />
<img width="1410" height="676" alt="image" src="https://github.com/user-attachments/assets/d833a8d7-8c2c-47b1-949e-eb5cd309336f" />
<img width="1417" height="797" alt="image" src="https://github.com/user-attachments/assets/0c988393-0d22-4a3d-ad32-475b9e625ed9" />
<img width="1422" height="718" alt="image" src="https://github.com/user-attachments/assets/8dae677f-ff1b-45de-b503-7a953313ecbf" />
<img width="1371" height="677" alt="image" src="https://github.com/user-attachments/assets/77e8f806-a990-4833-af91-b55d6cd0451e" />



## Developer

Korivi Varshitha
