import pandas as pd
import numpy as np

# Load dataset (replace with your actual file)
df = pd.read_csv('student_scores.csv')

# Preview data
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df = df.dropna()  # or df.fillna(method='ffill')

# Create derived columns
df['total'] = df['math_score'] + df['science_score'] + df['english_score']
df['average'] = df['total'] / 3