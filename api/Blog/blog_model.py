from api import db
from datetime import datetime
from api.Tags_Blog.tags_table import tags_blog

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    authorname=db.Column(db.String(128),nullable=False)
    title=db.Column(db.String(128),nullable=False)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    tags= db.relationship('Tag',secondary=tags_blog,backref=db.backref('blogs_associated',lazy="dynamic"))
    featured_image= db.Column(db.String,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'authorname': self.authorname,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'featured_image': self.featured_image,
            'updated_at': self.updated_at,
        }
    