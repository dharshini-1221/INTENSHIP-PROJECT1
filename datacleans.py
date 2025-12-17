

import pandas as pd
import numpy as np
df = pd.read_csv("NewCompanyDetails.csv")
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
df['revenue'] = df['revenue'].astype(str)
df['revenue'] = df['revenue'].str.replace("million", "", case=False, regex=True)
df['revenue'] = df['revenue'].str.strip()
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['revenue'] = df['revenue'] * 1_000_000
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)
df = df[df['revenue'] > 0]
df.to_csv("Cleaned_NewCompanyDetails.csv", index=False)

print(" Revenue cleaned and Power BI ready")
