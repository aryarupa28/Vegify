import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load your data
data = pd.read_csv('ml/recipes_data.csv')

# Check if data is loaded correctly
print("Data Sample:")
print(data.head())

# Preprocess data
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X = vectorizer.fit_transform(data['ingredients'])
y = data['recipe_name']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = KNeighborsClassifier(n_neighbors=min(5, X_train.shape[0]))
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(model, 'ml/recipe_model.pkl')
joblib.dump(vectorizer, 'ml/vectorizer.pkl')

print("Model and vectorizer saved successfully.")
