from werkzeug.security import generate_password_hash
from db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    username = db.Column(db.String(30))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    fisrt_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    enabled = db.Column(db.Boolean)
    db.UniqueConstraint('username', name='unique_ix_0001')

    def __init__(self, username, password, email, first_name, last_name, enabled=True):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.fisrt_name = first_name
        self.last_name = last_name
        self.enabled = enabled

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()