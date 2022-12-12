from flask import Flask, render_template

from .controller.HomeController import home
from .controller.AgregarEncargadoController import agregar_encargado
from .controller.ConsultarEncargadoController import consultar_encargado
from .controller.ActualizarEncargadoController import actualizar_encargado
from .controller.EliminarEncargadoController import eliminar_encargado


from .models.database import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Fer110675#01@localhost:3306/Hoteland"
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(home)
    app.register_blueprint(agregar_encargado)
    app.register_blueprint(consultar_encargado)
    app.register_blueprint(actualizar_encargado)
    app.register_blueprint(eliminar_encargado)


    return app
