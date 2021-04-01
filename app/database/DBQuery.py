from .DB import DB

class DBQuery(DB):

    def __init__(self, mysql):
        super(DBQuery,self).__init__(DB)
        self.mysql = mysql

    def getAllMeasurments(self):
        self.cur.execute('''SELECT * FROM Measurement''')
        return self.cur.fetchall()