from flask import Flask, redirect, url_for
from alchemyClasses.usuario import db
from controllers.auth import bp
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.reservations import view_reservations

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(bp)
app.register_blueprint(loginBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(view_reservations)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Fer110675#01@localhost:3306/prueba"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    db.create_all()
    app.run()


