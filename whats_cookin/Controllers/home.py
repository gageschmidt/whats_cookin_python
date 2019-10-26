from django.shortcuts import render
from whats_cookin.Models import elasticsearch
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def index(request):
    staticfiles_urlpatterns()
    response = elasticsearch.index_single_document()
    return render(request, 'home.html', locals())
