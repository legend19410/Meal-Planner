
from app import app
from flask import Flask, render_template, flash
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

"""import blueprints (routes) for different sections of the system"""
from .PopulateDBRoute import populate_db
from .UpdateDBRoute import update_db
from .QueryDBRoute import query_db

"""register blueprints"""
app.register_blueprint(populate_db, url_prefix="/populate_db")
app.register_blueprint(update_db, url_prefix="/update_db")
app.register_blueprint(query_db, url_prefix="/query_db")


#JASON TEST routes, will soon create a blueprint for this
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/sign-up')
def signup():
    return render_template("sign_up.html")

@app.route('/recipe/<recipe_name>')
def recipe(recipe_name):
    return render_template("recipe.html", recipe_name=recipe_name)


@app.route('/add-recipe')
def add_recipe():
    return render_template("input_recipe.html")

@app.route('/create')
def create():
    return render_template("create_mplan.html")

# @app.route('/')
# def index():
#     return "HOME"
