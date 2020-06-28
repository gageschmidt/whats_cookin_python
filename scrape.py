from bs4 import BeautifulSoup
from whats_cookin.models.mongo import Connect
import random
import re
import time
import urllib.error
import urllib.request


def check_recipe_url(recipe_url):
    try:
        urllib.request.urlopen(recipe_url)
    except urllib.error.HTTPError:
        time.sleep(3)
        check_recipe_url(recipe_url)
    else:
        recipe_data = BeautifulSoup(urllib.request.urlopen(recipe_url), 'html.parser')
        return recipe_data


def get_recipe_data(data):
    i = 0
    for text in data:
        data[i] = text.get_text()
        i += 1
    return data


def scrape():
    recipe_url = 'https://www.allrecipes.com/recipe/2' + str(random.randint(00000, 99999))
    recipe = check_recipe_url(recipe_url)
    return recipe


def parse():
    data = scrape()
    ingredients = data.find_all('span', {'class': 'recipe-ingred_txt added'})
    ingredients = get_recipe_data(ingredients)
    directions = data.find_all('span', {'class': 'recipe-directions__list--item'})
    directions = get_recipe_data(directions)
    title = data.find('title')
    title = re.sub(r'- Allrecipes\.com', ' ', title.get_text())
    recipe = {
        'title': title,
        'ingredients': ingredients,
        'directions': directions
    }
    return recipe


def mongo_index_recipe():
    connection = Connect.get_connection()
    db = connection.test
    recipe = parse()
    name = recipe['title']
    ingredients = recipe['ingredients']
    directions = recipe['directions']
    recipe_id = db['recipes'].count() + 1
    db.recipes.insert_one({
        'id': recipe_id,
        'name': name,
        'ingredients': ingredients,
        'directions': directions
    })


if __name__ == '__main__':
    mongo_index_recipe()

