from alchemyClasses.reservacion import Reservacion


def obtener_reservaciones(email):
    ans = Reservacion.query.filter(Reservacion.idusuario == email).first()
    return ans