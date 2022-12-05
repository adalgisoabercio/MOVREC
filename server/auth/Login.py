from flask import Flask, request, jsonify
import flask_sqlalchemy
import flask_jwt_extended
import flask_restx
import json
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__== '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")