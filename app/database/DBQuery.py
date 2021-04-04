from .DB import DB

class DBQuery(DB):

    def __init__(self, mysql):
        super(DBQuery,self).__init__(DB)
        self.mysql = mysql

    def getAllMeasurments(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM measurement''')
        measurements = self.cur.fetchall()
        # self._close_conn()
        return measurements
    
    def getUser(self, id, email):
        self._start_conn()
        query = "SELECT * FROM user WHERE email=%(email)s or user_id=%(id)s"
        self.cur.execute(query, {'email':email, 'id':id})
        user = self.cur.fetchone()
        # self._close_conn()
        return user

    def getRecipesOfCalCount(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Recipe WHERE ''')
        recipes = self.cur.fetchall()
        # self._close_conn()
        return recipes

    def getRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_id={}'''.format(recipeId))
        recipe = self.cur.fetchone()
        # self._close_conn()
        return recipe

    def getInstructionForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Instruction WHERE recipe_id={}'''.format(recipeId))
        instructions = self.cur.fetchall()
        # self._close_conn()
        return instructions

    def getIngredientsForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Ingredients_In_Recipes WHERE recipe_id={}'''.format(recipeId))
        ingredients = self.cur.fetchall()
        # self._close_conn()
        return ingredients

    def getUserById(self, userId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM User WHERE user_id={}'''.format(userId))
        user = self.cur.fetchone()
        # self._close_conn()
        return user

    def getMealForDate(self, userId, date):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Meal_Plan WHERE user_id={} AND consumption_date='{}' '''\
                         .format(userId,date))
        meals = self.cur.fetchall()
        # self._close_conn()
        return meals

    def getMealInRange(self, userId, startDate, endDate):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Meal_Plan WHERE user_id={} AND consumption_date >= '{}' AND\
                            consumption_date <= '{}' ORDER BY consumption_date ASC'''.format(userId, startDate, endDate))
        meals = self.cur.fetchall()
        # self._close_conn()
        return meals

    def getMaxRecipeId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(recipe_id) AS recipe_id FROM Recipe''')
        recipe = self.cur.fetchone()
        # self._close_conn()
        return recipe['recipe_id']

    def getMaxUserId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(user_id) AS user_id FROM User''')
        recipe = self.cur.fetchone()
        # self._close_conn()
        return recipe['user_id']

    def getMyStock(self, userId):
        self._start_conn()
        self.cur.execute('''SELECT * From Kitchen_Stock JOIN Food_Item ON Kitchen_Stock.food_id=Food_Item.food_id \
        WHERE Kitchen_Stock.user_id={}'''.format(userId))
        stock = self.cur.fetchall()
        # self._close_conn()
        return stock