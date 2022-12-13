from flask import Blueprint, render_template, flash, redirect, url_for
  

home = Blueprint('home', __name__)



@home.route("/", methods=['GET', 'POST'])
def show():
    return render_template('index.html')



@home.route("/index.html", methods=['GET', 'POST'])
def showd():
    return render_template('index.html')

@home.route("/huesped", methods=['GET', 'POST'])
def showHuesped():
    return render_template('huespedView.html')


@home.route("/encargado", methods=['GET', 'POST'])
def showAdmin():
    return render_template('adminView.html')
