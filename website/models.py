from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    token = db.Column(db.String(150))
    confirmed_email = db.Column(db.Boolean, default=False)

    def __init__(self, email, password, first_name, token, confirmed_email):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.token = token
        self.confirmed_email = confirmed_email
