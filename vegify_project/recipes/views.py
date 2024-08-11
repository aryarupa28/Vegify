from django.shortcuts import render
from .forms import IngredientForm
from vegify_project.ml.generate_recipe import generate_recipe

def recipe_input(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data['ingredient']
            quantity = form.cleaned_data['quantity']

            # Prepare the input for the model
            ingredients = [f"{quantity} {ingredient}"]

            # Call the AI model function to generate a recipe
            recipe = generate_recipe(ingredients)

            # Render the output to the template
            return render(request, 'recipe_output.html', {'recipe': recipe})
    else:
        form = IngredientForm()

    return render(request, 'recipe_input.html', {'form': form})
