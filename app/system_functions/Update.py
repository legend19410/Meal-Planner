class Update:

    def __init__(self, dbQuery, dbUpdate):
        self.dbQuery = dbQuery
        self.dbUpdate = dbUpdate

    def addRecipe(self, request):

        #extract request
        #add recipe to db
        #self.dbUpdate.insertRecipe()
        pass

    def insertIngredients(self):
        foodId = 300
        recipeId = 38
        units = 'cup'
        quantity = 2.0
        self.dbUpdate.insertIngredients(foodId, recipeId,units,quantity)