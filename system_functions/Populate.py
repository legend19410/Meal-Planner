import random
from faker import Faker
import pandas as pd
import re


class PopulateDatabase:

    def __init__(self, dbPopulate):
        self.dbPopulate = dbPopulate
        self.NUMBER_OF_USERS = 200000
        self.units = ['gill','teaspoon', 'tablespoon', 'ounce', 'cup', 'pint', 'quart', 'gallon', 'ml', 'litre', 'slice', 'lb',
                 'mg', 'g','dl']

    def populateUsers(self):

        fake = Faker()

        for i in range(self.NUMBER_OF_USERS):

            firstName = fake.first_name()
            lastName = fake.last_name()
            email = fake.safe_email()
            password = fake.password()
            address = fake.address()

            self.dbPopulate.insertUser(firstName,lastName,email,password,address)

    def populateUnits(self):
        self.dbPopulate.insertUnits(self.units)

    def populateRecipes(self):
        recipes = pd.read_csv('./RAW_recipes.csv')
        # count = 1

        for recipe in recipes.index:

            ingredients = recipes['ingredients'][recipe]
            ingredients = self.convertToList(ingredients)
            ingredients = self.filterStringInLst(ingredients)

            instructions = recipes['steps'][recipe]
            instructions = self.convertToList(instructions)
            instructions = self.filterStringInLst(instructions)

            recipeName = recipes['name'][recipe]
            recipeName = self.filterString(recipeName)
            # recipeId = int(recipes['id'][recipe])

            self.dbPopulate.insertRecipe(recipeName, random.randint(1,self.NUMBER_OF_USERS))
            recipeId = int(self.dbPopulate.getRecipeByName(recipeName)['recipe_id'])

            for index, instruction in enumerate(instructions):
                self.dbPopulate.insertInstruction(recipeId, index+1,instruction)
            for ingredient in ingredients:
                ingred = self.dbPopulate.getFoodByName(ingredient)
                if ingred == None:
                    self.dbPopulate.insertFood(ingredient, self.ran(1,13))
                    food = self.dbPopulate.getFoodByName(ingredient)
                    quantity = self.ran(1, 15)
                    self.dbPopulate.insertIngredInRecipe(int(food['food_id']),recipeId,quantity,float(food['calories_per_unit'])\
                                                         * quantity,self.getRandMea(self.units))
                else:
                    quantity = self.ran(1, 15)
                    self.dbPopulate.insertIngredInRecipe(int(ingred['food_id']), recipeId, quantity,\
                                                         float(ingred['calories_per_unit']) \
                                                         * quantity, self.getRandMea(self.units))

            # count = count + 1
            # if count > 1:
            #     break

    def convertToList(self, string):
        return string.strip('][').split(', ')

    def filterStringInLst(self,lst):

        newlst = []
        for el in lst:
            noQuotes = el.strip("'")
            alphaNum = re.sub(r'\W+', ' ', noQuotes)
            # alphaNum = ''.join(filter(str.isalnum, noQuotes))
            newlst.append(alphaNum.strip())
        return newlst

    def filterString(self,string):

        alphaNum = re.sub(r'\W+', ' ', string)
        # alphaNum = ''.join(filter(str.isalnum, string))
        return alphaNum.strip()

    def getRandMea(self,lst):

        ranVal = random.randint(1, len(lst)-1)
        return lst[ranVal]

    def ran(self,lbount, ubound):
        return round(random.uniform(lbount, ubound), 1)
