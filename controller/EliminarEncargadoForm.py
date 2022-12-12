from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, EmailField, PasswordField
from wtforms.validators import InputRequired, EqualTo


class EliminarEncargadoForm(FlaskForm):

    idUsuario = IntegerField("id Usuario", validators=[InputRequired()])
    submit = SubmitField("Aceptar")





