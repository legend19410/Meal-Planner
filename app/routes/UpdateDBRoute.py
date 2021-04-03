from flask import Blueprint
from ..system_functions import populate_database, query_database, update_database

update_db = Blueprint("update_db", __name__)

@update_db.route('/')
def index():
    update_database.insertIngredients()
    return "check db"