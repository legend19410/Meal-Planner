import random
from faker import Faker
import pandas as pd
import re
import mysql.connector
import os

class PopulateDatabase:

    def __init__(self, dbPopulate):
        self.dbPopulate = dbPopulate
        self.NUMBER_OF_USERS = 200000
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
        # count = 1

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
                    self.dbPopulate.insertIngredInRecipe(int(food[0]),recipeId,quantity,self.getRandMea(self.units))
                else:
                    quantity = self.ran(1, 15)
                    print(self.getRandMea(self.units))
                    self.dbPopulate.insertIngredInRecipe(int(ingred[0]), recipeId, quantity, self.getRandMea(self.units))

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
        return lst[ranVal][0]

    def ran(self,lbount, ubound):
        return round(random.uniform(lbount, ubound), 1)

    def removeDuplicates(self, lst):
         return list(dict.fromkeys(lst))


class DBPopulate:

    def __init__(self, mysql):
        self.mysql = mysql
        self.cur = mysql.cursor()

    def insertUser(self, firstName, lastName, email, password, address):
        self.cur.execute('''INSERT INTO `User` (first_name, last_name, email, password, address) \
                VALUES('{}','{}','{}','{}','{}')'''.format(firstName, lastName, email, password, address))
        self.mysql.commit()

    def insertUnits(self, unitsList):
        for unit in unitsList:
            self.cur.execute('''INSERT INTO Measurement (units,type) VALUES('{}','{}')'''.format(unit[0], unit[1]))
            self.mysql.commit()

    def insertRecipe(self, recipeId, recipeName, userMarker):
        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                         format(recipeId, recipeName, userMarker))
        self.mysql.commit()

    def getRecipeByName(self, recipeName):
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_name='{}' '''.format(recipeName))
        return self.cur.fetchone()

    def getRecipeById(self, recipeId):
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_id={} '''.format(recipeId))
        return self.cur.fetchone()

    def insertInstruction(self, recipeId, step, instruction):
        self.cur.execute('''INSERT INTO instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                         format(recipeId, step, instruction))
        self.mysql.commit()

    def getFoodByName(self, name):
        self.cur.execute('''SELECT * FROM Food_Item WHERE food_name='{}' '''.format(name))
        return self.cur.fetchone()

    def insertFood(self, food, colariesPerGram, colariesPerMl):
        self.cur.execute('''INSERT INTO Food_Item (food_name, calories_per_g, calories_per_ml) VALUES('{}',{},{}) '''. \
                         format(food, colariesPerGram, colariesPerMl))
        self.mysql.commit()

    def insertIngredInRecipe(self, foodId, recipeId, quantity, units):
        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,quantity,units) 
                               VALUES({},{},{},'{}') '''.format(foodId, recipeId, quantity, units))
        self.mysql.commit()


if __name__ =='__main__':


    try:
        connection = mysql.connector.connect(host= os.environ.get('MYSQL_HOST') or 'localhost',
                                             database= os.environ.get('MYSQL_DB') or 'meal_planner',
                                             user= os.environ.get('MYSQL_USER') or 'root',
                                             password= os.environ.get('MYSQL_PASSWORD') or '')
        popRec = PopulateDatabase(DBPopulate(connection))
        popRec.populateRecipes()

        # cursor = connection.cursor()
        # cursor.execute(mySql_insert_query)
        # connection.commit()
        # print(cursor.rowcount, "Record inserted successfully into Laptop table")
        connection.cursor().close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")