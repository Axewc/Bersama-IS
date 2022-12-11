import hashlib

from flask import Blueprint, render_template
from flask_wtf import FlaskForm


from .AgregarEncargadoForm import AgregarEncargadoForm
from ..models.UsuarioModel import insert_encargado


agregar_encargado = Blueprint('agregar_encargado', __name__)



@agregar_encargado.route('/encargado/agregar', methods= ['GET','POST'])
def show():
    nombre = None
    apellidoPaterno = None
    apellidoMaterno = None
    correo = None
    contrasena = None
    fechaNacimiento = None
    idHostal = None 
    tipo = "encargado"
         
    form = AgregarEncargadoForm()
    if form.validate_on_submit():
        nombre= form.nombre.data
        form.nombre.data = ""
        apellidoPaterno= form.apellidoPaterno.data
        form.apellidoPaterno.data = ""
        apellidoMaterno= form.apellidoMaterno.data
        form.apellidoMaterno.data = ""
        correo= form.correo.data
        form.correo.data = ""
        contrasena= form.contrasena.data
        form.contrasena.data = ""
        confirmarContrasena= form.confirmarContrasena.data
        form.confirmarContrasena.data = ""
        fechaNacimiento= form.fechaNacimiento.data
        idHostal= form.idHostal.data
        
        passhash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()


        insert_encargado(nombre, apellidoPaterno, apellidoMaterno, correo, passhash, fechaNacimiento, idHostal)
 
    return render_template("agregar_encargado.html",
                            nombre= nombre,
                            apellidoPaterno= apellidoPaterno,
                            apellidoMaterno= apellidoMaterno,
                            correo= correo,
                            contrasena= contrasena,
                            fechaNacimiento= fechaNacimiento,
                            idHostal= idHostal,
                            form= form)
 
