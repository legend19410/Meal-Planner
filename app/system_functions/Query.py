class Query:

    def __init__(self, dbQuery):
        self.dbQuery = dbQuery

    def getAllMeasurements(self):
        return self.dbQuery.getAllMeasurments()

    def getUser(self,id=None, email=None):
        return self.dbQuery.getUser(id,email)

    def getRecipe(self,recipeId):
        recipe = self.dbQuery.getRecipe(recipeId)
        instructions = self.dbQuery.getInstructionForRecipe(recipeId)
        ingredients = self.dbQuery.getIngredientsForRecipe(recipeId)
        return {'recipe':recipe,'instructions':instructions,'ingredients':ingredients}

    def getRecipesOfCalCount(self, calCount):
        pass

    def getKitchenStock(self):
        pass