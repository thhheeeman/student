# 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Load Titanic dataset
df = sns.load_dataset('titanic')

# 3. Display dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# 4. Basic Visualization

# (a) Bar plot: sex vs age
sns.barplot(x='sex', y='age', data=df)
plt.title("Average Age of Male and Female")
plt.show()

# (b) Count plot: survival count
sns.countplot(x='survived', data=df)
plt.title("Survival Count")
plt.show()

# (c) Count plot: survival based on gender
sns.countplot(x='sex', hue='survived', data=df)
plt.title("Survival based on Gender")
plt.show()

# 5. Histogram of fare (IMPORTANT for assignment)
sns.histplot(df['fare'])
plt.title("Distribution of Ticket Fare")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

# Optional (as shown in your PDF - binwidth)
sns.histplot(df['fare'], bins=30)
plt.title("Fare Distribution with Bins")
plt.show()