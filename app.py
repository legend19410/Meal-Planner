import pandas as pd
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'meal_planner'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    df = pd.read_csv('RAW_recipes.csv')
    count = 1
    ing = ''
    inst = ''
    for ind in df.index:
        #     print(df['name'][ind], df['ingredients'][ind])

        ing = df['ingredients'][ind]
        inst = df['steps'][ind]

        if count == 1:
            break
        count = count + 1
    lst = lst.strip('][').split(', ')
    type(lst)
    return str(lst)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")