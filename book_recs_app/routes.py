from book_recs_app import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from book_recs_app.forms import UserForm, LoginForm, PreferenceForm
from book_recs_app.models import User, FavBook, check_password_hash

@app.route('/', methods = ['GET', 'POST'])
def home():

    form = PreferenceForm()
    if request.method == 'POST' and form.validate():
        min_rating = form.min_rating.data
        # max_rating = form.max_rating.data
        book_length = form.book_length.data 
        popularity = form.popularity.data 
        pub_year = form.pub_year.data 
        

    return render_template('home.html', form = form)

# @app.route('/register')
# def testRoute():
#     name = ['._.']
#     return render_template('test.html', list_names = name)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.username.data
        password = form.password.data
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()

        # if user registers they are logged in
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # TODO username or email login in 1 line
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        logged_user = User.query.filter(User.username == username).first()
        if logged_user and check_password_hash(logged_user.password, password):
            user(logged_user)
            # todo remove modal or make modal say 'Logged In'
            return redirect(url_for('home'))
        else:
            # todo modal saying log in failed, try again
            pass
    return render_template('login.html', form = form)

@app.route('/search')
def search():
    
    return render_template('search.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/list')
def user_list():
    return render_template('user_list.html')
