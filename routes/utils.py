from flask import session, redirect, jsonify, url_for, request
from functools import wraps

# check had login
def page_check_login(func):
    @wraps(func)
    def call(*args, **kwargs):
        print 'zp'
        if 'has_login' not in session:
            return redirect(
                url_for('view.login', prev_url = request.path)
            )
        return func(*args, **kwargs)
    return call

def success(key, value):
    response = { 'code': 200 }
    response[key] = value
    return jsonify(response)

def param_error(msg):
    return jsonify({ 'code': 400, 'msg': msg })
