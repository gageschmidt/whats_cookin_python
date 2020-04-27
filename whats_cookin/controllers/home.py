from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from whats_cookin.models.mongo import Connect


def index(request):
    staticfiles_urlpatterns()
    connection = Connect.get_connection()
    db = connection.test
    check_for_indices = db['recipes'].count()
    if check_for_indices > 0:
        recipe = Connect.get_homepage_recipe()
        name = recipe['name']
        ingredients = recipe['ingredients']
        directions = recipe['directions']
        return JsonResponse({
            'name': name,
            'ingredients': ingredients,
            'directions': directions
        })
    else:
        return JsonResponse({
            'nothing today :('
        })
