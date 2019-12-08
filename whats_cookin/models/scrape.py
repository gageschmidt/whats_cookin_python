from bs4 import BeautifulSoup
import random
import re
import socket
import time
import urllib.error
import urllib.request


def parse():
    data = scrape()
    ingredients = data.find_all('span', {'class': 'recipe-ingred_txt added'})
    ingredients = get_recipe_data(ingredients)
    directions = data.find_all('span', {'class': 'recipe-directions__list--item'})
    directions = get_recipe_data(directions)
    title = data.find('title')
    title = re.sub(r'- Allrecipes\.com', ' ', title.get_text())
    recipe = [title, ingredients, directions]
    return recipe


def scrape():
    recipe_url = 'https://www.allrecipes.com/recipe/2' + str(random.randint(00000, 99999))
    recipe = check_recipe_url(recipe_url)
    return recipe


def check_recipe_url(recipe_url):
    try:
        urllib.request.urlopen(recipe_url)
    except urllib.error.HTTPError:
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

