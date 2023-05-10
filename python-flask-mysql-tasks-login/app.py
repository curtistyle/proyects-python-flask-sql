from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)

db = MySQL(app)

config = Config()

@app.route('/', methods=['GET'])
def Index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        
if __name__=='__main__':
    app.config.from_object(config)
    app.run()
    