from flask import Flask, render_template, request, session, redirect, url_for
import config
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

db = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    
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
        return render_template('index.html', message="Las credenciales no son correctas")
        
@app.route('/tasks', methods=['GET'])
def tasks():
    email = session['email']
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE email = %s", [email])
    tasks = cur.fetchall()
    
    insertObject = []
    columNames = [column[0] for column in cur.description]
    for record in tasks:
        insertObject.append(dict(zip(columNames, record)))
    cur.close()    
       
    
    return render_template('tasks.html', tasks = insertObject)

@app.route("/loguot")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/new-task", methods=['POST'])
def newTask():
    title = request.form['title']
    description = request.form['description']
    email = session['email']
    d = datetime.now()
    dateTask = d.strftime("%Y-%m-%d %H:%M:%S")
    
    if title and description and email:
        cur = db.connection.cursor()
        query = "INSERT INTO tasks (email, title, description, date_task) VALUES (%s, %s, %s, %s)"
        values = (email, title, description, dateTask)
        cur.execute(query, values)
        db.connection.commit()
    return redirect(url_for('tasks'))

@app.route("/new-user", methods=['POST'])
def newUser():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password = request.form['password']
    
    if name and surname and email and password:
        cur = db.connection.cursor()
        query = "INSERT INTO users (name, surnames, email, password) VALUES (%s, %s, %s, %s)"
        values = (name, surname, email, password)
        cur.execute(query, values)
        db.connection.commit()
    
    return redirect(url_for('tasks'))

@app.route("/delete-task", methods=['POST'])
def deteleTask():
    cur = db.connection.cursor()
    id = request.form['id']
    print(id)
    query = "DELETE FROM tasks WHERE id = %s"
    values = (id,)
    cur.execute(query, values)
    db.connection.commit()
    
    return redirect(url_for("tasks"))

if __name__=="__main__":
    app.run(debug="True")
    