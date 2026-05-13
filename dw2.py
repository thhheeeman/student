# 🔹 1. Load and Understand Dataset

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dw2.csv")

# Display data
print("First 5 rows:")
df.head()

# Structure
print("\nDataset Info:")
df.info()

print("\nShape:")
df.shape


# 🔹 2. Handle Missing Values & Inconsistencies

print("\nMissing Values:")
df.isnull().sum()

# Fill missing values using mean
df['Subject 3'] = df['Subject 3'].fillna(df['Subject 3'].mean())
df['Subject 4'] = df['Subject 4'].fillna(df['Subject 4'].mean())

# Fix negative value
df['Attendance'] = df['Attendance'].apply(lambda x: abs(x))

print("\nAfter Handling Missing Values:")
print(df.isnull().sum())


# 🔹 3. Detect and Handle Outliers (IQR Method)

cols = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Attendance']

for col in cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Remove outliers
    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("\nAfter Removing Outliers:")
df.shape


# 🔹 4. Apply Data Transformation

# Log Transformation (reduce skewness)
df['Subject1_log'] = np.log(df['Subject 1'] + 1)

# Min-Max Scaling (0 to 1)
df['Attendance_scaled'] = (df['Attendance'] - df['Attendance'].min()) / 
                          (df['Attendance'].max() - df['Attendance'].min())


# 🔹 5. Final Dataset Check

print("\nFinal Dataset:")
df.head()

print("\nFinal Missing Values:")
df.isnull().sum()