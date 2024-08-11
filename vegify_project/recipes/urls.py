from django.urls import path
from . import views

urlpatterns = [
    path('generate-recipe/', views.recipe_input, name='recipe_input'),
]
