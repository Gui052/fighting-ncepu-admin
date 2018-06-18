from flask import Blueprint, jsonify

import sys
import os
sys.path.append(os.getcwd() + '/models')

from type_model import *

get_type = Blueprint('get_type', __name__)
@get_type.route('/index')
def index():
    return jsonify({
        'code': 200,
        'data': get_all_type()
    })
