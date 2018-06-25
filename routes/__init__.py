from type_route import *
from view_route import *
from auth_route import *

def init_routes(app):
    app.register_blueprint(type_url, url_prefix = '/type')
    app.register_blueprint(view)
    app.register_blueprint(auth_url, url_prefix = '/auth')
