class Update:

    def __init__(self, dbQuery, dbUpdate):
        self.dbQuery = dbQuery
        self.dbUpdate = dbUpdate

    def addRecipe(self,recipe):

        details = recipe['recipe']
        instructions = recipe['instructions']
        ingredients = recipe['ingredients']

        recipeId = self.dbQuery.getMaxRecipeId() + 1
        self.dbUpdate.insertRecipe(recipeId, details['name'],int(details['added_by']))
        if recipeId:
            for ingredient in ingredients:
                self.dbUpdate.insertIngredients(ingredient['ingredient_id'],recipeId,ingredient['units'],ingredient['quantity'])
            for instruction in instructions:
                self.dbUpdate.insertInstruction(recipeId,instruction['step_no'],instruction['description'])
        recipe = self.dbQuery.getRecipe(recipeId)
        instructions = self.dbQuery.getInstructionForRecipe(recipeId)
        ingredients = self.dbQuery.getIngredientsForRecipe(recipeId)
        return {'recipe': recipe, 'cal_count':self.dbQuery.getCalCount(recipeId),'instructions': instructions, 'ingredients': ingredients}

    def insertUser(self, user):
        fname = user['fname']
        lname = user['lname']
        email = user['email']
        password = user['password']

        self.dbUpdate.insertUser(fname,lname,email,password)
        userId = self.dbQuery.getMaxUserId()
        return self.dbQuery.getUserById(userId)

    def addToKitchenStock(self,userId,foodId,units,quantity):

        self.dbUpdate.insertFoodInKitchenStock(int(userId),int(foodId),units,quantity)
        return self.dbQuery.getMyStock(int(userId))

    def addMeal(self,userId,recipeId,consumptionDate,serving,mealType):

        self.dbUpdate.insertMeal(int(userId),int(recipeId),consumptionDate,serving,mealType)
        return self.dbQuery.getMealForDate(int(userId),consumptionDate)








