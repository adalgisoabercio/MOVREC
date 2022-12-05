from decouple import config
import os

SQL_dir = os.path.dirname(os.path.realpath(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast = bool) # either 0 to be false or 1 to be true
    SECRET_KEY = config('SECRET_KEY')
    # FRONTED_URL = ""

class DevCONFIG(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQL_dir, 'sqlitedb.sql') # database placement
    DEBUG = True # needed to checking front end connections
    SQLALCHEMY_ECHO = True # provided the developement to running the sql commands realtime

class ProdCONFIG(Config):
    pass

class TestCONFIG(Config):
    pass
