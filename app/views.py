from flask import render_template
from app import app, collect
import json

@app.route('/')
@app.route('/index')
def index():
    articles = json.loads(collect.retrieve())
    print articles["source"]
    return render_template('index.html',
                           title='Home',
                           articles=articles)
