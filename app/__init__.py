from flask import Flask
# from flask_mysqldb import MySQL
from .config import Config, dbconfig
from mysql.connector import pooling


app = Flask(__name__)
app.config.from_object(Config)

mysql = pooling.MySQLConnectionPool(pool_name = 'meal_planner_cnx_pool',
                                    pool_size = 10, **dbconfig)


from app import routes
