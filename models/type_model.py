from create_db import db

class Type(db.Model):
    __tablename__ = 'question_sort'
    id = db.Column(
        db.Integer,
        nullable = False,
        primary_key = True,
        autoincrement = True
    )
    sort = db.Column(db.String(16))
    status = db.Column(
        db.Integer,
        default = 1
    )

def get_all_type():
    types = Type.query.filter_by(status = 1).with_entities(Type.id, Type.sort).all()
    data = list()
    for t in types:
        data.append({
            'id': t[0],
            'name': t[1]
        })
    return data

def get_type(id):
    type = Type.query.filter_by(id = id).first()
    return type

def del_type(id):
    type = get_type(id)
    type.status = 0
    db.session.commit()

def update_type(id, name):
    type = get_type(id)
    type.sort = name
    db.session.commit()

def add_type(name):
    old = Type.query.filter_by(sort = name).first()

    if old != None:
        if old.status == 0:
            old.status = 1
        else:
            return None
    else:
        type = Type(sort = name)
        db.session.add(type)

    db.session.commit()
    return db.session.query(Type).filter_by(sort = name).first()
