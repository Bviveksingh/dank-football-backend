from api import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(100), nullable=False)
    lastname=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(120), nullable=False)
    email=db.Column(db.String(120),nullable=False)
    blogs=db.relationship('Blog',backref='user')
    followers=db.Column(db.Integer,default=0)
    following=db.Column(db.Integer,default=0)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'followers': self.followers,
            'following': self.following
        }
