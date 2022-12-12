import hashlib

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm


from .ActualizarEncargadoForm import ActualizarEncargadoForm
from ..models.UsuarioModel import select_first_usuario
from ..models.UsuarioModel import update_usuario


actualizar_encargado = Blueprint('actualizar_encargado', __name__)



@actualizar_encargado.route('/encargado/actualizar/<int:idUsuario>', methods= ['GET','POST'])
def show(idUsuario):
    usuario = select_first_usuario(idUsuario)
         
    form = ActualizarEncargadoForm()

    if form.validate_on_submit():
        nombre= form.nombre.data
        apellidoPaterno= form.apellidoPaterno.data
        apellidoMaterno= form.apellidoMaterno.data
        correo= form.correo.data
        fechaNacimiento= form.fechaNacimiento.data
        idHostal= form.idHostal.data

            
        if update_usuario(usuario, nombre, apellidoPaterno, apellidoMaterno, correo, fechaNacimiento, idHostal):
            flash("Encargado actualizada satisfactoriamente")
            return redirect(url_for("actualizar_encargado.show", idUsuario= idUsuario))
        else:
            flash("No se pudo actualizar la base de datos, intente mas tarde")


 
    return render_template("actualizar_encargado.html",
                            usuario= usuario,
                            form= form)
 
