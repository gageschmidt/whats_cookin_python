from bs4 import BeautifulSoup
import urllib.request
import random

# h1 recipe-main-content recipe-summary__h1 itemprop="name"
# section recipe-ingredients
# section recipe-directions
# section recipe-footnotes

def parse():
    data = scrape()
    ingredients = data.find_all("section", {"class": "recipe-ingredient"})
    return data

def scrape():
    query = generate_recipe_query()
    recipe = check_recipe_url(query)
    return recipe

def check_recipe_url(query):
    recipe_url = 'https://www.allrecipes.com/recipe/2' + str(query)
    recipe_data = urllib.request.urlopen(recipe_url)
    if recipe_data.getcode() is not '404':
         recipe_data = BeautifulSoup(urllib.request.urlopen(recipe_url), 'html.parser')
         return recipe_data

def generate_recipe_query():
    return random.randint(00000, 99999)