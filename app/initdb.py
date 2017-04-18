# initdb.py

import os, sys

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://usuario:clave@localhost/app"


db = SQLAlchemy(app)


class Paste(db.Model):
    id = db.Column(db.String(36), unique=True, primary_key=True)
    poster = db.Column(db.String(51))
    paste = db.Column(db.Text())

db.create_all()