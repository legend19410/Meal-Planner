from flask import Blueprint
from ..system_functions import query_database

query_db = Blueprint("query_db", __name__)


@query_db.route('/get_all_measurements')
def get_all_measurements():
    query = Query(DBQuery(mysql))
    measurements = query.getAllMeasurements()
    return str(measurements)


