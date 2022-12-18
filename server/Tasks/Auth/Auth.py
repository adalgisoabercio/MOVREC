

# Importing Flask API and built-in Dependencies
from flask_restx import Api, Namespacee, Resource
from datetime import datetime, timezone, timedelta
from functools import wraps
from flask import request
import jwt

# Database Model and App Configurations



rest_api = Api(version="1.0", title="Users API")