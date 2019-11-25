import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///berlin.db'
db = SQLAlchemy(app)

#from project import models
from project import controller