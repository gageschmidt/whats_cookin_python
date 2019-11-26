from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from whats_cookin.models import elasticsearch
from whats_cookin.models import scrape


def index(request):
    staticfiles_urlpatterns()
    if elasticsearch.count_current_indices() > 0:
        recipe = elasticsearch.get_homepage_recipe()
        name = recipe['name']
        ingredients = recipe['ingredients']
        directions = recipe['directions']
    data = scrape.parse()
    return render(request, 'home.html', locals())

