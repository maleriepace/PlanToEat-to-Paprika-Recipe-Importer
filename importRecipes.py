import csv
import array


def readFromCsv(filename):
    with open(filename) as csvfile:
        items = csv.reader(csvfile, delimiter=',')
        recipes = []
        for row in items:
            recipe = getRecipe(row)
            recipes.append(recipe)
        print("%s Recipes Found" % (len(recipes)))
    return recipes

def getRecipe(row):
    columns = ["Title","Course","Cuisine","MainIngredient","Description","Source","Url","UrlHost","PrepTime","CookTime","TotalTime","Servings","Yield","Ingredients","Directions","Tags","Rating","PublicUrl","PhotoUrl","Private","NutritionalScore","Calories","Fat","Cholesterol","Sodium","Sugar","Carbohydrate","Fiber","Protein","Cost","CreatedAt","UpdatedAt"]
    recipe = {}

    i = 0
    while i < len(columns):
        name = columns[i]
        value = row[i]

        recipe[name] = value

        i += 1

    for data in columns:
        recipe[data]
    return recipe
