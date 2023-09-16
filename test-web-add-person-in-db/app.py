from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from cfg import Config_db
from jinja2 import *
from methods_spotify import search_albums_for_artist, generate_dic, set_dict_in_json, get_dict_in_json


app = Flask(__name__)

db = MySQL(app)

lista = []

@app.route('/')
def Index():
    #input_band()
    #get_dict_in_json('list_band.json')
    
    return render_template('search.html')

@app.route('/lista', methods=['POST'])
def Lista():
    seleccionados = []

    seleccionados = request.form.getlist('lista')
    # print(">>>",seleccionados)
    # for select in seleccionados:
    #     print(f" '{select}'")
    seleccionados = generate_dic(seleccionados)
    print(seleccionados)
    return render_template('index.html')

@app.route('/create_list', methods=['GET','POST'])
def Create_List():
    if request.method == 'GET':
        return render_template('create_list.html')
    if request.method == 'POST':

        name = request.form['name']
        description = request.form['description']
        info = {'id' : None, 'name' : None, 'user' : None, 'key' : None, 'description' : None, 'list_tracks': None}
        
        
        info['name'] = name
        info['description'] = description
        
        set_dict_in_json(info)
        return render_template('index.html')

    

@app.route('/search', methods=['GET'])
def Search():
    get_name = request.args['name']
    response = search_albums_for_artist(get_name)
    
    data = get_dict_in_json('list_band.json')
    return render_template('search.html', albums=response, artist=get_name, band_list=data)

@app.route('/list')
def List():
    return render_template('list.html')

if __name__=='__main__':
    app.config.from_object(Config_db)
    app.run()

