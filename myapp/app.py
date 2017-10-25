from flask import Flask
from flask import request
from flask import render_template
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ILoveGoogle'
app.config['MYSQL_DB'] = 'list'
app.config['MYSQL_HOST'] = '35.195.18.23'
mysql.init_app(app)

@app.route('/')
def statichtml(name=None):
    return render_template('list.html', name=name)

# The first route to access the webservice from http://35.190.217.3:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/list")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM todolist''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return render_template('list.html', name=str(rv))     #Return the data in a string form

@app.route("/add/<task>")
def add(task=None):
    cur= mysql.connection.cursor()
    insert_stmt = ("INSERT INTO todolist (taskDesc) VALUES (%s)")
    data=(task)
    cur.execute(insert_stmt, data)
    mysql.connection.commit()
    return render_template('list.html', name="New Record is added to the database")

@app.route("/adds", methods=['GET'])
def adds():
    name = request.args.get('task', '')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO todolist (taskDesc) values ('"+name+"')")
    mysql.connection.commit()
    return str('Success')

@app.route("/update", methods=['GET'])
def update():
    id = request.args.get('task', '')
    cur = mysql.connection.cursor()
    cur.execute("UPDATE todolist SET taskDesc = 'Wake' WHERE taskID = '"+id+"'");
    mysql.connection.commit()
    return str('Success')

@app.route("/delete", methods=['GET'])
def delete():
    name = request.args.get('task', '')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM todolist WHERE taskDesc = '"+name+"'")
    mysql.connection.commit()
    return str('Success')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
