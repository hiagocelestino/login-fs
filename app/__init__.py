import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
host = os.environ.get("HOST")
db = os.environ.get("DATABASE")
user_db = os.environ.get("USER_DB")
pass_db = os.environ.get("PASSWORD_DB")
port = os.environ.get("PORT")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user_db}:{pass_db}@{host}:{port}/{db}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
CORS(app)
db = SQLAlchemy(app)


from .models import usuarios, enderecos
from .routes import routes
