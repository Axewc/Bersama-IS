from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from controller.HomeController import home


#Configuraciones
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Fer110675#01@localhost:3306/prueba"
SQLAlchemy(app)

app.register_blueprint(home)


