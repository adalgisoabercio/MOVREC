

# from flask import Flask
from __base import db, time
from __base import generate_password_hash, check_password_hash
import json

"""CLASS FOR USER DATABASE REPRESENTATIONS"""

class User(db.Model):
    
    __tablename__ = "user_db"
    
    """The Column Name, datatype, maximum length"""
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(200), nullable = False)
    phone_number = db.Column(db.String(50), nullable = False)
    jwt_auth_active = db.Column(db.Boolean())
    data_created = db.Column(db.DateTime(), default = time)

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

    # Saving the Profile Edit
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Update Username Data from Profile Edit
    def username_update(self, new_username: str) -> str:
        self.username = new_username

    # Update Email Data from Profile Edit
    def email_update(self, new_email: str) -> str:
        self.email = new_email

    # Update Address Data from Profile Edit
    def address_update(self, new_address: str) -> str:
        self.address = new_address

    # Update Phone Number Data from Profile Edit
    def phone_update(self, new_phone_number: str) -> str:
        self.phone_number = new_phone_number

    # return the JWT are activated or not
    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    # Set the JWT Authentications
    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    def delete(self, id):
        pass

    # Internal class methods for searching a specific users by id
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    # Internal class methods for searching a specific users by email
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


    # For data exporting purposes -> JSON file
    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['username'] = self.username
        cls_dict['email'] = self.email

        return cls_dict

    # returning the JSON view of Users Data
    def toJSON(self):

        return self.toDICT()


"""CLASS JWT TOKEN REPRESENTATIONS"""

class JWTTokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jwt_token = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"

    def save(self):
        db.session.add(self)
        db.session.commit()



"""CLASS FOR MOVIE DATABASE REPRESENTATIONS"""

class Movie_List(db.Model):
    __tablename__ = "movie_db" # table name

    """The Column Name, datatype, maximum length"""
    id = db.Column(db.Integer, primary_key = True)
    movie_title = db.Column(db.String(50), nullable = False)
    region = db.Column(db.String(200), nullable = False)
    language = db.Column(db.String(50), nullable = False)
    # movie_type = db.Column(db.String(16), nullable = False)
    movie_genre = db.Column(db.String(100), nullable = False)
    movie_rating = db.Column(db.Integer, nullable = False)
    movie_vote = db.CLoumn(db.Integer, nullable = False)
    # movie_popular_title = db.Column(db.String(500), nullable = False)
    movie_link = db.Column(db.String(500), nullable = False)
    data_created_at = db.Column(db.DateTime(), default = time)

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

    # Saving the Profile Edit
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Update genre Data from Profile Edit
    def movie_genre_update(self, new_movie_genre: str) -> str:
        self.movie_genre = new_movie_genre

    # Update language Data from Profile Edit
    def language_update(self, new_language: str) -> str:
        self.language = new_language

    # Update movie_rating Data from Profile Edit
    def movie_rating_update(self, new_movie_rating: str) -> str:
        self.movie_rating = new_movie_rating

    # Update movie_link Data from Profile Edit
    def movie_link_update(self, new_movie_link_number: str) -> str:
        self.movie_link_number = new_movie_link_number

    # # return the JWT are activated or not
    # def check_jwt_auth_active(self):
    #     return self.jwt_auth_active

    # # Set the JWT Authentications
    # def set_jwt_auth_active(self, set_status):
    #     self.jwt_auth_active = set_status

    def delete(self, id):
        pass

    # Internal class methods for searching a specific users by id
    @classmethod
    def get_by_title(cls, title):
        return cls.query.get_or_404(title)

    # Internal class methods for searching a specific users by email
    @classmethod
    def get_by_movie_genre(cls, movie_genre):
        return cls.query.filter_by(movie_genre=movie_genre).first()


    # For data exporting purposes -> JSON file
    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['movie_title'] = self.movie_title
        cls_dict['movie_rating'] = self.movie_rating

        return cls_dict

    # returning the JSON view of Users Data
    def toJSON(self):

        return self.toDICT()