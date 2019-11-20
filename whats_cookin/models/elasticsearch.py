from datetime import datetime
from elasticsearch import Elasticsearch
import random

elasticsearch = Elasticsearch()


def index_recipe(name, ingredients, directions):
    document = {
        'name': name,
        'ingredients': ingredients,
        'directions': directions,
        'timestamp': datetime.now()
    }
    count = count_current_indices()
    elasticsearch.index(index='recipes', id=count + 1, body=document)


def get_homepage_recipe():
    recipe_id = random.randint(1, count_current_indices())
    recipe = elasticsearch.get('recipes', recipe_id)
    name = recipe['_source']['name']
    ingredients = recipe['_source']['ingredients']
    directions = recipe['_source']['directions']
    recipe = {
        'name': name,
        'ingredients': ingredients,
        'directions': directions
    }
    return recipe


def count_current_indices():
    indices = elasticsearch.search('recipes')
    total = indices['hits']['total']['value']
    return total
