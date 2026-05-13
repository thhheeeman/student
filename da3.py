# 🔹 1. Import Libraries

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# 🔹 2. Load Dataset

df = pd.read_csv("da3.csv")

print("First 5 Rows:")
df.head()

print("\nDataset Info:")
df.info()


# 🔹 3. Define X and y

X = df.drop('species', axis=1)

y = df['species']


# 🔹 4. Feature Scaling

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)


# 🔹 5. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=10
)


# 🔹 6. Create Naive Bayes Model

model = GaussianNB()

# Train model
model.fit(X_train, y_train)


# 🔹 7. Prediction

y_pred = model.predict(X_test)

print("\nPredicted Values:")
y_pred


# 🔹 8. Confusion Matrix

labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

cm = confusion_matrix(y_test, y_pred, labels=labels)

print("\nConfusion Matrix:")
cm


# 🔹 9. Performance Metrics

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average='macro'
)

recall = recall_score(
    y_test,
    y_pred,
    average='macro'
)

error_rate = 1 - accuracy

print("\nAccuracy =", accuracy)

print("Error Rate =", error_rate)

print("Precision =", precision)

print("Recall =", recall) 
