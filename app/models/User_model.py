#models

from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class User(db.Model):
    id      = db.Column(db.String(50), unique = True, primary_key = True)
    name    = db.Column(db.String(50))
    email   = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, name, email, password):
        self.id         = str(uuid.uuid4())
        self.name       = name
        self.email      = email
        self.password   = password

    @property
    def serialize(self):
        return {
            'id':self.id,
            'name': self.name,
            'email':self.email
        }

    @property
    def serialize_many2many(self):
        """
        Return object's relations in easily serializeable format.
        NB! Calls many2many's serialize property.
        """
        return [ item.serialize for item in self.many2many]