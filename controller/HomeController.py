from flask import Blueprint, render_template
  

home = Blueprint('home', __name__)



@home.route("/", methods=['GET'])
def show():
    return render_template('base.html')


