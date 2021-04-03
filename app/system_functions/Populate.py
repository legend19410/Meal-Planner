import random
from faker import Faker
import pandas as pd
import re


class PopulateDatabase:

    def __init__(self, dbPopulate):
        self.dbPopulate = dbPopulate
        self.NUMBER_OF_USERS = 100
        self.units = [('gill','volume'),('teaspoon','volume'), ('tablespoon','volume'), ('ounce','mass'), ('cup','volume'),\
                        ('pint','volume'), ('quart','volume'), ('gallon','volume'), \
                        ('ml','volume'), ('litre','volume'), ('lb','mass'),('mg','mass'), ('g','mass'),('dl','mass')]

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

        '''read the recipes from the csv file into a dataframe'''
        recipes = pd.read_csv('./RAW_recipes.csv')
        count = 1

        for recipe in recipes.index:
            # count = count + 1
            # if count < 890:
            #     continue

            ingredients = recipes['ingredients'][recipe]
            ingredients = self.convertToList(ingredients)
            ingredients = self.filterStringInLst(ingredients)
            ingredients = self.removeDuplicates(ingredients)

            instructions = recipes['steps'][recipe]
            instructions = self.convertToList(instructions)
            instructions = self.filterStringInLst(instructions)

            recipeName = recipes['name'][recipe]
            recipeName = self.filterString(recipeName)

            recipeId = int(recipes['id'][recipe])

            '''if recipe already in database skip'''
            if self.dbPopulate.getRecipeById(recipeId) != None:
                continue

            self.dbPopulate.insertRecipe(recipeId, recipeName, random.randint(1,self.NUMBER_OF_USERS))
            # recipeId = int(self.dbPopulate.getRecipeByName(recipeName)['recipe_id'])

            for index, instruction in enumerate(instructions):
                self.dbPopulate.insertInstruction(recipeId, index+1,instruction)
            for ingredient in ingredients:
                ingred = self.dbPopulate.getFoodByName(ingredient)
                if ingred == None:
                    self.dbPopulate.insertFood(ingredient, self.ran(1,13), self.ran(1,13))
                    food = self.dbPopulate.getFoodByName(ingredient)
                    quantity = self.ran(1, 15)
                    self.dbPopulate.insertIngredInRecipe(int(food['food_id']),recipeId,quantity,self.getRandMea(self.units))
                else:
                    quantity = self.ran(1, 15)
                    self.dbPopulate.insertIngredInRecipe(int(ingred['food_id']), recipeId, quantity, self.getRandMea(self.units))

            count = count + 1
            if count > 25:
                break

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
        return lst[ranVal][0]

    def ran(self,lbount, ubound):
        return round(random.uniform(lbount, ubound), 1)

    def removeDuplicates(self, lst):
         return list(dict.fromkeys(lst))

    
    def insertUser(self,data):
        return self.dbPopulate.insertUser(data)