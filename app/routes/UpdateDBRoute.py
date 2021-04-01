from flask import Blueprint
# from ..system_functions import 

update_db = Blueprint("update_db", __name__)

from system_functions.Update import Update
from database.DBQuery import DBQuery
from database.DBUpdate import DBUpdate

@update_db.route('/')
def index():
    pass