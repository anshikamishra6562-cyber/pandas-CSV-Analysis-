import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Filter employees with Salary > 50000
high_salary_df = df[df["Salary"] > 50000]
print("\nEmployees with Salary > 50000:")
print(high_salary_df)

# Save filtered data
high_salary_df.to_csv("high_salary_employees.csv", index=False)
print("\nFiltered file saved as 'high_salary_employees.csv'")


