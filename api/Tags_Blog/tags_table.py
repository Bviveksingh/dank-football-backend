from api import db

tags_blog = db.Table('tags_blog',
    db.Column('blog_id', db.Integer,db.ForeignKey('blog.id')),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'))
)   