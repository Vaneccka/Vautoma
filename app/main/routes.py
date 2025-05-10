# app/main/routes.py
from . import main
from flask import render_template

@main.route('/')
def index():
    items = ["Первый", "Второй", "Третий"]
    return render_template(
        'main.html',
        title="Главная",
        header="Добро пожаловать!",
        message="Шаблон из main Blueprint",
        items=items
    )

