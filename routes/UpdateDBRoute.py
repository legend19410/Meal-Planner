from flask import Blueprint

update_db = Blueprint("update_db", __name__)

@update_db.route('/')
def index():
    pass