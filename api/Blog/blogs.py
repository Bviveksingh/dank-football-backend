from flask import Blueprint,request,jsonify,make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from api import db
from api.Blog.blog_model import Blog
from api.Tags.tags_model import Tag
from api.User.user_model import User


blogs = Blueprint('blogs',__name__)

@blogs.route('/blogs',methods=["GET"])
def get_all_blogs():
    blogs = Blog.query.limit(5).all()
    serialized_data = [];

    for blog in blogs:
        serialized_data.append(blog.serialize)
    return jsonify({"blogs":serialized_data})


@blogs.route('/add_blog',methods=['POST'])
@jwt_required
def add_blog():
    current_user = get_jwt_identity()
    blog_data = request.get_json()

    user = User.query.filter_by(id=current_user).first()

    name = user.firstname + " " + user.lastname
    new_blog = Blog(authorname=name,title=blog_data["title"],content=blog_data["content"],featured_image=blog_data['featured_image'])
    new_blog.user = user


    for x in blog_data["tags"]:
        present_tag=Tag.query.filter_by(name=x).first()
        if(present_tag):
            present_tag.blogs_associated.append(new_blog)
        else:
            new_tag = Tag(name=x)
            db.session.add(new_tag)
            new_tag.blogs_associated.append(new_blog)

    db.session.add(new_blog)
    db.session.commit()

    blog_id = getattr(new_blog,"id")
   
    return jsonify({"id":blog_id}),201

@blogs.route('/blog/<int:id>', methods=["GET"])
def show_blog(id):
    blog_by_id= Blog.query.filter_by(id=id).first_or_404()
    serialized_data = blog_by_id.serialize
    serialized_data["tags"]=[]

    for tag in blog_by_id.tags:
        serialized_data["tags"].append(tag.serialize)

    

    return jsonify({"blog": serialized_data})
    
@blogs.route('/user_blogs/<int:user_id>', methods=["GET"])
def get_blogs_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user.blogs




