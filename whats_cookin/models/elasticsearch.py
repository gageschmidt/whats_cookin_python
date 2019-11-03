from elasticsearch import Elasticsearch
from datetime import datetime

elasticsearch = Elasticsearch()


def check_ids():
    if check_if_index_exists() is False:
        elasticsearch.create(index='recipes', id=1, body='first')
    indices = elasticsearch.get('recipes', '*')
    return indices.count()


def index_recipe(name, ingredients, directions):
    document = {
        'name': name,
        'ingredients': ingredients,
        'directions': directions,
        'timestamp': datetime.now()
    }
    elasticsearch.index(index='recipes', id=1, body=document)


def check_if_index_exists():
    return elasticsearch.exists('recipes', '*', '*')

def get_homepage_recipe():
    #will be random
    return elasticsearch.get('recipes', '1')

