import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

df = pd.read_csv("Telco-Customer-Churn.csv")
pd.set_option('display.max_columns', None)

print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Data Cleaning
# Convert TotalCharges to numeric (some blank spaces cause errors)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])

print("\nMissing Values per Column:")
print(df.isnull().sum())

# Churn Distribution
print("\nChurn Value Counts:")
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True))

plt.figure(figsize=(5,4))
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()

# Numeric Columns Summary
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print("\nNumeric Column Statistics:")
print(df[numeric_cols].agg(['mean', 'median', 'std']))

# Categorical Feature Frequencies
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
for col in cat_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts(normalize=True).round(2))

# Statistical Tests
# Chi-square for Gender vs Churn
table = pd.crosstab(df['gender'], df['Churn'])
chi2, p, dof, expected = chi2_contingency(table)
print("\nChi-square test (Gender vs Churn) p-value =", p)
print("Churn is related to Gender" if p < 0.05 else "Churn is NOT related to Gender")

# Chi-square for Contract vs Churn
table = pd.crosstab(df['Contract'], df['Churn'])
chi2, p, dof, expected = chi2_contingency(table)
print("Chi-square test (Contract vs Churn) p-value =", p)
print("Churn is related to Contract Type" if p < 0.05 else "Churn is NOT related to Contract Type")

# T-test for Monthly Charges
yes_churn = df[df['Churn'] == 'Yes']['MonthlyCharges']
no_churn = df[df['Churn'] == 'No']['MonthlyCharges']
t_stat, p = ttest_ind(yes_churn, no_churn)
print("\nT-test (MonthlyCharges) p-value =", p)
print("Monthly Charges differ between churned & non-churned customers" if p < 0.05 else "Monthly Charges are similar")

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[num_cols].hist(bins=30, figsize=(10,4))
plt.suptitle("Numeric Features Distribution")
plt.show()

# Churn vs Numeric Features
for col in num_cols:
    plt.figure(figsize=(5,4))
    sns.boxplot(x='Churn', y=col, data=df)
    plt.title(f"{col} vs Churn")
    plt.show()

# Categorical Features vs Churn
cat_cols.remove('customerID')
cat_cols.remove('Churn')
for col in cat_cols:
    plt.figure(figsize=(5,4))
    sns.countplot(x=col, hue='Churn', data=df)
    plt.title(f"{col} vs Churn")
    plt.xticks(rotation=45)
    plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Numeric Feature Correlation")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

