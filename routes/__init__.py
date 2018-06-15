from type_route import *

def init_routes(app):
    app.register_blueprint(get_type)
