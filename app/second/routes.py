from . import second
from flask import render_template

@second.route('/')
def index():
    return render_template('second/index.html')
