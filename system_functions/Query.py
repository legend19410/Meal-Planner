class Query:

    def __init__(self, dbQuery):
        self.dbQuery = dbQuery

    def getAllMeasurements(self):
        return self.dbQuery.getAllMeasurments()

