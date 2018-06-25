from flask import Blueprint, jsonify

import sys
import os
sys.path.append(os.getcwd() + '/models')

from type_model import *

type_url = Blueprint('type_url', __name__)
@type_url.route('/get')
def index():
    return jsonify({
        'code': 200,
        'data': get_all_type()
    })
