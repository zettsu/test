from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/dash')
def main():
   return render_template('index.html')
   
@app.route('/signUp')
def showSignUp():
   return render_template('signup.html')
   
@app.route('/signIn')
def showSignIn():
   return render_template('signin.html')

@app.route('/signOut')
def showSignOut():
   return render_template('signout.html')

if __name__ == "__main__":
   app.run()
