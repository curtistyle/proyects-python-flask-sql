from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL
from cfg import Config_db
from jinja2 import *

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')



if __name__=='__main__':
    app.config.from_object(Config_db)
    app.run()
