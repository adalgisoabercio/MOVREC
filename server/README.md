# MOVREC Back End Developement Environment

## Web Application Server
The Projects itself are develop by using Flask as main library for Back End Processing. There are several libriaries,
- Flask 
- Flask SQLAlchemy
- Flask JWT Extended
- Flask Restx
- Python Decouple
- etc

Also the all packages and versions can be check [HERE](Pipfile)

The Libraries are downloaded and generated with [python-pipenv](https://pipenv.pypa.io/en/latest/) based, The Python Virtual Package Environment. For installing can check [HERE](https://pipenv.pypa.io/en/latest/#install-pipenv-today). Also the python-pipenv important commands are [Here](https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55)


## Recommendation System
The 


## Deployment

Set Up the Developement
```
set FLASK_APP=setup.py
set FLASK_ENV=developement
flask run
```

Generating SECRET_KEY
- on terminal type step-by-step
```
python 
import secrets
secrets.token_hex(12)
q()

```
- putting the SECRET KEY in .env
- if want to more secure, just update it daily or weekly

API dir Accessing
- There is a instances to declare the API
- The API assets are saved in **/Assets** directory
- After run the flask, just adding **/Assets**. Ex = http://127.0.0.1:5000/Assets
```
API = Api(app, doc = '/Assets')
```

Generating Database
- Type in Terminal to Settings the app instances and for Database Generator Purposes
- It can be update while development, for now main.py
```
export FLASK_APP=main.py
flask shell 
```