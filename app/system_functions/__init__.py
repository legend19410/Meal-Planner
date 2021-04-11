#import database sql queries or prepare statements
from ..database import db_populate
from ..database import db_query
from ..database import db_update
#import system function modules
from .Populate import PopulateDatabase
from .Query import Query
from .Update import Update

#initialize system function modules
populate_database = PopulateDatabase(db_populate)
update_database = Update(db_query,db_update)
query_database = Query(db_query)