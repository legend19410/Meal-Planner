from flask import Blueprint
from ..system_functions import populate_database

populate_db = Blueprint("populate_db", __name__)

@populate_db.route('/populate_users')
def populate_users():
    populate_database.populateUsers()
    return "check user's table in db"

@populate_db.route('/populate_units')
def populate_units():
    populate_database.populateUnits()
    return "check units table in db"

@populate_db.route('/populate_recipes')
def populate_recipes():
    populate_database.populateRecipes()
    return "check recipes table"