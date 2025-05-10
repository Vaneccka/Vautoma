# app/__init__.py
from flask import Flask
from flask import session
from flask import redirect, url_for
def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # если есть конфиг: app.config.from_pyfile('../config.py', silent=True)

    app.secret_key = "auehwfbiasueghfuiashiouefhuiosahedfuihwui2u41278963y87r2t873hf872h"

    # импортируем и регистрируем Blueprint без префикса
    from app.main import main as main_bp
    app.register_blueprint(main_bp)


    # --- auto-register blueprint for 'about' ---
    from app.about import about as about_bp
    app.register_blueprint(about_bp, url_prefix='/about')


    # --- auto-register blueprint for 'contact' ---
    from app.contact import contact as contact_bp
    app.register_blueprint(contact_bp, url_prefix='/contact')


    # --- auto-register blueprint for 'privacy' ---
    from app.privacy import privacy as privacy_bp
    app.register_blueprint(privacy_bp, url_prefix='/privacy')


    # --- auto-register blueprint for 'ai' ---
    from app.ai import ai as ai_bp
    app.register_blueprint(ai_bp, url_prefix="/ai")

    return app