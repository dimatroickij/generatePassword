from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    middlename = db.Column(db.String(64), index=True)
    birthday = db.Column(db.String(10))
    placeBirth = db.Column(db.String(64), index=True)
    tel = db.Column(db.String(10))

    def __repr__(self):
        return '<{} {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)