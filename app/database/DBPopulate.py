from .DB import DB

class DBPopulate(DB):

    def __init__(self, mysql):
        super(DBPopulate,self).__init__(DB)
        self.mysql = mysql

    def insertUser(self, firstName,lastName,email,password,address):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO User (first_name, last_name, email, password, address) \
                VALUES('{}','{}','{}','{}','{}')'''.format(firstName, lastName, email, password, address))
        
        # self.__close_conn(conn, cur)

    def insertUnits(self, unitsList):
        # conn, cur = self.__start_conn()

        for unit in unitsList:
            self.cur.execute('''INSERT INTO Measurement (units) VALUES('{}','{}')'''.format(unit[0],unit[1]))
        
        # self.__close_conn(conn, cur)

    def insertRecipe(self, recipeId, recipeName, userMarker):
        # conn, cur = self.__start_conn()

        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO Recipe (recipe_name,added_by) VALUES({},'{}',{})'''. \
                    format(recipeId, recipeName,userMarker))
        
        # self.__close_conn(conn, cur)

    def getRecipeByName(self, recipeName):
        # conn, cur = self.__start_conn()

        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_name='{}' '''.format(recipeName))
        recipe = self.cur.fetchone()
        # self.__close_conn(conn, cur)
        return recipe

    def getRecipeById(self, recipeId):
        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_id={} '''.format(recipeId))
        return self.cur.fetchone()

    def insertInstruction(self,recipeId, step,instruction):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO Instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                    format(recipeId, step, instruction))
        
        # self.__close_conn(conn, cur)

    def getFoodByName(self,name):
        # conn, cur = self.__start_conn()

        self.cur.execute('''SELECT * FROM Food_Item WHERE food_name='{}' '''.format(name))
        food = self.cur.fetchone()
        # self.__close_conn(conn, cur)
        return food

    def insertFood(self,food, colariesPerGram, colariesPerMl):
        self.cur.execute('''INSERT INTO Food_Item (food_name, calories_per_g, calories_per_ml) VALUES('{}',{},{}) '''. \
                    format(food, colariesPerGram, colariesPerMl))
        

    def insertIngredInRecipe(self,foodId,recipeId, quantity,units):
        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,quantity,units) 
                               VALUES({},{},{},'{}') '''.format(foodId,recipeId,quantity,units))
    

