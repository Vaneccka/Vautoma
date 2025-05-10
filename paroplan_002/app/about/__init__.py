from flask import Blueprint

about = Blueprint('about', __name__, template_folder='templates')

from app.about import routes
