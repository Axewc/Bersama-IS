from flask import Blueprint, session, redirect, url_for

logoutBlueprint =  Blueprint('logout', __name__)

@logoutBlueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('home.show'))