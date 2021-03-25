#import database sql queries or prepare statements
from ..database import db_populate
# from ..database import db_query
# from ..database import db_update
#import system function modules
from .Populate import PopulateDatabase
# from .Query import 
# from .Update import 

#initialize system function modules
populate_database = PopulateDatabase(db_populate)