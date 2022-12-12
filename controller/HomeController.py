from flask import Blueprint, render_template
  

home = Blueprint('home', __name__)



@home.route("/", methods=['GET', 'POST'])
def show():
    return render_template('index.html')



@home.route("/index.html", methods=['GET', 'POST'])
def showd():
    return render_template('index.html')
