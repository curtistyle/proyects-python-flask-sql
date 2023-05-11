from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)

db = MySQL(app)

config = Config()

@app.route('/', methods=['GET'])
def index():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM users")
    user = cur.fetchone()
    print(user)
    cur.close()
    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()
        if user is not None:
            session['email'] = email
            session['name'] = user[1]
            session['surname'] = user[2]
            
            return redirect(url_for('tasks'))
        else:
            return render_template('index.html', message='Las credenciales no son correctas')
    else:
        render_template('index.html')
        
@app.route('/tasks', methods=['GET'])
def tasks():
    return render_template('tasks.html')  
 
        
if __name__=='__main__':
    app.config.from_object(config)
    app.run()
    
    
