from .DB import DB
from mysql.connector import errors

class DBPopulate(DB):

    def __init__(self, mysql):
        super(DBPopulate,self).__init__(DB)
        self.mysql = mysql

    def insertUser(self, data):
        self._start_conn()
        query = '''INSERT INTO user (first_name, last_name, email, password) \
                VALUES('{fname}','{lname}','{email}','{password}')'''
        try:
            self.cur.execute(query,data)
            result = True
        except errors.IntegrityError:
            result =  False
        finally:
            return result
            self._close_conn()

    def insertUnits(self, unitsList):
        self._start_conn()

        for unit in unitsList:
            self.cur.execute('''INSERT INTO measurement (units,type) VALUES('{}','{}')'''.format(unit[0],unit[1]))
        
        self._close_conn()

    def insertRecipe(self, recipeId, recipeName, userMarker):
        self._start_conn()

        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''.format(recipeId, recipeName,userMarker))
        
        self._close_conn()

    def getRecipeByName(self, recipeName):
        self._start_conn()

        self.cur.execute('''SELECT * FROM recipe WHERE recipe_name='{}' '''.format(recipeName))
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe

    def getRecipeById(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM recipe WHERE recipe_id={} '''.format(recipeId))
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe 

    def insertInstruction(self,recipeId, step,instruction):
        self._start_conn()

        self.cur.execute('''INSERT INTO instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                    format(recipeId, step, instruction))
        
        self._close_conn()

    def getFoodByName(self,name):
        self._start_conn()

        self.cur.execute('''SELECT * FROM food_item WHERE food_name='{}' '''.format(name))
        food = self.cur.fetchone()
        self._close_conn()
        return food

    def insertFood(self,food, colariesPerGram, colariesPerMl):
        self._start_conn()
        self.cur.execute('''INSERT INTO food_item (food_name, calories_per_g, calories_per_ml) VALUES('{}',{},{}) '''. \
                    format(food, colariesPerGram, colariesPerMl))
        self._close_conn()

    def insertIngredInRecipe(self,foodId,recipeId, quantity,units):
        self._start_conn()
        self.cur.execute('''INSERT INTO ingredients_in_recipes (food_id,recipe_id,quantity,units) 
                               VALUES({},{},{},'{}') '''.format(foodId,recipeId,quantity,units))
        self._close_conn()

