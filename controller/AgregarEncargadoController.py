import hashlib

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm


from .AgregarEncargadoForm import AgregarEncargadoForm
from ..models.UsuarioModel import insert_usuario


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
        apellidoPaterno= form.apellidoPaterno.data
        apellidoMaterno= form.apellidoMaterno.data
        correo= form.correo.data
        contrasena= form.contrasena.data
        confirmarContrasena= form.confirmarContrasena.data
        fechaNacimiento= form.fechaNacimiento.data
        idHostal= form.idHostal.data
        
        passhash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()


        if insert_usuario(nombre, apellidoPaterno, apellidoMaterno, correo, passhash, fechaNacimiento, tipo, idHostal):
            flash("Encargado agregado a la base de datos satisfactoriamente")
            return redirect(url_for('agregar_encargado.show'))
        else:
            flash("No se pudo actualizar la base de datos, intente mas tarde")


 
    return render_template("agregar_encargado.html",
                            nombre= nombre,
                            apellidoPaterno= apellidoPaterno,
                            apellidoMaterno= apellidoMaterno,
                            correo= correo,
                            contrasena= contrasena,
                            fechaNacimiento= fechaNacimiento,
                            idHostal= idHostal,
                            form= form)
 
