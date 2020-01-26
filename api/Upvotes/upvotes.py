from flask import Flask,Blueprint,request,jsonify
from api import db
from api.Upvotes.upvotes_model import Upvote
from api.User.user_model import User


upvotes = Blueprint("upvotes",__name__)

@upvotes.route('/add_upvote', methods=["POST"])
def add_upvote():
    data = request.get_json()

    user = User.query.filter_by(id=data["user_id"]).first()


    upvoted_data=Upvote(user_id=user.id,upvoted_blog_id=data["blog_id"])

    db.session.add(upvoted_data)
    db.session.commit()

    return jsonify("Upvoted!!")

@upvotes.route('/downvote/<int:user_id>/<int:blog_id>', methods=["DELETE"])
def downvote(user_id,blog_id):
    upvote = Upvote.query.filter_by(user_id=user_id,upvoted_blog_id=blog_id).first()
    print(upvote)
    db.session.delete(upvote)
    db.session.commit()
    return jsonify("Downvoted");

@upvotes.route('/upvotes_blog/<int:id>', methods=["GET"])
def get_blog_upvotes(id):
    upvotes = Upvote.query.filter_by(upvoted_blog_id=id).all()

    upvotes_array = []
    for upvote in upvotes:
        upvotes_array.append(upvote)
    return jsonify({"count": len(upvotes_array)})

@upvotes.route('/check_upvote/<int:user_id>/<int:blog_id>', methods=["GET"])
def check_user_upvote(user_id,blog_id):
    upvote = Upvote.query.filter_by(user_id=user_id,upvoted_blog_id=blog_id).first()
    count = 0;
    if(upvote):
        count+=1
    
    return jsonify({"count": count}) 

    

    
