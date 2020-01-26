from api import db

class Upvote(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,nullable=False)
    upvoted_blog_id=db.Column(db.Integer,nullable=False)

