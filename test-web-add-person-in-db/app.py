from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from cfg import Config_db
from jinja2 import *
from methods_spotify import search_albums_for_artist, generate_dic


app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def Index():
    #input_band()
    return render_template('index.html')

@app.route('/lista', methods=['POST'])
def Lista():
    seleccionados = []

    seleccionados = request.form.getlist('lista')
    # print(">>>",seleccionados)
    # for select in seleccionados:
    #     print(f" '{select}'")
    seleccionados= generate_dic(seleccionados)
    print(seleccionados)
    return render_template('index.html')



@app.route('/search')
def Search():
    get_name = request.args['name']
    response = search_albums_for_artist(get_name)
    return render_template('index.html', albums=response, artist=get_name)

if __name__=='__main__':
    app.config.from_object(Config_db)
    app.run()

