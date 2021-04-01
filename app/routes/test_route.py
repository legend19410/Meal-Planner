from flask import Blueprint, Flask, render_template, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#app imports
from ..system_functions import populate_database

test_app = Blueprint("test_app", __name__)

#JASON TEST routes, will soon create a blueprint for this
@test_app.route('/')
def index():
    return render_template("index.html")

@test_app.route('/login')
def login():
    return render_template("login.html")

@test_app.route('/sign-up')
def signup():
    return render_template("sign_up.html")

@test_app.route('/recipe/<recipe_name>')
def recipe(recipe_name):
    return render_template("recipe.html", recipe_name=recipe_name)


@test_app.route('/add-recipe')
def add_recipe():
    return render_template("input_recipe.html")

@test_app.route('/create')
def create():
    return render_template("create_mplan.html")