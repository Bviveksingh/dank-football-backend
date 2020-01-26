from flask import Blueprint,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from api.User.user_model import User
from api import db



user = Blueprint('user', __name__)

@user.route('/add_user', methods=['POST'])
def add_user():

    user_data = request.get_json()

    new_user = User(firstname=user_data["firstname"],lastname=user_data["lastname"],password=user_data["password"],email=user_data["email"])

    new_user.password = generate_password_hash(new_user.password, "sha256",salt_length=12)

    db.session.add(new_user)
    db.session.commit()
    my_response = make_response(jsonify("Success"),201)
    return my_response


@user.route('/users',methods=["GET"])
@jwt_required
def users():
    return jsonify("All users returned"),201

@user.route('/user/<int:id>',methods=["GET"])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    serialized_data = user.serialize

    serialized_data["blogs"] = []

    for blog in user.blogs:
        serialized_data["blogs"].append(blog.serialize)

    return jsonify({"user": serialized_data})



