from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dankdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='secretKey'
    jwt=JWTManager(app)
    
    db.init_app(app)

    from api.User.user import user
    app.register_blueprint(user)

    from api.Blog.blogs import blogs
    app.register_blueprint(blogs)

    from api.Tags.tags import tags
    app.register_blueprint(tags)

    from api.Login.login import user_login
    app.register_blueprint(user_login)

    from api.Upvotes.upvotes import upvotes
    app.register_blueprint(upvotes)

    return app