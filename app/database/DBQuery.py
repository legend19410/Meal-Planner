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
    
    def getUser(self, username):
        self._start_conn()
        query = '''SELECT * FROM user WHERE username={}'''.format(username)
        self.cur.execute(query)
        user = self.cur.fetchone()
        self._close_conn()
        return user