from flask import render_template
from app import app, collect
import json

@app.route('/')
@app.route('/index')
def index():
    sourceList = json.loads(collect.call_API())
    print sourceList["status"]
    return render_template('index.html',
                           title='Home',
                           sourceList=sourceList)
