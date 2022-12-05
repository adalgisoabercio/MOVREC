The Python Back End Configuration
- Flask
- Pandas
- Scikit Learn
- etc

Dataset Sources
- https://datasets.imdbws.com/, https://www.imdb.com/interfaces/
- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
- https://www.lafabbricadellarealta.com/open-data-entertainment/

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