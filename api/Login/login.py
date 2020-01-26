from flask import Blueprint,request,jsonify
from api.User.user_model import User
from flask_jwt_extended import (jwt_required, create_access_token,
    get_jwt_identity)
from werkzeug.security import check_password_hash


user_login= Blueprint('login',__name__)

@user_login.route("/login", methods=["POST"])
def login():
    user_info=request.get_json()

    user=User.query.filter_by(email=user_info["email"]).first()
    if user:
        if check_password_hash(user.password,user_info["password"]):
            jwt_token= create_access_token(identity=user.id)
            return jsonify({"token":jwt_token})
        else:
            return "Invalid email or password",400
    else:
        return "Invalid email or password",400    
    