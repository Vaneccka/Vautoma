# app/main/routes.py
from . import main
from flask import render_template

@main.route("/")
def home():
    return render_template("main.html",
                           header="Добро пожаловать!",
                           message="Здесь вы можете протестировать общение с ИИ.")