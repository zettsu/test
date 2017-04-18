# basics http and routes

from flask import Blueprint
from flask import request, url_for, redirect

# basics templates and views

from flask import render_template

# extensions and tools

from flask import json, jsonify
from flask.ext.responses import json_response, xml_response, auto_response

# models

from models.Paste_model import Paste, db

# Blueprints 

pasteBlueprint = Blueprint("Paste", __name__)

# Methods for Paste

@pasteBlueprint.route("/")
def show_submit_page():
    pastes = Paste.query.all()
    return render_template("/paste/submit.html", pastes = pastes)

@pasteBlueprint.route("/submit", methods = ["POST"])
def submit():
    
    paste_text = request.form["paste"]
    paste_text = paste_text.encode("ascii", errors = "ignore")

    paste_user = request.form["poster"]

    if paste_user == None:
        paste_user = "Anonimous"

    paste = Paste(paste_text, paste_user)

    db.session.add(paste)
    db.session.commit()
    
    return render_template("/paste/success.html", id=paste.id)

@pasteBlueprint.route("/paste/<id>")
def show(id):

    pastes = Paste.query.filter_by(id = id)
    paste = pastes.first()

    if paste == None:
        raise Exception("No such paste by id %s" % id)

    return render_template("/paste/paste.html", paste = paste)

@pasteBlueprint.route("/json")
def get_last_pastes():
    pastes = Paste.query.all()
    
    all_pastes_json = []

    for paste in pastes:
        all_pastes_json.append(paste.serialize)

    return jsonify(data = all_pastes_json)