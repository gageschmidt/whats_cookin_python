from django.shortcuts import render
from whats_cookin.models import elasticsearch
from whats_cookin.forms.recipe import RecipeForm


def index(request):
    form = RecipeForm()
    if request.method == 'POST': 
        form = RecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            ingredients = form.cleaned_data['ingredients']
            directions = form.cleaned_data['directions']
            elasticsearch.index_recipe(name, ingredients, directions)
    return render(request, 'submission.html', {'form': form}, locals())

