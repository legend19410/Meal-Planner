class Query:

    def __init__(self, dbQuery):
        self.dbQuery = dbQuery

    def getAllMeasurements(self):
        return self.dbQuery.getAllMeasurments()

    def getUser(self,id=None, email=None):
        return self.dbQuery.getUser(id,email)