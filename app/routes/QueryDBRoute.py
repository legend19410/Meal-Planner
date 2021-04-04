from flask import Blueprint
from ..system_functions import query_database

import datetime

query_db = Blueprint("query_db", __name__)


@query_db.route('/get_all_measurements')
def get_all_measurements():
    query = Query(DBQuery(mysql))
    measurements = query.getAllMeasurements()
    return str(measurements)

@query_db.route('/get_recipe')
def get_recipe():
   return str(query_database.getRecipe(38))

@query_db.route('/get_meal_plan')
def get_meal_plan():

    user = 1
    startDate = datetime.datetime(2021,4,1)
    endDate = datetime.datetime(2021, 4, 15)

    return str(query_database.getMealPlan(user,startDate,endDate))