# 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Load dataset
df = sns.load_dataset('iris')

# 3. Display dataset
print("First 5 rows:")
print(df.head())

# 4. Feature names and types
print("\nFeatures and Data Types:")
print(df.dtypes)

# 5. Histogram for all features
df.hist(bins=20, figsize=(10, 8))
plt.suptitle("Histogram of Iris Features")
plt.show()

# 6. Boxplot for all features
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("Boxplot of Iris Features")
plt.show()


sns.pairplot(df)
plt.show()