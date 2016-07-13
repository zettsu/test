from flask import Blueprint
from flask import Flask, request, flash, redirect, render_template, session, json
from flask.helpers import url_for

admin = Blueprint('admin', __name__)

@admin.route('/')
def main():
   return render_template('index.html')
   
@admin.route('/signup')
def showSignUp():
   return render_template('signup.html')
   
@admin.route('/signin')
def showSignIn():
   return render_template('signin.html')

@admin.route('/signout')
def showSignOut():
   return render_template('signout.html')

@admin.route('/validatelogin',methods=['POST'])
def validateLogin():
    try:
        _user_email     = request.form['inputUserEmail']
        _user_password  = request.form['inputUserPassword']
        
    except Exception as e:
           return render_template('error.html',error = str(e))
    

