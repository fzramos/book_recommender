from book_recs_app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    name = ['._.']
    return render_template('test.html', list_names = name)