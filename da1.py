# 🔹 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# 🔹 2. Load Dataset

df = pd.read_csv("da1.csv")

print("First 5 Rows:")
df.head()

print("Shape of Dataset:")
df.shape

print("Dataset Info:")
df.info()


# 🔹 3. Data Preprocessing

print("\nMissing Values:")
df.isnull().sum()

# Fill missing values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Statistical summary
print("\nStatistical Summary:")
df.describe()


# 🔹 4. Data Visualization

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# 🔹 5. Create Linear Regression Model

# X = input features
X = df.drop('MEDV', axis=1)

# y = target/output
y = df['MEDV']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)


# 🔹 6. Prediction

y_pred = model.predict(X_test)

print("\nPredicted Values:")
y_pred[:5]


# 🔹 7. Model Evaluation

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE :", rmse)
print("R2 Score :", r2)


# 🔹 8. Actual vs Predicted Graph

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")

plt.show()
