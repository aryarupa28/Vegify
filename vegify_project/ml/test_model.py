import joblib
import os

# Ensure you're running the script from the right directory
script_dir = os.path.dirname(__file__)

# Load the saved model and vectorizer
model_path = os.path.join(script_dir, 'recipe_model.pkl')
vectorizer_path = os.path.join(script_dir, 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Example ingredients for prediction
ingredients = ["chicken, rice, soy sauce", "tomato, cheese, dough"]

# Transform the ingredients using the loaded vectorizer
X = vectorizer.transform(ingredients)

# Predict using the loaded model
predictions = model.predict(X)
print("Predictions:")
for ing, pred in zip(ingredients, predictions):
    print(f'Ingredients: {ing} => Recipe: {pred}')
