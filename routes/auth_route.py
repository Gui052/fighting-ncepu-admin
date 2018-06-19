# coding=utf-8

from flask import Blueprint, request, session, jsonify, url_for, redirect
from werkzeug.security import check_password_hash

import sys
import os
sys.path.append(os.getcwd() + '/models')

from user_model import *

msgs = {
    'username': '请输入用户名',
    'password': '请输入密码'
}

def param_error(msg):
    return jsonify({ 'code': 400, 'msg': msg })

auth_url = Blueprint('auth_url', __name__)
@auth_url.route('/login', methods=['POST'])
def login():
    data = {}
    for k, v in msgs.items():
        val = request.values.get(k)
        if val == '':
            return param_error(v)
        data[k] = val
    row = select_by_username(data['username'])
    if row == None:
        return param_error('该用户未注册,请联系管理员')
    if not(check_password_hash(row.passwd, data['password'])):
        return param_error('密码错误')
    session['has_login'] = True
    return jsonify({ 'code': 200 })

@auth_url.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login_view.login'))
