import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model and vectorizer
with open('ml/recipe_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('ml/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def generate_recipe(ingredients):
    """
    Generate a recipe based on the input ingredients.
    :param ingredients: List of ingredients provided by the user.
    :return: Predicted recipe.
    """
    # Preprocess ingredients
    ingredients_str = ' '.join(ingredients)
    ingredients_vector = vectorizer.transform([ingredients_str])

    # Predict the recipe
    recipe_index = model.kneighbors(ingredients_vector, return_distance=False)[0][0]
    return f"Recipe {recipe_index + 1}: {ingredients_str}"
