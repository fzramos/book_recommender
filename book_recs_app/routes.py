from book_recs_app import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from book_recs_app.forms import UserForm, LoginForm
from book_recs_app.models import User, FavBook, check_password_hash

@app.route('/', methods = ['GET', 'POST'])
def home():
    # TODO username or email login in 1 line
    login_form = LoginForm()
    print(10)
    if request.method == 'POST':
        print('method worked')
    if login_form.validate():
        print('validated')
    if request.method == 'POST' and login_form.validate():
        print(1)
        username = login_form.username.data
        password = login_form.password.data
        logged_user = User.query.filter(User.username == username).first()
        print(0)
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # todo remove modal or make modal say 'Logged In'
            return redirect(url_for('home'))
        else:
            # todo modal saying log in failed, try again
            pass
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
