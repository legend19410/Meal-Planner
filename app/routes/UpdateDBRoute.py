from flask import Blueprint
from ..system_functions import populate_database, query_database, update_database

import datetime

update_db = Blueprint("update_db", __name__)

@update_db.route('/')
def index():
    # update_database.insertIngredients()
    return "HOME"

@update_db.route('/insert_recipe', methods=["GET","POST"])
def insert_recipe():
    recipe = {"recipe":{ \
                "name":"some_name",\
                "added_by":200,\
                "image":"urlblob"},\
                "ingredients":[\
                    {\
                        "ingredient_id":1,\
                        "units":"cup",\
                        "quantity":11\
                    },\
                    {\
                        "ingredient_id":2,\
                        "units":'cup',\
                        "quantity":4\
                    }\
                ],\
                "instructions":[\
                    {\
                        "step_no":1,\
                        "description":"some description"\
                    }, \
                    { \
                        "step_no": 2, \
                        "description": "some description" \
                        } \
                    ]\
            }

    return str(update_database.addRecipe(recipe))

@update_db.route('/insert_user', methods=["GET","POST"])
def insert_user():
    fname = 'milton'
    lname = 'francis'
    email = 'francis@yahoo.com'
    password = '1234'
    user = {'fname':fname,'lname':lname,'email':email,'password':password}

    return str(update_database.insertUser(user))

@update_db.route('/add_to_stock', methods=["GET","POST"])
def add_to_stock():
    return str(update_database.addToKitchenStock(200201,11,'cup',13))

@update_db.route('/add_meal', methods=["GET","POST"])
def add_meal():
    userId = 200201
    recipeId = 38
    consumptionDate = datetime.datetime(2021,5,11)
    mealType = 'LUNCH'
    serving = 'curry'
    return str(update_database.addMeal(userId, recipeId, consumptionDate, serving, mealType))