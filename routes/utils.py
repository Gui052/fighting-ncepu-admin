from flask import session, redirect, url_for, request
from functools import wraps

# check had login
def page_check_login(func):
    @wraps(func)
    def call(*args, **kwargs):
        if 'has_login' not in session:
            return redirect(
                url_for('view.login', prev_url = request.path)
            )
        return func(*args, **kwargs)
    return call
