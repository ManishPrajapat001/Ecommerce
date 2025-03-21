import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# PostgreSQL Connection URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/ecommerce_db'# in local db for linux no password is needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
