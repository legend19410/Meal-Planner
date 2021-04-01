from flask import Blueprint
# from ..system_functions import

query_db = Blueprint("query_db", __name__)

from system_functions.Query import Query
from database.DBQuery import DBQuery

@query_db.route('/get_all_measurements')
def get_all_measurements():
    query = Query(DBQuery(mysql))
    measurements = query.getAllMeasurements()
    return str(measurements)


