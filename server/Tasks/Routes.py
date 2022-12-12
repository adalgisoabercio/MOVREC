"""Python 3.10.6 Supported Libraries"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager, jwt_required, jwt_manager
from decouple import config
from datetime import datetime
import json

"""Development Packages"""
from Auth import Register, Login, Logout
from Methods import User_Action_Create, User_Action_Delete, User_Action_Read, User_Action_Update
from Database import Users
from Recommendation import Adjective, Trending, History

from Config import DevCONFIG, ProdCONFIG

app = Flask(__name__)
app.config.from_object()

@app.route()
def user_welsoming():
    return jsonify({'Message':'Succesfully Log In. Enter Mode.....'}), 200

def app_run():
    return "GOOD"

if __name__ == '__main__':
    app.run()