from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 

app = Flask(__name__)
app.config["SECRET_KEY"] = 'asdasdsjhfusdhfuhdsf89hew7f8h347fg'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
