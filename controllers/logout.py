from flask import Blueprint, session, redirect, url_for

logoutBlueprint =  Blueprint('logout', __name__, url_prefix='/logout')

@logoutBlueprint.route('/', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login.login'))