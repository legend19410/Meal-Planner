from flask import Flask
# from flask_mysqldb import MySQL
from .config import Config, dbconfig
from mysql.connector import pooling


app = Flask(__name__)
app.config.from_object(Config)

mysql = pooling.MySQLConnectionPool(pool_name = 'meal_planner_cnx_pool',
                                    pool_size = 10, **dbconfig)
# mysql.set_config(**dbconfig)
print(repr(mysql))
# print('dbconfig',mysql.get_connection())
# mysql = MySQL(app)
# print('Config User', app.config['MYSQL_USER'])
# print('Config Pswd', app.config['MYSQL_PASSWORD'])
# print('Congif DB', app.config['MYSQL_DB'])
# with app.app_context():
#     cur = mysql.connection.cursor()
#     print('Connectinon', mysql.connection)

from app import routes
