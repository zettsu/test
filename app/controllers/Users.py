# basics http and routes

from flask import Blueprint
from flask import request, url_for, redirect

# basics templates and views

from flask import render_template

# extensions and tools

from flask import json, jsonify
from flask.ext.responses import json_response, xml_response, auto_response

# models

from models.User_model import User, db

# Blueprints

userBlueprint = Blueprint("Users", __name__)