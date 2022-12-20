

"""Python 3.10.6 Supported Libraries"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, Namespace
from flask_jwt_extended import JWTManager, jwt_required, jwt_manager
from decouple import config
from datetime import datetime, timezone, timedelta
from functools import wraps
import os
import jwt
import json

"""Development Packages"""
from auth import Register, Login, Logout
from Constant.http_code import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from Database import Users
from Recommendation import Adjective, Trending, History

from Constant.config import DevCONFIG, ProdCONFIG

app = Flask(__name__) # Flask Instances
app.config.from_object(DevCONFIG) # importing the developement configurations class
API = Api(app, doc = '/Assets') # the dir for data, etc API consumptions\
rest_api = Api(app, version="1.0", title="Users API") # doc = Auth


# API Endpoint
@API.route('/hello')
class HelloResource(Resource):
    def get(self): # GET -> HTTP METHODS
        return {"message":"Hello World !!"}

@API.route('/movie-delete')
class Movie_Deletion(Resource):
    def delete(self):
        return {"message":"Movie deleted succesfully !!"}




@app.route()
def user_welcoming():
    return jsonify({'Message':'Succesfully Log In. Enter Mode.....'}), 200

def app_run():
    return "GOOD"

if __name__ == '__main__':
    app.run()