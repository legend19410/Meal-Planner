from .DB import DB
from mysql.connector import errors

class DBUpdate(DB):

    def __init__(self, mysql):
        super(DBUpdate,self).__init__(DB)
        self.mysql = mysql

    def insertRecipe(self, recipeId, recipeName, userMarker):
        '''create recipe with id and name'''
        self._start_conn()
        try:
            self.cur.execute('''INSERT INTO recipe (recipe_id,recipe_name,added_by) VALUES({},'{}',{})'''. \
                            format(recipeId, recipeName, userMarker))
            result = True
        except errors.IntegrityError:
            result = False
        finally:
            self._close_conn()
            return result
