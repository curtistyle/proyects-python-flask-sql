from flask import Flask
from flask import render_template, url_for, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb
from decouple import config
from config import DevelopmentConfig, Config


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = MySQL(app)


@app.route("/")
def Index():
    # print (db.connection())
    # print(config('MYSQL_HOST'), config('MYSQL_USER'), config('MYSQL_PASSWORD'), config('MYSQL_DB'))
    cur = db.connection.cursor()
    cur.execute('''SELECT * FROM contacts''')
    for item in cur.fetchone():
        print(item)
    return "<h1>Bienvenidos</h1>"

#   https://www.youtube.com/watch?v=QO4lBskfH7w
#   https://www.youtube.com/watch?v=pkotA0tvewQ&list=WL&index=2
if __name__=='__main__':
    app.run(debug=True)