# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # если есть конфиг: app.config.from_pyfile('../config.py', silent=True)

    # импортируем и регистрируем Blueprint без префикса
    from app.main import main as main_bp
    app.register_blueprint(main_bp)


    # --- auto-register blueprint for 'second' ---
    from app.second import second as second_bp
    app.register_blueprint(second_bp, url_prefix='/second')

    return app