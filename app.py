from flask import Flask, redirect, url_for
from alchemyClasses.usuario import db
from controllers.auth import bp
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.reservations import view_reservations


#Configuraciones
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/prueba"
db = SQLAlchemy(app)

#Mapeo al ORM
class Usuario(db.Model):

    email = db.Column('correo', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(200))
    passwd = db.Column('contrasena', db.String(40))

    def __init__(self, email, nombre, passwd):
        self.email = email
        self.nombre = nombre
        self.passwd = passwd


#Consulta
def obtenUsuario(email_arg):
    ans = Usuario.query.filter(Usuario.email==email_arg).first()
    return ans

#Controller
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        email = request.form['email']
        usuario = Usuario(email, passwd, username)
        if obtenUsuario(email) != None:
            return render_template('success.html')
        else:
            return render_template('fail.html')
        """
        Como ya se hizo el request.form, ya se consumio el valor esperado de la vista, entonces esto causa error.
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:"""
        return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/", methods=['GET'])
def home():
    return "<p>Hello world!</p>"



