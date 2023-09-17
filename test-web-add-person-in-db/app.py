from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from cfg import Config_db
from jinja2 import *
from methods_spotify import search_albums_for_artist, generate_dic, set_dict_in_json, get_dict_in_json, get_pos, test_set_dic


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
    """ requests """
    tracks_selects = request.form.getlist('tracks_select')
    list_select = request.form.get('camp_select')
    
    """ returns the position of the searched element """
    pos = get_pos(list_select)
    
    data = get_dict_in_json('list_band.json')
    
    """ add list selected and tracks selected in dict `list_tracks`"""
    dict_list = generate_dic(tracks_selects, list_select)
    
    #data['list_band'][pos]['list_tracks'].append(dict_list)
    #data['list_band'][pos]['list_tracks'].append(tracks_selects)
    
    for item in dict_list:
        data['list_band'][pos]['list_tracks'].append(item)
    
    """set dict in json file"""
    test_set_dic(data)
    # dict_list = generate_dic(tracks_selects, list_select)
    # set_dict_in_json(dict_list)
    return redirect(url_for('Index'))

@app.route('/create_list', methods=['GET','POST'])
def Create_List():
    if request.method == 'GET':
        return render_template('create_list.html')
    if request.method == 'POST':

        """get name and description of the list"""
        name = request.form['name']
        
        description = request.form['description']
        print('>>>>>',name, description)
        info = {'id' : None, 'name' : None, 'user' : None, 'key' : None, 'description' : None, 'list_tracks': []}
        
        
        info['name'] = name
        info['description'] = description
        
        print(info)
        """save new list in json file"""
        set_dict_in_json(info)
        
        return render_template('index.html')

@app.route('/search', methods=['GET'])
def Search():
    get_name = request.args['name']
    response = search_albums_for_artist(get_name)

    
    data = get_dict_in_json('list_band.json')
    print(data)
    return render_template('search2.html', albums=response, artist=get_name, band_list=data) # , band_list=data

@app.route('/view_list', methods=['GET'])
def View_List():
    if request.method == 'GET':
        data = get_dict_in_json('list_band.json')
        print(data)
        return render_template('view_list.html',lists_band = data)


@app.route('/list')
def List():
    return render_template('list.html')

if __name__=='__main__':
    app.config.from_object(Config_db)
    app.run()

