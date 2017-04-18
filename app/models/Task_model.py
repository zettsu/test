#models

from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Task(db.Model):
    id          = db.Column(db.String(50), unique = True, primary_key = True)
    name        = db.Column(db.String(50))
    comment     = db.Column(db.Text())


    def __init__(self, name, comment = '', parent_task = None):
        self.id          = str(uuid.uuid4())
        self.parent_task = parent_task
        self.name        = name
        self.comment     = comment

    @property
    def serialize(self):
       return {
           'id'             : self.id,
           'parent_task'    : self.parent_task,
           'name'		    : self.name,
           'comment'        : self.comment
       }

    @property
    def serialize_many2many(self):
       """
       Return object's relations in easily serializeable format.
       NB! Calls many2many's serialize property.
       """
       return [ item.serialize for item in self.many2many]
