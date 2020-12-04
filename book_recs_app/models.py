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
            + f'email {self.email}.'

class BookDetails(db.Model):
    __tablename__ = 'book_details'
    id = db.Column('id', db.INTEGER(), autoincrement=False, nullable=False, primary_key = True)
    title = db.Column('title', db.VARCHAR(length=254), autoincrement=False, nullable=False)
    authors = db.Column('authors', db.VARCHAR(length=750), autoincrement=False, nullable=False)
    average_rating = db.Column('average_rating', db.NUMERIC(precision=4, scale=2), autoincrement=False, nullable=False)
    isbn = db.Column('isbn', db.VARCHAR(length=10), autoincrement=False, nullable=False)
    isbn13 = db.Column('isbn13', db.VARCHAR(length=13), autoincrement=False, nullable=False)
    language_code = db.Column('language_code', db.VARCHAR(length=5), autoincrement=False, nullable=False)
    num_pages = db.Column('num_pages', db.INTEGER(), autoincrement=False, nullable=False)
    ratings_count = db.Column('ratings_count', db.INTEGER(), autoincrement=False, nullable=False)
    text_reviews_count = db.Column('text_reviews_count', db.INTEGER(), autoincrement=False, nullable=False)
    publication_date = db.Column('publication_date', db.DATE(), autoincrement=False, nullable=False)
    publisher = db.Column('publisher', db.VARCHAR(length=67), autoincrement=False, nullable=False)
    # db.PrimaryKeyConstraint('id', name='book_details_pkey')

    # TODO
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    # no init, repr because this should be a read only table

class FavBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    isbn13 = db.Column(db.String(13))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, isbn13, user_id):
        self.isbn13 = isbn13
        self.user_id = user_id
    
    def __repr__(self):
        return f'New book added to User {self.user_id} favorites list with isbn13: {self.isbn13}.'



# Obsolete FavBook, choosing to only dbve book_detail table id to favbook
# class FavBook(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100))
#     author =  db.Column(db.String(100))
#     cover = db.Column(db.String(100))
#     description = db.Column(db.String(300))
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

#     def __init__(self, title, author, cover, description, user_id):
#         self.title = title
#         self.author = author
#         self.cover = cover
#         self.description = description
#         self.user_id = user_id
    
#     def __repr__(self):
#         return 'New book added to favorites list with isbn13: {self.isbn} by {self.author}.'


