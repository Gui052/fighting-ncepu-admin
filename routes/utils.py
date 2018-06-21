from flask import session, redirect, url_for
from functools import wraps

# check had login
def page_check_login(func):
    @wraps(func)
    def call(*args, **kwargs):
        if 'has_login' not in session:
            return redirect(url_for('view.login'))
        return func(*args, **kwargs)
    return call
