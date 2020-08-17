from bs4 import BeautifulSoup
from whats_cookin.models.mongo import Connect
import random
import re
import sys
import time
import urllib.error
import urllib.request

cmd = sys.stdout


def grab_html(recipe_url):
    # Hit url. If the generated url exists, we scrape it.
    try:
        urllib.request.urlopen(recipe_url)
    except urllib.error.HTTPError:
        # Page doesn't exist. We need to wait a few seconds before sending another request, or they temp ban ip.
        cmd.write(recipe_url + '\n')
        cmd.write('Does not exist. Moving on \n')
        cmd.flush()
        time.sleep(3)
        scrape()
    else:
        cmd.write(recipe_url + '\n')
        cmd.write('Success! Continue.. \n')
        cmd.flush()
        recipe_data = BeautifulSoup(urllib.request.urlopen(recipe_url), 'html.parser')
        return recipe_data


def get_recipe_data(data):
    i = 0
    for text in data:
        data[i] = text.get_text()
        i += 1
    return data


def generate_page():
    # Generate a url to hit for data.
    recipe_url = 'https://www.allrecipes.com/recipe/' + str(random.randint(00000, 999999))
    return recipe_url


def scrape():
    page = generate_page()
    data = grab_html(page)
    try:
        # Data is the html, we search for some specific elements.
        # We will then check the data, and ultimately try to index it.
        # To do: Make this more general to hit a wider array of websites.
        ingredient_elements = data.find_all('span', {'class': 'recipe-ingred_txt added'})
        ingredients = get_recipe_data(ingredient_elements)
        direction_elements = data.find_all('span', {'class': 'recipe-directions__list--item'})
        directions = get_recipe_data(direction_elements)
        title_element = data.find('title')
        title = re.sub(r'- Allrecipes\.com', ' ', title_element.get_text())
    except AttributeError:    
        cmd.write('Page is probably empty :/ \n')
        cmd.flush()
        return scrape()
    recipe = {
        'title': title,
        'ingredients': ingredients,
        'directions': directions
    }
    check_recipe_data(recipe)
    return recipe


def check_recipe_data(recipe):
    # Here we make sure the index, i.e. name, ingredients, etc. actually has data tied to it.
    # Restart the process if anything is missing, to avoid incomplete recipe data.    
    for index in recipe:
        value = recipe[index]
        cmd.write(str(value))
        if not value:
            cmd.write('Recipe is missing data. Finding new one. \n')
            cmd.flush()
            scrape()


def mongo_index_recipe():
    connection = Connect.get_connection()   
    db = connection.test
    recipe = scrape()
    try:
        # Here we try to insert the recipe into mongo.
        name = recipe['title']
        ingredients = recipe['ingredients']
        directions = recipe['directions']
        recipe_id = db['recipes'].count_documents({}) + 1
        db.recipes.insert_one({
            'id': recipe_id,
            'name': name,
            'ingredients': ingredients,
            'directions': directions
        })
        cmd.write('We got one! \n' + name + '\n')
        cmd.flush()
    except KeyError:
        # If one of them is not set, and got through the check, we start the process over.
        cmd.write('Tried to index. Failed. Go again! \n')
        cmd.flush()
        scrape()
    except TypeError:
        # Data we are trying to index is incorrect, throw it out.
        cmd.write('Tried to index. Failed. Go again! \n')
        cmd.flush()
        scrape()


if __name__ == '__main__':
    mongo_index_recipe()

