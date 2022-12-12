from .database import db


from ..alchemyClasses.usuario import Usuario




def insert_usuario(nombre, apPaterno, apMaterno, correo, passhash, fechaNacimiento, tipo, idHostal):
    encargado = Usuario(nombre, apPaterno, apMaterno, correo, passhash, fechaNacimiento, tipo, idHostal)
    try:
        db.session.add(encargado)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
 
def select_usuario(nombre, apPaterno, apMaterno, correo, fechaNacimiento, tipo, idHostal):
    
    usuarios = []
    if not (nombre is None or nombre == ""):
        usuarios = Usuario.query.filter_by(nombre =nombre)

    elif not (apPaterno is None or apPaterno == ""):
        usuarios = Usuario.query.filter_by(apellidoPaterno= apPaterno)

    elif not (apMaterno is None or apMaterno == ""):
        usuarios = Usuario.query.filter_by(apellidoMaterno= apMaterno)

    elif not (correo is None or correo == ""):
        usuarios = Usuario.query.filter_by(correo= correo)

    elif not (fechaNacimiento is None or fechaNacimiento == ""):
        usuarios = Usuario.query.filter_by(fechaaAcimiento= fechaNacimiento)

    elif not (idHostal is None or idHostal == ""):
        usuarios = Usuario.query.filter_by(idHostal= idHostal)



    if not (nombre is None or nombre == ""):
        usuarios = [x for x in usuarios if x.nombre == nombre]

    if not (apPaterno is None or apPaterno == ""):
        usuarios = [x for x in usuarios if x.apellidoPaterno == apPaterno]

    if not (apMaterno is None or apMaterno == ""):
        usuarios = [x for x in usuarios if x.apellidoMaterno == apMaterno]

    if not (correo is None or correo == ""):
        usuarios = [x for x in usuarios if x.correo == correo]

    if not (fechaNacimiento is None or fechaNacimiento == ""):
        usuarios = [x for x in usuarios if x.fechaNacimiento == fechaNacimiento]

    if not (idHostal is None or idHostal == ""):
        usuarios = [x for x in usuarios if x.idHostal == idHostal]

        usuarios = [x for x in usuarios if x.tipo == tipo]
    
    return usuarios

def select_first_usuario(idUsuario):
    return Usuario.query.filter_by(idUsuario= idUsuario).first_or_404()

def update_usuario(usuario, nombre, apPaterno, apMaterno, correo, fechaNacimiento, idHostal):
    usuario.nombre= nombre
    usuario.apellidoPaterno= apPaterno
    usuario.apellidoMaterno= apMaterno
    usuario.correo= correo
    usuario.fechaNacimiento= fechaNacimiento
    usuario.idHostal= idHostal



    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def delete_usuario(usuario):
    try:
        db.session.delete(usuario)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
