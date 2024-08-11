from django import forms

class IngredientForm(forms.Form):
    ingredient = forms.CharField(label='Ingredient', max_length=100)
    quantity = forms.FloatField(label='Quantity')