from alchemyClasses.__init__ import db

class Usuario(db.Model):

    idUsuario = db.Column('idUsuario', db.Integer, primary_key=True)
    nombre = db.Column('nombre', db.String(100))
    apPaterno = db.Column('apPaterno', db.String(100))
    apMaterno = db.Column('apMaterno', db.String(100))
    email = db.Column('correo', db.String(200))
    contrasena = db.Column('hash_contrasena', db.String(40))
    telefono = db.Column('telefono', db.String(10))
    fechaNacimiento = db.Column('fechaNacimiento', db.String(40))
    nacionalidad = db.Column('nacionalidad', db.String(200))
    idHostal = db.Column('idHostal', db.Integer)
    esAdministrador = db.Column('esAdministrador', db.Integer)
    esEncargado = db.Column('esEncargado', db.Integer)
    esHuesped = db.Column('esHuesped', db.Integer)

    def __init__(self, nombre, apPaterno, apMaterno, email, contrasena, telefono, fechaNacimiento, nacionalidad, esAdministrador, esEncargado, esHuesped):
        self.idPersona = None
        self.nombre = nombre
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.email = email
        self.contrasena = contrasena
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.nacionalidad = nacionalidad
        self.idHostal = None
        self.esAdministrador = esAdministrador
        self.esEncargado = esEncargado
        self.esHuesped = esHuesped