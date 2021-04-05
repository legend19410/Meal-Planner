from flask import Blueprint
from ..system_functions import query_database

import datetime

query_db = Blueprint("query_db", __name__)

start_index = 0
increment_by = 25


@query_db.route('/get_n_recipes')
def get_n_recipes():
    global start_index
    recipes = query_database.getNRecipes(start_index, increment_by)
    start_index += increment_by
    return str([recipe['recipe_name'] for recipe in recipes])

@query_db.route('/reset_index')
def reset_index():
    global start_index
    start_index = 0
    return 'Reset'


@query_db.route('/get_all_measurements')
def get_all_measurements():
    query = Query(DBQuery(mysql))
    measurements = query.getAllMeasurements()
    return str(measurements)

@query_db.route('/get_recipe')
def get_recipe():
   return str(query_database.getRecipeByName('low fat berry blue frozen dessert'))

@query_db.route('/get_meal_plan')
def get_meal_plan():

    user = 1
    startDate = datetime.datetime(2021,4,1)
    endDate = datetime.datetime(2021, 4, 15)

    return str(query_database.getMealPlan(user,startDate,endDate))

@query_db.route('/generate_lst')
def generate_lst():

    user = 1
    startDate = datetime.datetime(2021,4,1)
    endDate = datetime.datetime(2021, 4, 15)

    return str(query_database.generateSupermarketList(user,startDate,endDate))

@query_db.route('/get_ing')
def get_ing():

    return str(query_database.getIngredients(38))

@query_db.route('/get_cal_count')
def get_cal_count():

    return str(query_database.getCalCount(910198))

@query_db.route('/get_ran_rec')
def get_ran_rec():

    return str(query_database.getRandomRecipe())


@query_db.route('/get_lst')
def get_lst():

    return str(query_database.genLst(38))