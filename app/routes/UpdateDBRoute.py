from flask import Blueprint
from ..system_functions import update_database

update_db = Blueprint("update_db", __name__)


@update_db.route('/')
def index():
    pass