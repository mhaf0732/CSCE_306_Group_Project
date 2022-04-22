import os
from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

project_root = os.path.dirname('CSCE_306_Group_Project')
# Your path to the templates folder goes on the line below
template_path = os.path.join(project_root, 'front-end')
app = Flask('middleware', template_folder=template_path)

mydb = None
cursor = None
#def configdb():

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
except Error as e:
    print(str(e) + "YEEEEEEEEEEET Marker")
cursor = mydb.cursor()
try:
    sql_file = open("message_app.sql")
    sql_string = sql_file.read()
    sql_file.close()
    sql_commands = sql_string.split(';')
    for command in sql_commands:
        try:
            cursor.execute(command)
        except Error as e:
            print(str(e) + "YEEEEEEEET Marker")
    mydb.commit()
    print(cursor.fetchall())
except Error as e:
    print(str(e) + "YEEEEEEEEEET Marker")

@app.route('/')
def login():
    return render_template('welcome_page.html')

@app.route('/login_screen', methods = ['GET', 'POST'])
def loginpage():
    if request.method == 'GET':
        request.form
        return render_template("login_screen.html")

@app.route('/signup_screen', methods = ['GET', 'POST'])
def signup_screen():
    if request.method == 'GET':
        request.form
        return render_template("signup_screen.html")
    if request.method == 'POST':
        form = request.form
        user = form['username']
        upass = form['password']
        uemail = form['email']
# Verify the account does not exist
        try:
            print(str(user) + " " + str(upass) + " " + str(uemail))
            sql_string = "SELECT * FROM profile WHERE email='" + str(uemail) + "';"
            cursor.execute(sql_string)
            if cursor.fetchall() == []:
                print("good")
            else:
                return render_template("login_screen.html")
        except Error as e:
            print(str(e) + " YEEEEEEEEEET Marker")
        try:
            sql_string = "SELECT * FROM credentials WHERE username='" + str(user) + "';"
            cursor.execute(sql_string)
            if cursor.fetchall() == []:
                print("good")
            else:
                return render_template("login_screen.html")
        except Error as e:
            print(str(e) + " YEEEEEEEEEET Marker")
        try:
            sql_string = "insert into credentials (username,password) values('" + str(user) + "','" + str(upass) + "');"
            cursor.execute(sql_string)
            sql_string = "SELECT * FROM credentials WHERE username='" + str(user) + "';"
            cursor.execute(sql_string)
            print(cursor.fetchall())
        except Error as e:
            print(str(e) + " YEEEEEEEEEET Marker")
        mydb.commit()
    return render_template('welcome_page.html')

@app.route('/chat_screen', methods = ['GET', 'POST'])
def chat_screen():
    if request.method == 'GET':
        request.form
        return render_template("chat_screen.html")

@app.route('/dashboard_screen', methods = ['GET', 'POST'])
def dashboard_screen():
    if request.method == 'GET':
        request.form
        return render_template("dashboard_screen.html")

@app.route('/forgot_password_screen', methods = ['GET', 'POST'])
def forgot_password_screen():
    if request.method == 'GET':
        request.form
        return render_template("forgot_password_screen.html")

@app.route('/inbox-screen', methods = ['GET', 'POST'])
def inbox_screen():
    if request.method == 'GET':
        request.form
        return render_template("inbox-screen.html")

@app.route('/new_message-screen', methods = ['GET', 'POST'])
def new_message_screen():
    if request.method == 'GET':
        request.form
        return render_template("new_message-screen.html")

@app.route('/personal_profile_screen', methods = ['GET', 'POST'])
def personal_profile_screen():
    if request.method == 'GET':
        request.form
        return render_template("personal_profile_screen.html")

@app.route('/profile_search-screen', methods = ['GET', 'POST'])
def profile_search_screen():
    if request.method == 'GET':
        request.form
        return render_template("profile_search-screen.html")

@app.route('/userprofile-screen', methods = ['GET', 'POST'])
def userprofile_screen():
    if request.method == 'GET':
        request.form
        return render_template("userprofile-screen.html")

if __name__ == "__main__":
#    configdb()
    app.run(debug=True)
    