from flask import Blueprint

# Создаём Blueprint
main = Blueprint('main', __name__, template_folder='templates')

# Импортируем маршруты, в которых используется этот Blueprint
from app.main import routes