from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import asyncio
import os

from app.ai import ai
from app.ai.ai_models import send_deepseek_request, send_openai_request

API_KEY = os.getenv("PROXYAPI_KEY") or "sk-Zc2RfcGl9PzffUlnfnRzDf4CDOZN5D4U"

@ai.route("/chat", methods=["GET", "POST"])
def ai_chat():
    if request.is_json:
        # Обработка AJAX запроса
        data = request.get_json()
        prompt = data.get("user_input", "")
        model = data.get("model", "deepseek")  # по умолчанию DeepSeek

        if not prompt:
            return jsonify({"response": "⛔ Пустой запрос"})

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        if model == "openai":
            ai_response = loop.run_until_complete(send_openai_request(prompt, API_KEY))
        else:
            ai_response = loop.run_until_complete(send_deepseek_request(prompt, API_KEY))

        return jsonify({"response": ai_response})

    # Обычная отправка формы
    if request.method == "POST":
        prompt = request.form.get("user_input")
        model = request.form.get("model", "deepseek")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        if model == "openai":
            ai_response = loop.run_until_complete(send_openai_request(prompt, API_KEY))
        else:
            ai_response = loop.run_until_complete(send_deepseek_request(prompt, API_KEY))

        session["last_input"] = prompt
        session["last_response"] = ai_response
        session["last_model"] = model

        return redirect(url_for("ai.ai_chat"))

    # На GET
    user_input = session.pop("last_input", None)
    ai_response = session.pop("last_response", None)
    model = session.pop("last_model", "deepseek")

    return render_template("ai/index.html", user_input=user_input, ai_response=ai_response, model=model)