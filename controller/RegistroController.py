import functools
from models.model_usuarios import obten_usuario
from alchemyClasses.usuario import Usuario
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from models.UsuarioModel import crear_usuario

registrerBlueprint = Blueprint('registro', __name__, url_prefix='/registro')

# Registrar un usuario.
@registrerBlueprint.route('/registro', methods=['GET', 'POST'])
def registro():
    tipo = "huesped"
    print(tipo)
    if request.method == 'POST':
        nombre = request.form['name']
        apePat = request.form['apellidoPaterno']
        apeMat = request.form['apellidoMaterno']
        correo = request.form['correo']
        password = request.form['hash']
        fechaNac = request.form['fechaNacimiento']

        print(nombre)
        usuario = Usuario(nombre=nombre, apellidoPaterno=apePat, apellidoMaterno=apeMat, correo=correo, passHash=password, fechaNacimiento=fechaNac, tipo=tipo, idHostal=None)
        error = None
        user_name = obten_usuario(correo)

        if user_name == None:
            crear_usuario(usuario)
            return redirect(url_for('huespedView.html'))
        else:
            error = f'El usuario {nombre} ya esta registrado.'

        return render_template('registro.html')
