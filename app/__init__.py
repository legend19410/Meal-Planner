from flask import Flask
from flask_login import LoginManager
# from flask_mysqldb import MySQL
from .config import Config, dbconfig
from mysql.connector import pooling


app = Flask(__name__)
app.config.from_object(Config)

mysql = pooling.MySQLConnectionPool(pool_name = 'meal_planner_cnx_pool',pool_size = 10, **dbconfig)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"  # customize the flash message category

from app import routes



#SOME default routes that is global to the app

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404