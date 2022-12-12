import hashlib

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm


from .ActualizarEncargadoForm import ActualizarEncargadoForm
from ..models.UsuarioModel import select_first_usuario
from ..models.UsuarioModel import delete_usuario


eliminar_encargado = Blueprint('eliminar_encargado', __name__)



@eliminar_encargado.route('/encargado/eliminar/<int:idUsuario>', methods= ['GET','POST'])
def show(idUsuario):
    usuario = select_first_usuario(idUsuario)
         
    if delete_usuario(usuario):
        flash("Encargado eliminado satisfactoriamente")
        return redirect(url_for("consultar_encargado.show"))
    else:
        flash("No se pudo eliminar al Encargado, intente mas tarde")

