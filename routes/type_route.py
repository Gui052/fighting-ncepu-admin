# -*- coding: UTF-8 -*-

from flask import Blueprint, request

import sys
import os
from utils import *
sys.path.append(os.getcwd() + '/models')

from type_model import *

type_url = Blueprint('type_url', __name__)
@type_url.route('/get')
def index():
    return success('data', get_all_type())

@type_url.route('/delete')
@page_check_login
def delete():
    id = request.values.get('id')
    del_type(id)
    return success('msg', '删除成功')

@type_url.route('/update', methods=['POST'])
@page_check_login
def update():
    id = request.values.get('id')
    name = request.values.get('name')
    if name == '':
        return param_error('类型名称不能为空')
    update_type(id, name)
    return success('msg', '更新成功')

@type_url.route('/add', methods=['POST'])
@page_check_login
def add():
    name = request.values.get('name')
    if name == '':
        return param_error('类型名称不能为空')
    res = add_type(name)
    if res == None:
        return param_error('该类型已存在')
    return success('data', {
        'id': res.id,
        'msg': '新增成功'
    })
