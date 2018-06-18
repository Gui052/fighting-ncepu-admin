from flask import Blueprint, request, session, jsonify, url_for, redirect

auth_url = Blueprint('auth_url', __name__)
@auth_url.route('/login', methods=['POST'])
def login():
    username = request.values.get('username', 0)
    password = request.values.get('password', 0)
    session['username'] = username
    return jsonify({ 'code': 200 })

@auth_url.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login_view.login'))
