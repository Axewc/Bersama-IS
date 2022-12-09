from alchemyClasses.__init__ import db

class Usuario(db.Model):

    idUsuario = db.Column('idUsuario', db.int, primary_key= True)
    nombre = db.Column('nombre', db.String(45))
    apPat = db.Column('apellidoPaterno', db.String(45))
    apMat = db.Column('apellidoMaterno', db.String(45))
    email = db.Column('correo', db.String(200))
    passwd = db.Column('hash', db.String(200))
    fechaNa = db.Column('fechaNacimiento', db.String(40))



    def __init__(self, idUsuario, nombre, apPat, apMat, email, passwd, fechaNa):
        self.idUsuario = idUsuario 
        self.nombre = nombre 
        self.apPat  = apPat
        self.apMat = apMat 
        self.email = email 
        self.passwd = passwd
        self.fechaNa = fechaNa