from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL
from cfg import Config_db
from jinja2 import *
from methods import input_band

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def Index():
    input_band()
    return render_template('index.html')

@app.route('/list')
def List():
    return render_template('list.html')

@app.route('/search')
def Search():
    
    return redirect('Index')

if __name__=='__main__':
    app.config.from_object(Config_db)
    app.run()

