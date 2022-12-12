import hashlib

from models.database import db
from flask import Blueprint, flash, render_template, request
from flask_wtf import FlaskForm

from alchemyClasses.usuario import Usuario


from .AgregarEncargadoForm import AgregarEncargadoForm
from ..models.UsuarioModel import insert_encargado


eliminar_encargado = Blueprint('eliminar_encargado', __name__)

@eliminar_encargado.route('/encargado/eliminar/<idUsuario>', methods= ['GET'])
def delete(idUsuario):
    usuario = Usuario.get_by_id(idUsuario)
    db.session.delete(usuario)
    db.session.commit()
    
    flash('Usuario eliminado correctamente')
    
    return render_template('encargado/eliminar.html')