from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/posts')
def post():
    return render_template('posts.html')

@app.route('/movielist')
def movielist():
    return render_template('movielist.html')

@app.route('/cleofrom5to7')
def cleofrom5to7():
    return render_template('cleofrom5to7.html')

@app.route('/cigarettesandcoffee')
def cigarettesandcoffee():
    return render_template('cigsandcoffee.html')