import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'JKHGIUGYUF(*&^&*^*YTTDYFJHGH*T^&T*T&GHKJHJGH'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 4

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(
    cloud_name='wrmjpntv',
    api_key='635691296158495',
    api_secret='5J9hXF9hkDtwQtIsHZQklBCBpHM'
)


