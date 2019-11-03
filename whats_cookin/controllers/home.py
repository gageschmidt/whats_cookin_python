from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from whats_cookin.models import elasticsearch


def index(request):
    staticfiles_urlpatterns()
    recipe = elasticsearch.get_homepage_recipe()
    name = recipe['_source']['name']
    ingredients = recipe['_source']['ingredients']
    directions = recipe['_source']['directions']
    return render(request, 'home.html', locals())
