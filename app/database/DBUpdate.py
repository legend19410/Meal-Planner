from .DB import DB
from mysql.connector import errors
class DBUpdate(DB):

    def __init__(self, mysql):
        super(DBUpdate,self).__init__(DB)
        self.mysql = mysql

    def insertUser(self, firstName, lastName, email, password):
        self._start_conn()
        self.cur.execute('''INSERT INTO User (first_name,last_name,email,password) VALUES('{}','{}','{}','{}')'''. \
                             format(firstName, lastName, email, password))
        self.conn.commit()
        self._close_conn()

    def insertRecipe(self,recipeId,recipeName, userMarker):
        '''create recipe with id and name'''
        self._start_conn()
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                            format(recipeId,recipeName, userMarker))
        self.conn.commit()
        self._close_conn()

    def insertInstruction(self,recipeId, step, description):
        self._start_conn()
        self.cur.execute('''INSERT INTO Instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                                 format(recipeId, step, description))
        self.conn.commit()
        self._close_conn()


    def insertIngredients(self, foodId, recipeId,units,quantity):
        self._start_conn()

        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,units,quantity) VALUES({},{},'{}',{})'''. \
                    format(foodId, recipeId, units, quantity))
        self.conn.commit()
        self._close_conn()


    def insertFoodInKitchenStock(self,userId,foodId,units,quantity):
        self._start_conn()

        self.cur.execute('''INSERT INTO Kitchen_Stock (user_id,food_id,units,quantity) VALUES({},{},'{}',{})'''. \
                             format(userId, foodId, units, quantity))
        self.conn.commit()
        self._close_conn()

    def updateFoodInKitchenStock(self, userId, recipeId, quantity):

        self._start_conn()
        try:
            self.cur.execute('''UPDATE TABLE Kitchen_Stock SET quantity={} WHERE user_id={} AND recipe_id={}'''. \
                             format(quantity, userId, recipeId))
            self.conn.commit()
            result = True
        except errors.IntegrityError:
            result = False
        finally:
            self._close_conn()
            return result

    def insertMeal(self, userId, recipeId, date, servings, type):
        self._start_conn()

        self.cur.execute('''INSERT INTO Meal_Plan (user_id,recipe_id,consumption_date,serving,type_of_meal) VALUES({},{},'{}','{}','{}')'''. \
                             format(userId, recipeId, date, servings, type))
        self.conn.commit()
        self._close_conn()



