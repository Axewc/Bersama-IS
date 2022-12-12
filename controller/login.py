import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash #This is only if security is enabled.
from alchemyClasses.usuario import Usuario
from models.UsuarioModel import obten_usuario

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['username']
        passwd = request.form['password']
        mail = request.form['email']
        usuario = Usuario(mail, nombre, passwd)
        if obten_usuario(mail) != None: #El usuario existe.
            #return render_template("success.html")
            session.clear()
            session['user_id'] = usuario.nombre
            g.user = usuario.nombre
            return redirect(url_for("login.success"))
        else:
            return redirect(url_for("login.failure"))
    else: #Estamos haciendo un wget localhost:5000/login/
        return render_template('login.html')

@loginBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('user_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('login.login'))

@loginBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")