from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy() # SQLAlchemy Istances
time = datetime.now() # Current Date and Time Instances