from api import db
from flask import Blueprint,request,jsonify
from api.Tags.tags_model import Tag

tags = Blueprint('tags',__name__)


@tags.route('/tags',methods=["GET"])
def get_tags():
    return jsonify("All tags returned")


# @tags.route('/add_tag', methods=["POST"])
# def add_tag():
#     tag_data = request.get_json()
    
#     new_tag = Tag(name=tag_data["name"])

