from flask import Blueprint

populate_db = Blueprint("populate_db", __name__)
from app import mysql
from system_functions.Populate import PopulateDatabase
from database.DBPopulate import DBPopulate


@populate_db.route('/populate_users')
def populate_users():
    populateDB = PopulateDatabase(DBPopulate(mysql))
    populateDB.populateUsers()
    return "check user's table in db"

@populate_db.route('/populate_units')
def populate_units():
    populateDB = PopulateDatabase(DBPopulate(mysql))
    populateDB.populateUnits()
    return "check units table in db"

@populate_db.route('/populate_recipes')
def populate_recipes():
    populateDB = PopulateDatabase(DBPopulate(mysql))
    populateDB.populateRecipes()
    return "check recipes table"