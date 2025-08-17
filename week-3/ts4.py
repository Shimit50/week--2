from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Create pass/fail column (assuming 60 is passing)
df['passed'] = np.where(df['average'] >= 60, 1, 0)

# Prepare data
X = df[['hours_studied', 'math_score', 'science_score']]
y = df['passed']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "K-NN": KNeighborsClassifier()
}

# Train and evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"{name} - Accuracy: {acc:.2f}")
    print(f"Confusion Matrix:\n{cm}\n")