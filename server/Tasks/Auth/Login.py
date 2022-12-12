from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, jwt_manager
from flask_restx import Api
import json
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__== '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")