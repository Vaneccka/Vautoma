from . import about
from flask import render_template

@about.route('/')
def index():
    return render_template('about/index.html')
