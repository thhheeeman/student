# Import library
import pandas as pd

# ---------------- PART 1 ----------------

# Load dataset
df = pd.read_csv("stat.csv")   # your dataset

print("First 5 rows:")
print(df.head())

# Group by categorical column (income) and numeric column (age)
print("\nSummary Statistics (Grouped by income):")
print(df.groupby("income")["age"].describe())

# Individual statistics
print("\nMean:")
print(df.groupby("income")["age"].mean())

print("\nMedian:")
print(df.groupby("income")["age"].median())

print("\nMin:")
print(df.groupby("income")["age"].min())

print("\nMax:")
print(df.groupby("income")["age"].max())

print("\nStandard Deviation:")
print(df.groupby("income")["age"].std())

# List of values for each category
value_list = df.groupby("income")["age"].apply(list)
print("\nList of values:")
print(value_list)


# ---------------- PART 2 ----------------

# Load Iris dataset
iris = pd.read_csv("Iris.csv")

# Iris-setosa
print("\nIris-setosa")
print(iris[iris["Species"] == "Iris-setosa"].describe())

# Iris-versicolor
print("\nIris-versicolor")
print(iris[iris["Species"] == "Iris-versicolor"].describe())

# Iris-virginica
print("\nIris-virginica")
print(iris[iris["Species"] == "Iris-virginica"].describe())
