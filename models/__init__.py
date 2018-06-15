from create_db import db

def init_models(app):
    db.init_app(app)
