
class Query:

    def __init__(self, dbQuery):
        self.dbQuery = dbQuery

    def getAllMeasurements(self):
        return self.dbQuery.getAllMeasurments()

    def getUser(self,id=None, email=None):
        return self.dbQuery.getUser(id,email)

    def getRecipe(self,recipeId):
        recipe = self.dbQuery.getRecipe(int(recipeId))
        instructions = self.dbQuery.getInstructionForRecipe(int(recipeId))
        ingredients = self.dbQuery.getIngredientsForRecipe(int(recipeId))
        return {'recipe':recipe,'cal_count':self.dbQuery.getCalCount(int(recipeId)),'instructions':instructions,'ingredients':ingredients}

    def getMealPlan(self,user,startDate,endDate):
        mealPlan = self.dbQuery.getMealInRange(int(user),startDate,endDate)
        if len(mealPlan) > 0:
            for meal in mealPlan:
                meal['cal_count'] = self.dbQuery.getCalCount(int(meal['recipe_id']))
        return mealPlan

    def getMealsForDate(self,userId, date):
        mealPlan =  self.dbQuery.getMealsForDate(int(userId),date)
        if len(mealPlan) > 0:
            for meal in mealPlan:
                meal['cal_count'] = self.dbQuery.getCalCount(int(meal['recipe_id']))
        return mealPlan

    def getKitchenStock(self,userId):
        return self.dbQuery.getMyStock(int(userId))

    def generateSupermarketList(self,userId,startDate,endDate):
        mealPlan = self.dbQuery.getMealInRange(int(userId),startDate,endDate)
        superLst = set()
        if len(mealPlan) > 0:
            for meal in mealPlan:
                ingr_lst = self.dbQuery.generateSupermarketList(meal['recipe_id'])
                for el in ingr_lst:
                    superLst.add(el['food_name'])
        return list(superLst)

    def getRandomRecipe(self):
        recipe = self.dbQuery.getRandomRecipe()
        instructions = self.dbQuery.getInstructionForRecipe(int(recipe['recipe_id']))
        ingredients = self.dbQuery.getIngredientsForRecipe(int(recipe['recipe_id']))
        return {'recipe': recipe, 'cal_count': self.dbQuery.getCalCount(recipe['recipe_id']), 'instructions': instructions,\
                'ingredients': ingredients}

    def getNRecipes(self,start,end):
        return self.dbQuery.getNRecipes(start,end)
    
    def getNFoodItems(self,start,end):
        return self.dbQuery.getNFoodItems(start,end)

    def getRecipeByName(self,recipeName):
        return self.dbQuery.getRecipeByName(recipeName)

    '''These were written just testing'''
    def genLst(self,rec):
        return self.dbQuery.generateSupermarketList(rec)

    def getRecipesOfCalCount(self, calCount):
        pass

    def getIngredients(self,recipeId):
        return self.dbQuery.getIngredientsForRecipe(int(recipeId))

    def getInstructions(self,recipeId):
        return self.dbQuery.getInstructionForRecipe(int(recipeId))

    def getCalCount(self,recipeId):
        return [self.dbQuery.getCalCount(recipeId),self.getIngredients(recipeId)]




