import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    # MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    # MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    # MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or  ''
    # MYSQL_DB = os.environ.get('MYSQL_DB') or 'meal_planner'
    # MYSQL_CURSORCLASS = 'DictCursor'
    UPLOAD_FOLDER = 'uploads'


dbconfig = { 
    'host': os.environ.get('MYSQL_HOST') or 'localhost',
    'user' : os.environ.get('MYSQL_USER') or 'root',
    'password' : os.environ.get('MYSQL_PASSWORD') or  '',
    'db' : os.environ.get('MYSQL_DB') or 'meal_planner'
}