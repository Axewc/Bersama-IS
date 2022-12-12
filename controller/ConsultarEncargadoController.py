from flask import Blueprint, render_template, redirect, url_for, session
from flask_wtf import FlaskForm


from .ConsultarEncargadoForm import ConsultarEncargadoForm
from ..models.UsuarioModel import select_usuario


consultar_encargado = Blueprint('consultar_encargado', __name__)



@consultar_encargado.route('/encargado/consultar', methods= ['GET','POST'])
def show():
    nombre = None
    apellidoPaterno = None
    apellidoMaterno = None
    correo = None
    fechaNacimiento = None
    idHostal = None 
    tipo = "encargado"
         
    form = ConsultarEncargadoForm()
    if form.validate_on_submit():
        nombre= form.nombre.data
        apellidoPaterno= form.apellidoPaterno.data
        apellidoMaterno= form.apellidoMaterno.data
        correo= form.correo.data
        fechaNacimiento= form.fechaNacimiento.data
        idHostal= form.idHostal.data
        

        
        usuarios = select_usuario(nombre, apellidoPaterno, apellidoMaterno, correo, fechaNacimiento, tipo, idHostal)

        return render_template("resultado_encargado.html",
                                usuarios= usuarios)

 
    return render_template("consultar_encargado.html",
                            nombre= nombre,
                            apellidoPaterno= apellidoPaterno,
                            apellidoMaterno= apellidoMaterno,
                            correo= correo,
                            fechaNacimiento= fechaNacimiento,
                            idHostal= idHostal,
                            form= form)
