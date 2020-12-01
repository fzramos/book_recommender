from book_recs_app import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, login_user
from book_recs_app.forms import UserForm, LoginForm
from book_recs_app.models import User, FavBook, check_password_hash

@app.route('/', methods = ['GET', 'POST'])
def home():
    # TODO username or email login in 1 line
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate():
        username = login_form.email.data
        password = login_form.password.data
        logged_user = User.query.filter(User.username == username).first()
        if logged_user and checked_passsword_hash(logged_user.password, password):
            login_user(logged_user)
            # todo remove modal or make modal say 'Logged In'
            return redirect(url_for('home'))
        else:
            # todo modal saying log in failed, try again
            pass
    return render_template('home.html', login_form = login_form)

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

    return render_template('register.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
