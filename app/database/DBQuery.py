class DBQuery:

    def __init__(self, mysql):

        self.mysql = mysql
        self.cur = mysql.connection.cursor()

    def getAllMeasurments(self):
        self.cur.execute('''SELECT * FROM Measurement''')
        return self.cur.fetchall()