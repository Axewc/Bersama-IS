from flask import Blueprint, render_template, request, session
from models.model_reservaciones import obtener_reservaciones

view_reservations = Blueprint('reservs', __name__, url_prefix='/reservs')

#localhost:5000/reservs/
@view_reservations.route("/", methods=['GET', 'POST'])
def handle_reservations():
    #Codigo python.
    if request.method == 'POST':
        mail = request.form['email']
        reservacion = obtener_reservaciones(mail)
        if reservacion != None:
            session['reservation'] = True
        else:
            session['reservation'] = False
        return render_template("show-reservations.html")
    return render_template("reservations.html")