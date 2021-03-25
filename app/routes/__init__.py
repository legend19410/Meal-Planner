
from app import app
from flask import Flask, render_template
from flask import session

"""import blueprints (routes) for different sections of the system"""
from .PopulateDBRoute import populate_db
from .UpdateDBRoute import update_db
from .QueryDBRoute import query_db

"""register blueprints"""
app.register_blueprint(populate_db, url_prefix="/populate_db")
app.register_blueprint(update_db, url_prefix="/update_db")
app.register_blueprint(query_db, url_prefix="/query_db")


@app.route('/')
def index():
    return "HOME"
