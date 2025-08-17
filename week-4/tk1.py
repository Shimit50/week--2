# model_train.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample data
data = {
    'hours_studied': [10, 15, 20, 25, 30, 5, 12, 18],
    'attendance': [80, 90, 75, 95, 100, 60, 85, 70],
    'assignments': [5, 8, 6, 10, 9, 3, 7, 4],
    'score': [65, 80, 70, 90, 95, 50, 75, 60]
}

df = pd.DataFrame(data)

# Train model
X = df[['hours_studied', 'attendance', 'assignments']]
y = df['score']
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model/student_performance_model.joblib')

# Test prediction
test_input = [[15, 85, 7]]
print(f"Test prediction: {model.predict(test_input)[0]}")