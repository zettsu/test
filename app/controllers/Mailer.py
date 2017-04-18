#Mailer.py

# import Mail #
from flask_mail import Mail, Message

from flask import Blueprint
from flask import request, url_for, redirect

# basics templates and views and principal app

from flask import render_template, Flask, current_app

# extensions and tools

from flask import json, jsonify
from flask.ext.responses import json_response, xml_response, auto_response

mailerBlueprint = Blueprint("mail",__name__)

@mailerBlueprint.route("/send")
def send():

	current_app.config["MAIL_SERVER"] = "smtp.gmail.com"
	current_app.config["MAIL_PORT"] = 465
	current_app.config["MAIL_USE_TLS"] = False
	current_app.config["MAIL_USE_SSL"] = True
	current_app.config["MAIL_DEBUG"] = current_app.debug
	current_app.config["MAIL_USERNAME"] = ""
	current_app.config["MAIL_PASSWORD"] = ""
	current_app.config["DEFAULT_MAIL_SENDER"] = None
	mail = Mail()
	mail.init_app(current_app)
	msg = Message("Prueba de Mailer Class",sender="",recipients=[""])
	mail.send(msg)

	return redirect(url_for('Paste.show_submit_page'))