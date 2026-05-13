# 🔹 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 🔹 2. Create Academic Performance Dataset

data = {
    'Student' : ['Om','Atharva','Blaise','Swayam','Tanmay','Sarthak'],

    'Subject 1' : [75,80,np.nan,150,90,85],

    'Subject 2' : [-10,70,85,75,np.nan,95],

    'Subject 3' : [60,np.nan,78,82,170,88],

    'Subject 4' : [85,90,np.nan,40,92,80],

    'Attendance' : [85,90,95,-20,88,92],

    'Percentage' : [78,82,89,45,96,84],

    'Grade' : ['B','A','A+',np.nan,'A+','A']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 🔹 3. Check Dataset Information

print("\nDataset Info:")
print(df.info())

print("\nShape of Dataset:")
print(df.shape)


# 🔹 4. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())


# 🔹 5. Handle Missing Values

# Fill missing numeric values with mean
df['Subject 1'] = df['Subject 1'].fillna(df['Subject 1'].mean())

df['Subject 2'] = df['Subject 2'].fillna(df['Subject 2'].mean())

df['Subject 3'] = df['Subject 3'].fillna(df['Subject 3'].mean())

df['Subject 4'] = df['Subject 4'].fillna(df['Subject 4'].mean())


# Fill missing categorical value
df['Grade'] = df['Grade'].fillna('B')


# 🔹 6. Handle Inconsistencies

# Convert negative values into positive
df['Subject 2'] = abs(df['Subject 2'])

df['Attendance'] = abs(df['Attendance'])


print("\nAfter Handling Missing Values:")
print(df)


# 🔹 7. Boxplot for Outlier Detection

df.boxplot(figsize=(10,6))

plt.title("Boxplot of Numeric Columns")

plt.show()


# 🔹 8. Remove Outliers using IQR Method

cols = ['Subject 1','Subject 2','Subject 3',
        'Subject 4','Attendance','Percentage']

for col in cols:

    Q1 = df[col].quantile(0.25)

    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR

    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]


print("\nAfter Removing Outliers:")
print(df)


# 🔹 9. Data Transformation

# Log Transformation
df['Subject1_log'] = np.log(df['Subject 1'] + 1)


# Min-Max Scaling
df['Attendance_scaled'] = (
    (df['Attendance'] - df['Attendance'].min()) /
    (df['Attendance'].max() - df['Attendance'].min())
)


# 🔹 10. Final Dataset

print("\nFinal Dataset:")
print(df)

print("\nFinal Missing Values:")
print(df.isnull().sum())
