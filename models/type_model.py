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

def get_all_type():
    types = Type.query.with_entities(Type.id, Type.sort).all()
    data = list()
    for t in types:
        data.append({
            'id': t[0],
            'name': t[1]
        })
    return data
