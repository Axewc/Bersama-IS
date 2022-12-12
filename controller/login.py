import functools
import hashlib

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash #This is only if security is enabled.
from ..alchemyClasses.usuario import Usuario
from ..models.UsuarioModel import obten_usuario

loginBlueprint = Blueprint('login', __name__)

# Iniciar Sesión

@loginBlueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        mail = request.form['email']
        passwrd = request.form['password']

        error = None

        usuario = obten_usuario(mail)

        passwrd = hashlib.sha256(passwrd.encode('utf-8')).hexdigest()
             
        if usuario == None:
            error = 'No existe el usuario'
        elif not passwrd == usuario.passHash:
        #elif not check_password_hash(usuario.passHash, passwrd):
            error = 'Contraseña incorrecta'

        if error is None:
            session.clear()
            session['email'] = usuario.correo
            if usuario.tipo == "huesped":
                return redirect(url_for('home.showHuesped'))
            elif usuario.tipo == "administrador":
                return redirect(url_for('home.showAdmin'))
            return redirect(url_for('home.show'))

        flash(error)

    return render_template('login.html')




''''
@loginBlueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        passwd = request.form['password']
        mail = request.form['email']
        if obten_usuario(mail) != None: #El usuario existe.
            #return render_template("success.html")
            #session.clear()
            #session['user_id'] = usuario.mail
            #g.user = usuario.mail
            return redirect(url_for("login.success"))
        else:
            return redirect(url_for("login.failure"))
    else: #Estamos haciendo un wget localhost:5000/login/
        return render_template('login.html')
'''

@loginBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('user_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('login.login'))

@loginBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")