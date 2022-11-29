import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash #Security matters.

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/another-index', methods=['GET'])
def another_index():
    return render_template("another-index.html")

@bp.route('/', methods=['GET'])
def reroute_home():
    return redirect(url_for('auth.another_index'))