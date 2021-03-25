from flask import Flask
from flask_mysqldb import MySQL
from .config import Config
from routes.PopulateDBRoute import populate_db
from routes.UpdateDBRoute import update_db
from routes.QueryDBRoute import query_db


app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

from app import routes
