from flask import redirect, url_for, send_from_directory
from app import app

"""import blueprints (routes) for different sections of the system"""
from .PopulateDBRoute import populate_db
from .UpdateDBRoute import update_db
from .QueryDBRoute import query_db
from .user_route import user

"""register blueprints"""
app.register_blueprint(populate_db, url_prefix="/populate_db")
app.register_blueprint(update_db, url_prefix="/update_db")
app.register_blueprint(query_db, url_prefix="/query_db")
app.register_blueprint(user, url_prefix="/user")


@app.route('/')
def index():
    return redirect(url_for('user.index'))

