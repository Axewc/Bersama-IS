from .database import db


from ..alchemyClasses.usuario import Usuario




def insert_encargado(nombre, apPaterno, apMaterno, correo, passhash, fechaNacimiento, idHostal):
     encargado = Usuario(nombre, apPaterno, apMaterno, correo, passhash, fechaNacimiento, "encargado", idHostal)
     db.session.add(encargado)
     db.session.commit()
 

