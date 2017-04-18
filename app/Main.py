# Pastes.py

# basic io and system #
#import os, sys

# utils #
from flask import Flask, Blueprint

#from flask import json, jsonify
from flask import redirect, url_for
#from flask.ext.responses import json_response, xml_response, auto_response

# models #
from models.Paste_model import db

# controllers #
from controllers.Pastes import pasteBlueprint
from controllers.Mailer import mailerBlueprint
from controllers.Users import userBlueprint


from api.auth import apiBlueprint


app = Flask(__name__)
app = Flask(__name__, template_folder = 'views/templates')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Sakura23!@localhost/app"

app.debug = True

db.init_app(app)

@app.route("/")
def home():
	return redirect(url_for("Paste.show_submit_page"))

app.register_blueprint(mailerBlueprint  , url_prefix 	= "/mail")
app.register_blueprint(pasteBlueprint   , url_prefix 	= "/paste")
app.register_blueprint(userBlueprint    , url_prefix    = "/user")
app.register_blueprint(apiBlueprint     , url_prefix 	= "/api")

if __name__ == "__main__":
    app.run()