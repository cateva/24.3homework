"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):

    ___tablename___ = "cupcakes"

    id = db.Column(db.Integer,
    primary_key=True,
    autoincrement=True)
    falvor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False,defalut=DEFAULT_IMAGE)

    def to_dict(self):

        return {
            "id" : self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.image,
            "image": self.image,
        }

def connect_db(app):

    ad.app = app
    db.init_app(app)