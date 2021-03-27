
class DBPopulate:

    def __init__(self, mysql):

        self.mysql = mysql
        self.cur = mysql.connection
        self.cur = self.cur.cursor()

    def insertUser(self, firstName,lastName,email,password,address):

        self.cur.execute('''INSERT INTO `User` (first_name, last_name, email, password, address) \
                VALUES('{}','{}','{}','{}','{}')'''.format(firstName, lastName, email, password, address))
        self.mysql.connection.commit()

    def insertUnits(self, unitsList):
        for unit in unitsList:
            self.cur.execute('''INSERT INTO Measurement (units,type) VALUES('{}','{}')'''.format(unit[0],unit[1]))
            self.mysql.connection.commit()

    def insertRecipe(self, recipeId, recipeName, userMarker):
        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                    format(recipeId,recipeName,userMarker))
        self.mysql.connection.commit()

    def getRecipeByName(self, recipeName):
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_name='{}' '''.format(recipeName))
        return self.cur.fetchone()

    def getRecipeById(self, recipeId):
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_id={} '''.format(recipeId))
        return self.cur.fetchone()

    def insertInstruction(self,recipeId, step,instruction):
        self.cur.execute('''INSERT INTO instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                    format(recipeId, step, instruction))
        self.mysql.connection.commit()

    def getFoodByName(self,name):
        self.cur.execute('''SELECT * FROM Food_Item WHERE food_name='{}' '''.format(name))
        return self.cur.fetchone()


    def insertFood(self,food, colariesPerGram, colariesPerMl):
        self.cur.execute('''INSERT INTO Food_Item (food_name, calories_per_g, calories_per_ml) VALUES('{}',{},{}) '''. \
                    format(food, colariesPerGram, colariesPerMl))
        self.mysql.connection.commit()

    def insertIngredInRecipe(self,foodId,recipeId, quantity,units):
        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,quantity,units) 
                               VALUES({},{},{},'{}') '''.format(foodId,recipeId,quantity,units))
        self.mysql.connection.commit()



