from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from whats_cookin.models import elasticsearch


def index(request):
    staticfiles_urlpatterns()
    try:
        check_for_indices = elasticsearch.count_current_indices()
        if check_for_indices > 0:
            recipe = elasticsearch.get_homepage_recipe()
            name = recipe['name']
            ingredients = recipe['ingredients']
            directions = recipe['directions']
        return render(request, 'home.html', locals())
    finally:
        return render(request, 'home.html', locals())

