class DBUpdate:

    def __init__(self, mysql):

        self.mysql = mysql
        self.cur = mysql.connection.cursor()

    def insertRecipe(self, recipeId, recipeName, userMarker):
        '''create recipe with id and name'''
        self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                         format(recipeId, recipeName, userMarker))
        self.mysql.connection.commit()