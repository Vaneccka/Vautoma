from . import privacy
from flask import render_template

@privacy.route('/')
def index():
    return render_template('privacy/index.html')
