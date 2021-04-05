from .DB import DB
from .conversions import convert

class DBQuery(DB):

    def __init__(self, mysql):
        super(DBQuery,self).__init__(DB)
        self.mysql = mysql

    def getAllMeasurments(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM measurement''')
        measurements = self.cur.fetchall()
        self._close_conn()
        return measurements
    
    def getUser(self, id, email):
        self._start_conn()
        query = "SELECT * FROM user WHERE email=%(email)s or user_id=%(id)s"
        self.cur.execute(query, {'email':email, 'id':id})
        user = self.cur.fetchone()
        self._close_conn()
        return user

    def getRecipesOfCalCount(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM recipe''')
        recipes = self.cur.fetchall()
        self._close_conn()
        return recipes

    def getRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM recipe WHERE recipe_id={}'''.format(recipeId))
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe

    def getInstructionForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM instruction WHERE recipe_id={}'''.format(recipeId))
        instructions = self.cur.fetchall()
        self._close_conn()
        return instructions

    def getIngredientsForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM ingredients_in_recipes JOIN food_item ON ingredients_in_recipes.food_id=\
        food_item.food_id WHERE ingredients_in_recipes.recipe_id={}'''.format(recipeId))
        ingredients = self.cur.fetchall()
        self._close_conn()
        return ingredients

    def getUserById(self, userId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM user WHERE user_id={}'''.format(userId))
        user = self.cur.fetchone()
        self._close_conn()
        return user

    def getMealsForDate(self, userId, date):
        self._start_conn()
        self.cur.execute('''SELECT * FROM meal_plan JOIN recipe ON meal_plan.recipe_id=recipe.recipe_id\
                            WHERE user_id={} AND consumption_date='{}' '''.format(userId,date))
        meals = self.cur.fetchall()
        self._close_conn()
        return meals

    def getMealInRange(self, userId, startDate, endDate):
        self._start_conn()
        self.cur.execute('''SELECT * FROM meal_plan JOIN recipe ON meal_plan.recipe_id=recipe.recipe_id WHERE user_id={}\
                            AND consumption_date >= '{}' AND consumption_date <= '{}' ORDER BY consumption_date,type_of_meal ASC  '''.\
                         format(userId, startDate, endDate))
        meals = self.cur.fetchall()
        self._close_conn()
        return meals

    def getMaxRecipeId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(recipe_id) AS recipe_id FROM recipe''')
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe['recipe_id']

    def getMaxUserId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(user_id) AS user_id FROM user''')
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe['user_id']

    def getMyStock(self, userId):
        self._start_conn()
        self.cur.execute('''SELECT * From kitchen_stock JOIN food_item ON kitchen_stock.food_id=food_item.food_id \
        WHERE kitchen_stock.user_id={}'''.format(userId))
        stock = self.cur.fetchall()
        self._close_conn()
        return stock

    def getCalCount(self,recipeId):
        ingredients = self.getIngredientsForRecipe(recipeId)
        calCount = 0
        for ing in ingredients:
            calCount += convert(ing['units'],float(ing['quantity']),float(ing['calories_per_ml']),float(ing['calories_per_g']))
        return calCount

    def generateSupermarketList(self,recipeId):
        self._start_conn()
        self.cur.execute('''SELECT food_item.food_name FROM ingredients_in_recipes JOIN food_item ON ingredients_in_recipes.food_id=\
                food_item.food_id WHERE ingredients_in_recipes.recipe_id={}'''.format(recipeId))
        foods = self.cur.fetchall()
        self._close_conn()
        return foods

    def getRandomRecipe(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM recipe ORDER BY RAND() LIMIT 1''')
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe
