from flask import Blueprint
from flask import Flask 
app = Flask(__name__)
app.secret_key = "auehwfbiasueghfuiashiouefhuiosahedfuihwui2u41278963y87r2t873hf872h"  # 🔐 сюда свой секретный ключ



ai = Blueprint("ai", __name__, template_folder="templates")

from app.ai import routes  # подключаем маршруты
