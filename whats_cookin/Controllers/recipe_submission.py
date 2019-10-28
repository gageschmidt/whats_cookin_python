from django.shortcuts import render
from whats_cookin.Models.recipe_form import RecipeForm


def index(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        print(form)
    return render(request, 'recipe_submission.html', {'form': form}, locals())

