from django.shortcuts import render
from whats_cookin.Models import Elasticsearch
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def index(request):
    staticfiles_urlpatterns()
    response = Elasticsearch.index_single_document()
    return render(request, 'home.html', locals())
