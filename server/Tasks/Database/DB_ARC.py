from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
time = datetime.now()

"""CLASS FOR DATABASE REPRESENTATIONS"""

# User Database Table
class User(db.Model):
    
    __tablename__ = "user_db" # table name
    
    """The Column Name, datatype, maximum length"""
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(200), nullable = False)
    phone = db.Column(db.String(50), nullable = False)

    # cascade = "all, delete", the all relationship between User and Blog_Spot that have same id, can be CRUD
    # This have relationship to Movie_List Database Table
    movie_rl = db.relationship("Movie_List", cascade = "all, delete", nullable = False)
    
    # User Database Table Informations
    def __repr__(self) -> str:
        """Retrieve the all information based on Category"""
        # Choosed Category info
        id_users_info = f"MOVREC - {id}".center(30, "*") + '\n'
        
        # Amount and Description of Choosed Category
        full_info = ""
        users_name = "{:<25}".format(self.name)
        users_email = "{:>7.2f}".format(self.email)
        # Retrieve all the formatted info
        full_info += f'{users_name[:23]}{users_email[:7]}' + '\n'

        # return the all information
        # return {"message":"{}".format(id_users_info + full_info)}
        return id_users_info + full_info

# User Database Table
class Movie_List(db.Model):
    __tablename__ = "movie_db" # table name

    """The Column Name, datatype, maximum length"""
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    region = db.Column(db.String(200), nullable = False)
    language = db.Column(db.String(50), nullable = False)
    movie_types = db.Column(db.String(16), nullable = False)
    movie_genres = db.Column(db.String(100), nullable = False)
    movie_avg_rating = db.Column(db.Integer, nullable = False)
    movie_vote = db.CLoumn(db.Integer, nullable = False)
    movie_popular_title = db.Column(db.String(500), nullable = False)
    movie_link = db.Column(db.String(500), nullable = False)

    #More Updated since Updating the Feature, like Recommendations

    

    # The foreign key of user_id must not null
    #so, _set_sqlite_pragma function will check the meet constraint
    #from the class Movie List that contain the user_id as foreign to class User that contain id as Primary Key
    # so the id just contain the user_id
    user_id = db.Column(db.Integer, db.ForeignKey("user_db.id"), nullable = False) # The relation between User and Blog_Spot

    # Movie Database Table Informations
    def __repr__(self) -> str:
        """Retrieve the all information based on Category"""
        # Choosed Category info
        movie_users_info = f"MOVREC - {id}".center(30, "*") + '\n'
        
        # Amount and Description of Choosed Category
        full_info = ""
        users_name = "{:<25}".format(self.name)
        users_email = "{:>7.2f}".format(self.email)
        # Retrieve all the formatted info
        full_info += f'{users_name[:23]}{users_email[:7]}' + '\n'

        # return the all information
        # return {"message":"{}".format(id_users_info + full_info)}
        return movie_users_info + full_info
