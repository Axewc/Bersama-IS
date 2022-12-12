from ..models.database import db

class Usuario(db.Model):
    
    __tablename__ = 'Usuario'
    idUsuario = db.Column('idUsuario', db.Integer, primary_key= True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    apellidoPaterno = db.Column('apellidoPaterno', db.String(45))
    apellidoMaterno = db.Column('apellidoMaterno', db.String(45))
    correo = db.Column('correo', db.String(200))
    passHash = db.Column('hash', db.String(64))
    fechaNacimiento = db.Column('fechaNacimiento', db.Date)
    tipo = db.Column('tipo', db.String(45))
    idHostal = db.Column('idHostal', db.Integer)


    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, correo, passHash, fechaNacimiento, tipo, idHostal= None):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.correo = correo
        self.passHash = passHash
        self.fechaNacimiento = fechaNacimiento
        self.tipo = tipo
        self.idHostal = idHostal
