from flask import Blueprint

privacy = Blueprint('privacy', __name__, template_folder='templates')

from app.privacy import routes
