from django.shortcuts import render
from whats_cookin.models.recipe import RecipeForm


def index(request):
    form = RecipeForm()
    if request.method == 'POST': 
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
    return render(request, 'submission.html', {'form': form}, locals())

