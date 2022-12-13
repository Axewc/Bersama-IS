from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, EmailField, PasswordField
from wtforms.validators import Optional


class ConsultarEncargadoForm(FlaskForm):

    nombre = StringField("Nombre", validators=[Optional()])
    apellidoPaterno = StringField("Apellido Paterno", validators=[Optional()])
    apellidoMaterno = StringField("Apellido Materno", validators=[Optional()])
    correo = EmailField("Correo Electronico", validators=[Optional()])
    fechaNacimiento = DateField("Fecha de Nacimiento", validators=[Optional()])
    idHostal = IntegerField("Hostal", validators=[Optional()])
    submit = SubmitField("Buscar")





