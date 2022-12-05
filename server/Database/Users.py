# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, jsonify, request
# from Database.Models.Users_DB import User
# from datetime import datetime
# from Database.DSA.Linked_List import LinkedList


# # Connecting the Object Relational Mapper to the Flask Applications
# db = SQLAlchemy()
# now = datetime.now()

# # @app.route("/user", methods = ["POST"]) # -> use post request method to user route
# def create_user():
#     data = request.get_json() # -> parse the json file to the data variable for db consumptions
#     new_user = User( # create new object to passing the data 'dictionary' to class parameter
#         name = data["name"],
#         email = data["email"],
#         address = data["address"],
#         phone = data["phone"],
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User Created"}), 200 # 200 -> status are responsed

# # @app.route("/user/<user_id>", methods = ["DELETE"])
# def delete_user(user_id):
#     user = User.query.filter_by(id = user_id).first() # filter_by user_id and take it first 
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify ({}), 200 # 200 -> status are responsed

# # @app.route("/user/<user_id>", methods = ["UPDATE"])
# def update_user(user_id, cur_name, cur_email):
#     name = cur_name
#     email = cur_email


# # @app.route("/user/descending_id", methods = ["GET"])
# def get_all_user_descending(): # descending by ID
#     users = User.query.all() 
#     all_user_sorted = LinkedList()
    
#     for user in users:
#         all_user_sorted.insert_beginning(
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email,
#                 "address": user.address,
#                 "phone": user.phone
#             }
#         )

#     # return the sorted linked list to a array
#     return jsonify(all_user_sorted.to_list()), 200

# # @app.route("/user/ascending_id", methods = ["GET"])
# def get_all_user_ascending():
#     # ascending by ID
#     users = User.query.all() 
#     all_user_sorted = LinkedList()
    
#     for user in users:
#         all_user_sorted.insert_at_end(
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email,
#                 "address": user.address,
#                 "phone": user.phone
#             }
#         )

#     # return the sorted linked list to a array
#     return jsonify(all_user_sorted.to_list()), 200 # 200 -> status are responsed

# # @app.route("/user/<user_id>", methods = ["GET"])
# def get_one_user(user_id):
#     users = User.query.all()
#     all_users_sorted = LinkedList()

#     for user in users:
#         all_users_sorted.insert_beginning(
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email,
#                 "address": user.address,
#                 "phone": user.phone
#             }
#         )

#     user = all_users_sorted.get_user_by_id(user_id)
#     return jsonify(user), 200


# # @app.route("/blog_post/<user_id>", methods = ["POST"])
# def create_blog_post(user_id):
#     pass

# # @app.route("/user/<user_id>", methods = ["GET"])
# def get_all_blog_post(user_id):
#     pass

# # @app.route("/blog_post/<blog_post_id>", methods = ["GET"])
# def get_one_blog_post(blog_post_id):
#     pass

# # @app.route("/blog_post/<blog_post_id>", methods = ["DELETE"])
# def delete_blog_post(blog_post_id):
#     pass