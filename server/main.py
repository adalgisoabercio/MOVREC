from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource
from config import DevCONFIG
from Database.Models import Users_DB
# from Database.Models.Users_DB import db
# from Database.Users import db


app = Flask(__name__) # Flask App instances
app.config.from_object(DevCONFIG) # importing the developement configurations class
API = Api(app, doc = '/Assets') # the dir for data, etc API consumptions

db = SQLAlchemy()

# API Endpoint
@API.route('/hello')
class HelloResource(Resource):
    def get(self): # GET -> HTTP METHODS
        return {"message":"Hello World !!"}

@API.route('/movie-delete')
class Movie_Deletion(Resource):
    def delete(self):
        return {"message":"Movie deleted succesfully !!"}

# @app.shell_context_processors
# def shell_dev_context():
#     return {
#         "db" : db,
#         "Users" : Users_DB.User
#     }

# @API.route('/movie-read')
# class Movie_Read(Resource):
#     def read(self):
#         return {"message":"Johansen Thomas: The Part of World"}

# @API.route('/movie-update')
# class Movie_Update(Resource):
#     def update(self):
#         return {"message":"Movie updated succesfully !!"}

if __name__ == '__main__':
    # app.run(debug =  True, host = '0.0.0.0')
    app.run()
