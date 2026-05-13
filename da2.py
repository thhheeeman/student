# 🔹 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# 🔹 2. Load Dataset

df = pd.read_csv("da2.csv")

print("First 5 Rows:")
df.head()

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
df.describe()


# 🔹 3. Data Preprocessing

# Remove unnecessary columns
df.drop(['User ID'], axis=1, inplace=True)
df.drop(['Gender'], axis=1, inplace=True)

# Define X and y
X = df.drop('Purchased', axis=1)
y = df['Purchased']


# 🔹 4. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# 🔹 5. Feature Scaling

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# 🔹 6. Create Logistic Regression Model

model = LogisticRegression()

# Train model
model.fit(X_train, y_train)


# 🔹 7. Prediction

y_pred = model.predict(X_test)

print("\nPredicted Values:")
y_pred


# 🔹 8. Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
cm


# Extract values
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("\nTP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)


# 🔹 9. Performance Metrics

accuracy = accuracy_score(y_test, y_pred)

error_rate = 1 - accuracy

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

print("\nAccuracy =", accuracy)

print("Error Rate =", error_rate)

print("Precision =", precision)

print("Recall =", recall)
