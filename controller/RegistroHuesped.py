from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, EmailField, PasswordField
from wtforms.validators import InputRequired, EqualTo


class RegistroHuesped(FlaskForm):

    nombre = StringField("Nombre", validators=[InputRequired()])
    apellidoPaterno = StringField("Apellido Paterno", validators=[InputRequired()])
    apellidoMaterno = StringField("Apellido Materno", validators=[InputRequired()])
    correo = EmailField("Correo Electronico", validators=[InputRequired()])
    contrasena = PasswordField("Contraseña", validators=[InputRequired()])
    fechaNacimiento = DateField("Fecha de Nacimiento", validators=[InputRequired()])
    submit = SubmitField("Registarse")