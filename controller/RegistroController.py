import hashlib

from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from flask_wtf import FlaskForm
from .RegistroHuesped import RegistroHuesped
from ..models.UsuarioModel import insert_usuario, obten_usuario


registro_bp = Blueprint('registro', __name__)

# Registrar un usuario.


@registro_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    nombre = None
    apellidoPaterno = None
    apellidoMaterno = None
    correo = None
    contrasena = None
    fechaNacimiento = None
    idHostal = None
    tipo = "huesped"

    form = RegistroHuesped()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellidoPaterno = form.apellidoPaterno.data
        apellidoMaterno = form.apellidoMaterno.data
        correo = form.correo.data
        contrasena = form.contrasena.data
        fechaNacimiento = form.fechaNacimiento.data

        passhash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

        # if obten_usuario(correo) != None:
        if insert_usuario(nombre, apellidoPaterno, apellidoMaterno, correo, passhash, fechaNacimiento, tipo, idHostal):
            flash("Usuario registrado con exito")
            return redirect(url_for('home.show'))
        else:
            flash("No se pudo actualizar la base de datos, intente mas tarde")
        # else:
           #flash('Datos erroneos, intente con otros')

    return render_template("registro.html", form=form)
    
    
