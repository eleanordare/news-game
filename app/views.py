from flask import render_template
from app import app, collect

@app.route('/')
@app.route('/index')
def index():
    article = collect.retrieve()
    print article["title"]
    return render_template('index.html',
                           title='Home',
                           article=article)
