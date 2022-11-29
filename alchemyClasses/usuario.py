from alchemyClasses.__init__ import db

class Usuario(db.Model):

    email = db.Column('correo', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(200))
    passwd = db.Column('contrasena', db.String(40))

    def __init__(self, email, nombre, passwd):
        self.email = email
        self.nombre = nombre
        self.passwd = passwd