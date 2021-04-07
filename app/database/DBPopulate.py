from .DB import DB
from mysql.connector import errors

class DBPopulate(DB):

    def __init__(self, mysql):
        super().__init__(mysql)

    def insertUser(self, data):
        self._start_conn()
        query = ("INSERT INTO user (first_name, last_name, email, password) \
                VALUES(%(fname)s, %(lname)s,%(email)s,%(password)s)")#.format(data['fname'],data['lname'],data['email'],data['password'])
        # print(data)
        try:
            self.cur.execute(query,data)
            result = True
        except errors.IntegrityError:
            result =  False
        except errors.DatabaseError:
            result = 'dberr'
        finally:
            self._close_conn()
            return result
        

    def insertUnits(self, unitsList):
        self._start_conn()

        try:
            for unit in unitsList:
                self.cur.execute('''INSERT INTO measurement (units,type) VALUES('{}','{}')'''.format(unit[0],unit[1]))
                    
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()

    def insertRecipe(self, recipeId, recipeName, userMarker):
        self._start_conn()
        try:
            '''create recipe with id and name'''
            self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''.format(recipeId, recipeName,userMarker))
                    
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()

    def getRecipeByName(self, recipeName):
        self._start_conn()
        recipe = {}
        try:
            self.cur.execute('''SELECT * FROM recipe WHERE recipe_name='{}' '''.format(recipeName))
            recipe = self.cur.fetchone()
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()
            return recipe

    def getRecipeById(self, recipeId):
        self._start_conn()
        try:
            self.cur.execute('''SELECT * FROM recipe WHERE recipe_id={} '''.format(recipeId))
            recipe = self.cur.fetchone()
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()
            return recipe 

    def insertInstruction(self,recipeId, step,instruction):
        self._start_conn()
        try:
            self.cur.execute('''INSERT INTO instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                        format(recipeId, step, instruction))
        except errors.Error as e:
            print(e)
        finally:        
            self._close_conn()

    def getFoodByName(self,name):
        self._start_conn()
        food = {}
        try:
            self.cur.execute('''SELECT * FROM food_item WHERE food_name='{}' '''.format(name))
            food = self.cur.fetchone()
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()
            return food

    def insertFood(self,food, colariesPerGram, colariesPerMl):
        self._start_conn()
        try:
            self.cur.execute('''INSERT INTO food_item (food_name, calories_per_g, calories_per_ml) VALUES('{}',{},{}) '''. \
                        format(food, colariesPerGram, colariesPerMl))
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()

    def insertIngredInRecipe(self,foodId,recipeId, quantity,units):
        self._start_conn()
        try:
            self.cur.execute('''INSERT INTO ingredients_in_recipes (food_id,recipe_id,quantity,units) 
                                VALUES({},{},{},'{}') '''.format(foodId,recipeId,quantity,units))
        except errors.Error as e:
            print(e)
        finally:
            self._close_conn()

