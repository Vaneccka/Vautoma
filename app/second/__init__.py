from flask import Blueprint

second = Blueprint('second', __name__, template_folder='templates')

from app.second import routes
