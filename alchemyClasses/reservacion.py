from alchemyClasses.__init__ import db

class Reservacion(db.Model):

    idreservacion = db.Column("idreservacion", db.Integer, primary_key=True)
    inicio = db.Column("inicio", db.Date)
    final = db.Column("final", db.Date)
    idusuario = db.Column("idusuario", db.String(200))

    def __init__(self, idreservacion, inicio, final, idusuario):
        self.idreservacion = idreservacion
        self.inicio = inicio
        self.final = final
        self.idusuario = idusuario

