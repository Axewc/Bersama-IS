import functools

from models.model_usuarios import obten_usuario
from alchemyClasses.usuario import Usuario
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

registrerBlueprint = Blueprint('registro', __name__, url_prefix='/registro')


# Registrar un usuario.
@registrerBlueprint.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('Name')
        apePat = request.form.get('apellidop')
        apeMat = request.form.get('apellidom')
        correo = request.form.get('Correo electronico')
        password = request.form.get('pass')
        numero = request.form.get('num')
        fechaNac = request.form.get('fechaN')

        usuario = Usuario(nombre, apePat, apeMat, correo,
                          generate_password_hash(password), numero, fechaNac)

        user_name = obten_usuario(correo)
        if user_name == None:
            session.add(usuario)
            session.commit()
        else:
            error = f'El usuario {nombre} ya esta registrado.'

        return render_template('registro.html')
