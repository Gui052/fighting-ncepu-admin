from flask import Blueprint, render_template, session, \
    redirect, url_for, request
from utils import page_check_login

import sys
import os
sys.path.append(os.getcwd() + '/models')
from type_model import get_all_type

view = Blueprint('view', __name__)

@view.route('/login')
def login():
    if 'has_login' in session:
        return redirect(url_for('view.index'))
    return render_template('login.html')

@view.route('/index')
@page_check_login
def index():
    return render_template('index.html', types = get_all_type())
