from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lsgogroup'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lsgozp1996@localhost:3306/admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(weeks=2)

from routes import init_routes
init_routes(app)

from models import init_models
init_models(app)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)
