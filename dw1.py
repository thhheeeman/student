# 1. Import Libraries
import pandas as pd
import numpy as np

# 2. Load Dataset
df = pd.read_csv("dw1.csv")   # change file name if needed

# 3. Display Data
print("First 5 rows:")
df.head()

print("\nLast 5 rows:")
df.tail()

# 4. Dataset Info
print("\nDataset Info:")
df.info()

print("\nShape of dataset:")
df.shape

# 5. Missing Values
print("\nMissing Values:")
df.isnull().sum()


print("\nStatistical Summary:")
df.describe()

# 7. Data Types
print("\nData Types:")
df.dtypes

# 8. Convert Data Types (Example)
if 'Duration' in df.columns:
    df['Duration'] = df['Duration'].astype(float)

# 9. Handle Missing Values
df = df.dropna()   # simple method
df['Subject 3'] = df['Subject 3'].fillna(df['Subject 3'].mean())

print("\nAfter removing missing values:")
df.isnull().sum()

# 10. Convert Categorical to Numeric
df = pd.get_dummies(df, drop_first=True)

print("\nAfter converting categorical variables:")
df.head()