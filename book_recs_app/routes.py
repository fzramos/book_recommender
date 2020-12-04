from book_recs_app import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from book_recs_app.forms import UserForm, LoginForm, PreferenceForm
from book_recs_app.models import User, FavBook, BookDetails, check_password_hash

# Globals
size_dict = {
    'Short': [0, 224],
    'Intermediate': [225, 375],
    'Long': [375, 3342],
    'Any': [0, 3342]
}
pop_dict = {
    'Little Known': [0, 200],
    'Popular': [200, 2000],
    'Very Well-Known': [2000, 2418736],
    'Any': [0, 2418736]
}
year_dict = {
    'Pre-1997': ['1-1-1919', '12-3-1997'],
    '1998-2002': ['12-3-1997', '12-31-2002'],
    '2003-2005': ['12-31-2002', '12-28-2004'],
    'Post-2005': ['12-28-2004', '12-28-2020'],
    'Any': ['1-1-1919', '12-28-2020']
}

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = PreferenceForm()
    if request.method == 'POST' and form.validate():
        min_rating = form.min_rating.data
        # max_rating = form.max_rating.data
        book_length = form.book_length.data 
        popularity = form.popularity.data 
        pub_year = form.pub_year.data 

        if min_rating > 4.50:
            min_rating = 4.50

        page_range = size_dict[book_length]
        pop_range = pop_dict[popularity]
        year_range = year_dict[pub_year]

        matching_books = db.session.query(
            BookDetails.isbn13
            ).filter(BookDetails.num_pages > page_range[0]
            ).filter(BookDetails.num_pages < page_range[1]
            ).filter(BookDetails.ratings_count > pop_range[0]
            ).filter(BookDetails.ratings_count < pop_range[1]
            ).filter(BookDetails.average_rating > min_rating
            ).filter(BookDetails.publication_date > year_range[0]
            ).filter(BookDetails.publication_date < year_range[1]
            ).limit(200).all()
        
        # return redirect(url_for('recommend'), matching_books)
        return render_template('results.html', isbns = matching_books)        

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
            login_user(logged_user)
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

# @app.route('/recommendation')
# def recommend(isbns):
#     return render_template('results.html', isbns = isbns)
