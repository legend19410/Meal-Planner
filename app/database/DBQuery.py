from .DB import DB

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
    def getUser(self, id, email):
        self._start_conn()
        query = "SELECT * FROM user WHERE email=%(email)s or user_id=%(id)s"
        self.cur.execute(query, {'email':email, 'id':id})
        user = self.cur.fetchone()
        self._close_conn()
        return user

    def getRecipes(self):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Recipe''')
        recipes = self.cur.fetchall()
        self._close_conn()
        return recipes

    def getRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_id={}'''.format(recipeId))
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe

    def getInstructionForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Instruction WHERE recipe_id={}'''.format(recipeId))
        instructions = self.cur.fetchall()
        self._close_conn()
        return instructions

    def getIngredientsForRecipe(self, recipeId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Ingredients_In_Recipes WHERE recipe_id={}'''.format(recipeId))
        ingredients = self.cur.fetchall()
        self._close_conn()
        return ingredients

    def getUserById(self, userId):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Instruction WHERE user_id={}'''.format(userId))
        user = self.cur.fetchone()
        self._close_conn()
        return user

    def getMealForDate(self, userId, date):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Meal_Plan WHERE user_id={} AND consumption_date={}'''\
                         .format(userId,date))
        meals = self.cur.fetchall()
        self._close_conn()
        return meals

    def getMealInRange(self, userId, startDate, endDate):
        self._start_conn()
        self.cur.execute('''SELECT * FROM Meal_Plan WHERE user_id={} AND consumption_date >= {} AND\
                            consumption_date <= {}'''.format(userId, startDate, endDate))
        meals = self.cur.fetchall()
        self._close_conn()
        return meals

