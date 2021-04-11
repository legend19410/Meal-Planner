from app import mysql
from .DBPopulate import DBPopulate
from .DBQuery import DBQuery
from .DBUpdate import DBUpdate

db_populate = DBPopulate(mysql)
db_query = DBQuery(mysql)
db_update= DBUpdate(mysql)