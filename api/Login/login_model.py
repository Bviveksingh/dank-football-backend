from api import db


class Login(db.Model):
    username=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)

