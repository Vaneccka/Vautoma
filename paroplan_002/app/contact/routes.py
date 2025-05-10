from . import contact
from flask import render_template

@contact.route('/')
def index():
    return render_template('contact/index.html')
