import requests
import yaml
import base64
from math import floor

def exportPaprikaYaml(recipes):
    items = []
    i = 1
    page = 1
    while i < len(recipes):
        item = {}
        item['name'] = recipes[i]['Title']
        item['servings'] = recipes[i]['Servings']
        item['source'] = recipes[i]['UrlHost']
        item['source_url'] = recipes[i]['Source']
        item['prep_time'] = recipes[i]['PrepTime']
        item['cook_time'] = recipes[i]['CookTime']
        item['categories'] = getCategories(recipes[i])
        item['photo'] = get_as_base64(recipes[i]['PhotoUrl'])
        item['ingredients'] = recipes[i]['Ingredients']
        item['directions'] = recipes[i]['Directions']
        items.append(item)
        newPage = floor((i/50) + 1)
        if newPage != page:
            with open('paprikaRecipes%s.yml' % page, 'w') as file:
                yaml.dump(items, file, explicit_start=False, default_style='|', width=75)
            items = []
            page = newPage

        print("Page %s" % floor((i/30) + 1))
        i +=1
    with open('paprikaRecipes%s.yml' % page, 'w') as file:
        yaml.dump(items, file, explicit_start=False, default_style='|', width=75)

def getCategories(recipe):
    categories = []
    if recipe['Course']:
        categories.append(recipe['Course'])
    if recipe['Cuisine']:
        categories.append(recipe['Cuisine'])
    if recipe['MainIngredient']:
        categories.append(recipe['MainIngredient'])
    return categories

def get_as_base64(url):
    if url != '':
        return base64.b64encode(requests.get(url).content).decode('utf-8')
