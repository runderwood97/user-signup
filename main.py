from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods = ['POST'])
def check():
    uName = request.userInfo["uName"]
    eMail = request.userInfo["eMail"]
    password = request.userInfo["password"]
    confirmPassword = request.userInfo["confirmPassword"]
    uNameError = ""
    eMailError = ""
    passwordError = ""
    confirmPasswordError = ""

    if (uName == "")
        uNameError = "You must insert a username"
    if (password == "")
        passwordError = "You must insert a password"
    if (confirmPassword == "")
        confirmPasswordError = "You must insert a confirm password"

    

@app.route("/")
def index():
    return render_template('index.html')

app.run()