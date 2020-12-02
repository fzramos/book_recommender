from book_recs_app import app, db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    book = db.relationship('FavBook', backref = 'owner', lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.encrypt_password(password)

    def encrypt_password(self, password):
        return generate_password_hash(password)

    def _repr__(self):
        return f'User {self.username} has be created with the'\
            f'email {self.email}.'

class FavBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    author =  db.Column(db.String(100))
    cover = db.Column(db.String(100))
    description = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, author, cover, description, user_id):
        self.title = title
        self.author = author
        self.cover = cover
        self.description = description
        self.user_id = user_id
    
    def __repr__(self):
        return 'New book added to favorites list: {self.title} by {self.author}.'
