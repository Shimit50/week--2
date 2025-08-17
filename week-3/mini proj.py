import joblib

# Create custom dataset (or use your existing one)
data = {
    'attendance': [90, 85, 70, 95, 80],
    'participation': [8, 7, 5, 9, 6],
    'final_score': [88, 82, 65, 95, 75]
}
project_df = pd.DataFrame(data)

# Train model
X = project_df[['attendance', 'participation']]
y = project_df['final_score']
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'student_score_predictor.pkl')

# Example prediction
new_data = [[85, 7]]  # attendance 85%, participation 7
prediction = model.predict(new_data)
print(f"Predicted score: {prediction[0]:.1f}")