from flask import *
import pymysql

app = Flask(__name__)

def database_connection():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='registerdata',
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def hello_world():
    return render_template('Home.html')

@app.route('/insertData')
def insert():
    return render_template('Register.html')

@app.route('/insertData',methods=["POST"])
def register():
    firstname=request.form['rfn']
    lastname=request.form['rln']
    username=request.form['run']
    password=request.form['rpw']
    hobby=request.form.getlist('rho')
    address=request.form['radd']

    hobby="-".join(hobby)

    connection=database_connection()
    cursor1=connection.cursor()
    cursor1.execute("INSERT INTO register(firstName,lastName,userName,password,hobby,address) VALUES ('"+firstname+"','"+lastname+"','"+username+"','"+password+"','"+hobby+"','"+address+"')")
    connection.commit()
    cursor1.close()
    connection.close()
    return render_template('Home.html')

@app.route('/Show')
def show():
    connection=database_connection()
    cursor2=connection.cursor()
    cursor2.execute("SELECT * FROM register ")
    data=cursor2.fetchall()
    print(data)
    connection.commit()
    cursor2.close()
    connection.close()
    return render_template("Show.html",data=data)


app.run(threaded=True,debug=True)
