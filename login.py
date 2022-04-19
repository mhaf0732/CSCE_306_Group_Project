import os
from flask import Flask, request, render_template
from cryptography.fernet import Fernet

project_root = os.path.dirname(__file__)
# Your path to the templates folder goes on the line below
template_path = os.path.join(project_root, 'Your_Path_Here')
app = Flask(__name__, template_folder=template_path)

# generates the key used in encrypting and decrypting a given string
key = Fernet.generate_key()
fernet = Fernet(key)

@app.route('/')
def login():
    return render_template('loginorcreate.html')

@app.route('/loginpage', methods = ['POST'])
def loginpage():
    if request.method == 'POST':
        request.form
        return render_template("loginpage.html")

@app.route('/createacct', methods = ['POST'])
def createacct():
    if request.method == 'POST':
        request.form
        return render_template("createacct.html")

# This is for logging in
@app.route('/profile', methods = ['POST'])
def profile():
    if request.method == 'POST':
        usr_data = request.form["user"] # uses the name attribute of the html input as the key because form data is saved as dict
        pass_data = request.form["pass"] # uses the name attribute of the html input as the key because form data is saved as dict
        
        # open file fore reading and writing
        file = open("credentials.txt", "r+")

        # creates account by writing to an empty text file
        if (os.stat("credentials.txt").st_size == 0 and len(usr_data) < 20 and len(pass_data) < 20):
            file.write(usr_data + "\n")
            file.write(pass_data + "\n")

            file.close()

            return render_template("profile.html", username=usr_data)
        else:
            usr = file.readline().rstrip("\n")
            passwrd = file.readline().rstrip("\n")

            file.close()

        # print statement for debugging
        print(usr_data)
        print(pass_data)
        print(usr)
        print(passwrd)
    # used for logging into the page
    if (usr_data == usr and pass_data == passwrd):
        return render_template("profile.html", username=usr_data)
    else:
        return render_template("loginpage.html")


### For quick debugging purposes ###
# Username: sampleuser123
# Password: secretpasswrd123
### For quick debugging purposes ###


if __name__ == "__main__":
    app.run(debug=True)