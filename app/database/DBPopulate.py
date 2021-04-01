from mysql.connector import errors

class DBPopulate:

    def __init__(self, mysql):
        self.mysql = mysql

    def insertUser(self, firstName,lastName,email,password,address):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO User (first_name, last_name, email, password, address) \
                VALUES('{}','{}','{}','{}','{}')'''.format(firstName, lastName, email, password, address))
        
        # self.__close_conn(conn, cur)

    def insertUnits(self, unitsList):
        # conn, cur = self.__start_conn()

        for unit in unitsList:
            self.cur.execute('''INSERT INTO Measurement (units) VALUES('{}')'''.format(unit))
        
        # self.__close_conn(conn, cur)

    def insertRecipe(self, recipeName, userMarker):
        # conn, cur = self.__start_conn()

        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO Recipe (recipe_name,added_by) VALUES('{}',{})'''. \
                    format(recipeName,userMarker))
        
        # self.__close_conn(conn, cur)

    def getRecipeByName(self, recipeName):
        # conn, cur = self.__start_conn()

        self.cur.execute('''SELECT * FROM Recipe WHERE recipe_name='{}' '''.format(recipeName))
        recipe = cur.fetchone()
        # self.__close_conn(conn, cur)
        return recipe

    def insertInstruction(self,recipeId, step,instruction):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO Instruction (recipe_id,step,description) VALUES({},{},'{}')'''. \
                    format(recipeId, step, instruction))
        
        # self.__close_conn(conn, cur)

    def getFoodByName(self,name):
        # conn, cur = self.__start_conn()

        self.cur.execute('''SELECT * FROM Food_Item WHERE food_name='{}' '''.format(name))
        food = cur.fetchone()
        # self.__close_conn(conn, cur)
        return food

    def insertFood(self,food, colaries):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO Food_Item (food_name, calories_per_unit) VALUES('{}',{}) '''. \
                    format(food, colaries))
        # self.__close_conn(conn, cur)


    def insertIngredInRecipe(self,foodId,recipeId, quantity,total_calories,units):
        # conn, cur = self.__start_conn()

        self.cur.execute('''INSERT INTO Ingredients_In_Recipes (food_id,recipe_id,quantity,total_calories,units) \
                               VALUES({},{},{},{},'{}') '''.format(foodId,recipeId,quantity,total_calories,units))
        # self.__close_conn(conn, cur)

    
    def start_conn(self):
        try:
            print(self.mysql.pool_size)
            self.conn = self.mysql.get_connection()
            self.cur = self.conn.cursor(dictionary=True)
        except errors.PoolError as e:
        # connection pool exhausted, so we can't fetch 4th connection
            print(e)
            print('Closing  connection ')


    def close_conn(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

