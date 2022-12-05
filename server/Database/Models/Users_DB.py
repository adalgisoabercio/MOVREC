from flask_sqlalchemy import SQLAlchemy
# from Database.Users import db
from datetime import datetime
# from Database.Users import create_user, delete_user, update_user

# Connecting the Object Relational Mapper to the Flask Applications
db = SQLAlchemy()
now = datetime.now()

# class for represent the tables in database
# Make Database Table for User
class User(db.Model):
    __tablename__ = "user" # table name
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False) # The Column Name, datatype, maximum length
    email = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(200), nullable = False)
    phone = db.Column(db.String(50), nullable = False)
    # cascade = "all, delete", the all relationship between User and Blog_Spot that have same id, can be deleted
    # movie_types = db.relationship("Movie_List", cascade = "all, delete", nullable = False) # This have relationship to Blog_Spot Class
    
    # User Class Informations
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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        db.session.add(self)
        db.session.commit()


'''
#Inherit to db.Model
# Make Database Table for Blog Post
class Movie_List(db.Model):
    __tablename__ = "blog_post" # table name
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    region = db.Column(db.String(200), nullable = False)
    language = db.Column(db.String(50), nullable = False)
    movie_types = db.Column(db.String(16), nullable = False)
    movie_genres = db.Column(db.String(100), nullable = False)
    movie_avg_rating = db.Column(db.Integer, nullable = False)
    movie_vote = db.CLoumn(db.Integer, nullable = False)
    movie_popular_title = db.Column(db.String(500), nullable = False)

    #More Updated since Updating the Feature, like Recommendations

    

    # The foreign key of user_id must not null
    #so, _set_sqlite_pragma function will check the meet constraint
    #from the class Blog Post that contain the user_id as foreign to class User that contain id as Primary Key
    # so the id just contain the user_id
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False) # The relation between User and Blog_Spot
'''