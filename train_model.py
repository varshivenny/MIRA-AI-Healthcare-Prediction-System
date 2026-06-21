import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df=pd.read_csv(
"data/health_data.csv"
)


X=df[
[
"glucose",
"haemoglobin",
"cholesterol"
]
]

y=df["risk"]


X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.2,
random_state=42
)


model=RandomForestClassifier(
n_estimators=200,
random_state=42
)


model.fit(
X_train,
y_train
)


prediction=model.predict(
X_test
)


accuracy=accuracy_score(
y_test,
prediction
)


os.makedirs(
"models",
exist_ok=True
)


joblib.dump(
model,
"models/health_model.pkl"
)


print(
"AI Model Created"
)


print(
"Accuracy:",
accuracy
)