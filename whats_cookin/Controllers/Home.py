from django.shortcuts import render
from whats_cookin.Models import Elasticsearch


def index(request):
    Elasticsearch.index_single_document(),
    return render(request, 'home.html', locals())
