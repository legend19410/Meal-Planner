from .DB import DB
class DBUpdate(DB):

    def __init__(self, mysql):
        super(DBUpdate,self).__init__(DB)
        self.mysql = mysql

    def insertRecipe(self, recipeId, recipeName, userMarker):
        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                         format(recipeId, recipeName, userMarker))
        self.mysql.commit()

    def insertUser(self, firstName, lastName, email, password):
        self.cur.execute('''INSERT INTO User (first_name,last_name,email,password) VALUES({},{},{},{})'''. \
                         format(firstName, lastName, email, password))
        self.mysql.commit()

    def insertInstruction(self,recipeId, step, description):
        self.cur.execute('''INSERT INTO Instruction (recipe_id,step,description) VALUES({},{},{})'''. \
                         format(recipeId, step, description))
        self.mysql.commit()

    def insertIngredients(self, foodId, recipeId,units,quantity):
        self._start_conn()
        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,units,quantity) VALUES({},{},'{}',{})'''. \
                         format(foodId, recipeId,units,quantity))
        self._close_conn()

    def insertFoodInKitchenStock(self,userId,recipeId,units,quantity):
        self.cur.execute('''INSERT INTO Kitchen_Stock (food_id,recipe_id,units,quantity) VALUES({},{},{})'''. \
                         format(userId,recipeId,units,quantity))
        self.mysql.commit()

    def updateFoodInKitchenStock(self, userId, recipeId, quantity):
        self.cur.execute('''UPDATE TABLE Kitchen_Stock SET quantity={} WHERE user_id={} AND recipe_id={}'''. \
                         format(quantity,userId, recipeId))
        self.mysql.commit()

    def insertMeal(self, userId, recipeId, date, servings, type):
        self.cur.execute('''INSERT INTO Meal_Plan (user_id,recipe_id,consumption_date,type) VALUES({},{},{},{})'''. \
                         format(userId, recipeId, date, servings, type))
        self.mysql.commit()

