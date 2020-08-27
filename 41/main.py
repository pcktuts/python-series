# pip install flask, pip instal mysql.connector
from flask import Flask, render_template, url_for, request
app = Flask(__name__)
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4b3#U>6@S^SLeJn",
    database="learn_sql"
)

mycursor = mydb.cursor(dictionary=True)



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':   
        return render_template('login.html')

    email = request.form['email']
    password = request.form['pwd']
    print(email, password)        
    sql = "SELECT * FROM learn_sql.users WHERE email= '"+ email +"' AND password = '"+ password +"';"
    print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    mydb.commit()
    print(mycursor.rowcount)
    if mycursor.rowcount > 0:
        return "login success"

    return "login failed"
    

