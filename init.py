import importRecipes
import exportRecipes

csvFileName = 'plantoeat-recipes.csv'
importedRecipes = importRecipes.readFromCsv(csvFileName)

exportRecipes.exportPaprikaYaml(importedRecipes)