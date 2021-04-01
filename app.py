from flask import Flask
from extension import mysql
from routes.PopulateDBRoute import populate_db
from routes.UpdateDBRoute import update_db
from routes.QueryDBRoute import query_db
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

'''create flask app'''
app = Flask(__name__)

'''connect to mysql database'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'meal_planner'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)

'''register blueprints'''
app.register_blueprint(populate_db, url_prefix="/populate_db")
app.register_blueprint(update_db, url_prefix="/update_db")
app.register_blueprint(query_db, url_prefix="/query_db")


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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
