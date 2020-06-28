import random

from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient('mongodb://127.0.0.1:27017/')

    @staticmethod
    def get_homepage_recipe():
        connection = Connect.get_connection()
        db = connection.test
        recipe_id = random.randint(1, db['recipes'].count_documents({}))
        recipe = db['recipes'].find_one({'id': recipe_id}, {'_id': False})
        name = recipe['name']
        ingredients = recipe['ingredients']
        directions = recipe['directions']
        recipe = {
            'name': name,
            'ingredients': ingredients,
            'directions': directions
        }
        return recipe
