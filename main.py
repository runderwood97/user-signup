from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods = ['POST'])
def check():
    uName = request.form["uName"]
    eMail = request.form["eMail"]
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]
    uNameError = ""
    eMailError = ""
    passwordError = ""
    confirmPasswordError = ""
    numErrors = 0

    #Check to confirm username
    if uName == "":
        uNameError = "You must insert a username"
        ++numErrors
    else:
        if " " in uName:
            uNameError = "There can be no space"
            ++numErrors
        if len(uName) < 3 or len(uName) > 20:
            if uNameError == "":
                uNameError = "Username must be 3-20 characters long"
                ++numErrors
            else:
                uNameError += ", Username must be 3-20 characters long"
                ++numErrors

    #Check to confirm password
    if password == "":
        passwordError = "You must insert a password"
        ++numErrors
    else:
        if " " in password:
            passwordError = "There can be no space"
            ++numErrors
        if len(password) < 3 or len(password) > 20:
            if passwordError == "":
                passwordError = "Passwod must be 3-20 characters long"
                ++numErrors
            else:
                passwordError += ", Password must be 3-20 characters long"
                ++numErrors

    #Check to verify confirmpassword
    if confirmPassword == "":
        confirmPasswordError = "You must insert a confirm password"
        ++numErrors
    else:
        if confirmPassword == password:
            if " " in confirmPassword:
                confirmPasswordError = "There can be no space"
                ++numErrors
            if len(confirmPassword) < 3 or len(confirmPassword) > 20:
                if confirmPasswordError == "":
                    confirmPasswordError = "Passwod must be 3-20 characters long"
                    ++numErrors
                else:
                    confirmPasswordError += ", Password must be 3-20 characters long"
                    ++numErrors
        else:
            confirmPasswordError = "Your confirm password and password do not match"
            ++numErrors

    #Check to verify e-mail
    if eMail != "":
        if " " in eMail:
            eMailError = "Your e-mail can not contain a space"
            ++numErrors
        if len(eMail) < 3 or len(eMail) > 20:
            if eMailError == "":
                eMailError = "Your e-mail must be 3-20 characters long"
                ++numErrors
            else:
                eMailError += ", Your e-mail must be 3-20 characters long"
                ++numErrors

        for letter in eMail:
            atSignFound = False
            dotFound = False

            if letter == "@":
                if atSignFound == False:
                    atSignFound = True
                else:
                    if eMailError == "":
                        eMailError = "You can only have one @ in your e-mail"
                        ++numErrors
                    else: 
                        eMailError += ", You can only have one @ in your e-mail"
                        ++numErrors
            if letter == ".":
                if dotFound == False:       
                    dotFound = True
                else: 
                    if eMailError == "":
                        eMailError = "You can only have one . in your e-mail"
                        ++numErrors
                    else:
                        eMailError += ", You can only have one . in your e-mail"
                        ++numErrors    

    #checking to see if any errors were caught and then deciding which template to return
    if numErrors == 0:
        return render_template("welcome.html", uName = uName)
    else:
        return render_template("index.html", uName = uName, eMail = eMail, uNameError = uNameError, eMailError = eMailError, passwordError = passwordError, confirmPasswordError = confirmPasswordError)
                
@app.route("/")
def index():
    return render_template('index.html')

app.run()