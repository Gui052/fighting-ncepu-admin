import datetime
from create_db import db

active_status = 1

class User(db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(
        db.Integer,
        nullable = False,
        primary_key = True,
        autoincrement = True
    )
    username = db.Column(db.String(16))
    passwd = db.Column(db.String(100))
    status = db.Column(
        db.Integer,
        default = active_status
    )
    ctime = db.Column(db.TIMESTAMP, default = datetime.datetime.now())
    utime = db.Column(db.TIMESTAMP, default = datetime.datetime.now())

def select_by_username(username):
    return User.query.filter_by(
        username = username,
        status = active_status
    ).first()
