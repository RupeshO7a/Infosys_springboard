# train_model.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset [cite: 10, 11]
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Initialize and train the Random Forest model [cite: 12]
# We use a simple configuration for this example.
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("Model trained successfully!")

# Save the trained model to a file [cite: 13]
joblib.dump(model, 'model.joblib')
print("Model saved to model.joblib")

# Also save the target names for later use in the app
target_names = iris.target_names
joblib.dump(target_names, 'target_names.joblib')
print("Target names saved to target_names.joblib")