#models
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Paste(db.Model):
    id      = db.Column(db.String(36), unique = True, primary_key = True)
    poster  = db.Column(db.String(51))
    paste   = db.Column(db.Text())

    def __init__(self, text, poster = "Anonimo"):
        self.paste  = text
        self.poster = poster
        self.id     = str(uuid.uuid4())

    @property
    def serialize(self):
       return {
           'id'       : self.id,
           'poster'		: self.poster,
           'paste'		: self.paste
       }

    @property
    def serialize_many2many(self):
       """
       Return object's relations in easily serializeable format.
       NB! Calls many2many's serialize property.
       """
       return [ item.serialize for item in self.many2many]