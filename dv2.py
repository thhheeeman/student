# 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Load dataset
df = sns.load_dataset('titanic')

# 3. Display dataset
print(df.head())

# 4. Boxplot (IMPORTANT)
sns.boxplot(x='sex', y='age', data=df, hue='survived')

# 5. Labels and title
plt.title("Distribution of Age by Gender and Survival Status")
plt.xlabel("Gender")
plt.ylabel("Age")

# 6. Show plot
plt.show()
