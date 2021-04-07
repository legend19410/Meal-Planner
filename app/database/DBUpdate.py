from .DB import DB
from mysql.connector import errors
class DBUpdate(DB):

    def __init__(self, mysql):
        super().__init__(mysql)

    def insertUser(self, firstName, lastName, email, password):
<<<<<<< HEAD
        try:
            self._start_conn()
            self.cur.execute('''INSERT INTO user (first_name,last_name,email,password) VALUES('{}','{}','{}','{}')'''. \
                                format(firstName, lastName, email, password))
            self._close_conn()
        except errors.Error as e:
            print(e)
        
=======
        self._start_conn()
        self.cur.execute('''INSERT INTO User (first_name,last_name,email,password) VALUES('{}','{}','{}','{}')'''. \
                             format(firstName, lastName, email, password))
        self.conn.commit()
        self._close_conn()
>>>>>>> home-page

    def insertRecipe(self,recipeId,recipeName, image, userMarker):
        '''create recipe with id and name'''
<<<<<<< HEAD
        try:
            self._start_conn()
            self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name, image, added_by) VALUES({},'{}', '{}',{})'''. \
                                format(recipeId,recipeName,image, userMarker))
            self._close_conn()
        except errors.Error as e:
            print(e)
        
        

    def insertInstruction(self,recipeId, step, description):
        try:
            self._start_conn()
            self.cur.execute('''INSERT INTO instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                                    format(recipeId, step, description))
            self._close_conn()
        except errors.Error as e:
            print(e)

=======
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
>>>>>>> home-page


    def insertIngredients(self, foodId, recipeId,units,quantity):
        try:
            self._start_conn()

            self.cur.execute('''INSERT INTO ingredients_in_recipes (food_id,recipe_id,units,quantity) VALUES({},{},'{}',{})'''. \
                        format(foodId, recipeId, units, quantity))
            self._close_conn()        
        except errors.Error as e:
            print(e)

<<<<<<< HEAD
=======
        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,units,quantity) VALUES({},{},'{}',{})'''. \
                    format(foodId, recipeId, units, quantity))
        self.conn.commit()
        self._close_conn()
>>>>>>> home-page


    def insertFoodInKitchenStock(self,userId,foodId,units,quantity):
        try:
            self._start_conn()

            self.cur.execute('''INSERT INTO kitchen_stock (user_id,food_id,units,quantity) VALUES({},{},'{}',{})'''. \
                                format(userId, foodId, units, quantity))
            self._close_conn()
        except errors.Error as e:
            print(e)

<<<<<<< HEAD
=======
        self.cur.execute('''INSERT INTO Kitchen_Stock (user_id,food_id,units,quantity) VALUES({},{},'{}',{})'''. \
                             format(userId, foodId, units, quantity))
        self.conn.commit()
        self._close_conn()
>>>>>>> home-page

    def updateFoodInKitchenStock(self, userId, recipeId, quantity):

        self._start_conn()
        try:
            self.cur.execute('''UPDATE TABLE kitchen_stock SET quantity={} WHERE user_id={} AND recipe_id={}'''. \
                             format(quantity, userId, recipeId))
            self._close_conn()
            result = True
        except errors.IntegrityError:
            result = False
        finally:
            self._close_conn()
            return result

    def insertMeal(self, userId, recipeId, date, servings, mealType):
        try:
            self._start_conn()

            self.cur.execute('''INSERT INTO meal_plan (user_id,recipe_id,consumption_date,serving,type_of_meal) VALUES({},{},'{}','{}','{}')'''. \
                                format(userId, recipeId, date, servings, mealType))
            self._close_conn()        
        except errors.Error as e:
            print(e)

    def deleteMeal(self, userId, date):
        try:
            self._start_conn()

            self.cur.execute('''DELETE from meal_plan where consumption_date='{}' and user_id ={}'''. \
                                format(date, userId))
            self._close_conn()        
        except errors.Error as e:
            print(e)

<<<<<<< HEAD
=======
        self.cur.execute('''INSERT INTO Meal_Plan (user_id,recipe_id,consumption_date,serving,type_of_meal) VALUES({},{},'{}','{}','{}')'''. \
                             format(userId, recipeId, date, servings, type))
        self.conn.commit()
        self._close_conn()
>>>>>>> home-page



