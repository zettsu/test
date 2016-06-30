from datetime import datetime
import re
from flask import Flask, request,flash, redirect, render_template, session, json

app = Flask(__name__)
app.config.from_pyfile('../configs/app.cfg')

@app.route('/')
@app.route('/dash')
def main():
   return render_template('index.html')
   
@app.route('/signup')
def showSignUp():
   return render_template('signup.html')
   
@app.route('/signin')
def showSignIn():
   return render_template('signin.html')

@app.route('/signout')
def showSignOut():
   return render_template('signout.html')

@app.route('/validatelogin',methods=['POST'])
def validateLogin():
    try:
        _user_email = request.form['inputUserEmail']
        _user_password 	= request.form['inputUserPassword']
        
    except Exception as e:
   	    return render_template('error.html',error = str(e))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
