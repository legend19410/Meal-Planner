from flask import Blueprint
from ..system_functions import populate_database

populate_db = Blueprint("populate_db", __name__)

@populate_db.route('/populate_users')
def populate_users():
    populate_database.start_conn()
    populate_database.populateUsers()
    populate_database.close_conn()
    return "check user's table in db"

@populate_db.route('/populate_units')
def populate_units():
    populate_database.start_conn()
    populate_database.populateUnits()
    populate_database.close_conn()
    return "check units table in db"

@populate_db.route('/populate_recipes')
def populate_recipes():
    populate_database.start_conn()
    populate_database.populateRecipes()
    populate_database.close_conn()
    return "check recipes table"