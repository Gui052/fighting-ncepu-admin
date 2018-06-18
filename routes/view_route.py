from flask import Blueprint, render_template, session, redirect, url_for

login_view = Blueprint('login_view', __name__)
@login_view.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('get_type.index'))
    return render_template('login.html')
