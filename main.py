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
    numErrors = 0

    #Check to confirm username
    if (uName == "")
        uNameError = "You must insert a username"
        ++numErrors
    else
        if (" " in uName)
            uNameError = "There can be no space"
            ++numErrors
        if (len(uName) < 3 || len(uName) > 20)
            if (uNameError == "")
                uNameError = "Username must be 3-20 characters long"
                ++numErrors
            else
                uNameError += ", Username must be 3-20 characters long"
                ++numErrors

    #Check to confirm password
    if (password == "")
        passwordError = "You must insert a password"
        ++numErrors
    else 
        if (" " in password)
            passwordError = "There can be no space"
            ++numErrors
        if (len(password) < 3 || len(password) > 20)
            if (passwordError == "")
                passwordError = "Passwod must be 3-20 characters long"
                ++numErrors
            else
                passwordError += ", Password must be 3-20 characters long"
                ++numErrors

    #Check to verify confirmpassword
    if (confirmPassword == "")
        confirmPasswordError = "You must insert a confirm password"
        ++numErrors
    else 
        if (confirmPassword == password)
            if (" " in confirmPassword)
                confirmPasswordError = "There can be no space"
                ++numErrors
            if (len(confirmPassword) < 3 || len(confirmPassword) > 20)
                if (confirmPasswordError == "")
                    confirmPasswordError = "Passwod must be 3-20 characters long"
                    ++numErrors
                else
                    confirmPasswordError += ", Password must be 3-20 characters long"
                    ++numErrors
        else
            confirmPasswordError = "Your confirm password and password do not match"
            ++numErrors

    #Check to verify e-mail
    

    
@app.route("/")
def index():
    return render_template('index.html')

app.run()