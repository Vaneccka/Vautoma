#!/usr/bin/env python3
import os
import sys

TEMPLATE_INIT = """from flask import Blueprint

{name} = Blueprint('{name}', __name__, template_folder='templates')

from app.{name} import routes
"""

TEMPLATE_ROUTES = """from . import {name}
from flask import render_template

@{name}.route('/')
def index():
    return render_template('{name}/index.html')
"""

TEMPLATE_HTML = """{{% extends 'base.html' %}}

{{% block content %}}
  <div class="container py-5">
    <h1 class="display-4">{Title} Page</h1>
    <p>Здесь будет контент страницы <code>{name}</code>.</p>
  </div>
{{% endblock %}}
"""

REGISTER_SNIPPET = """
    # --- auto-register blueprint for '{name}' ---
    from app.{name} import {name} as {name}_bp
    app.register_blueprint({name}_bp, url_prefix='/{name}')
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate.py <page_name>")
        sys.exit(1)

    name = sys.argv[1].lower()
    Title = name.capitalize()
    base = os.getcwd()
    app_dir = os.path.join(base, 'app')
    page_dir = os.path.join(app_dir, name)

    # 1. Проверки
    if not os.path.isdir(app_dir):
        print("Ошибка: нет каталога 'app/' в текущей папке.")
        sys.exit(1)
    if os.path.exists(page_dir):
        print(f"Ошибка: каталог app/{name}/ уже существует.")
        sys.exit(1)

    # 2. Создаём структуру каталогов
    os.makedirs(os.path.join(page_dir, 'templates', name))
    # (можно также добавить static, если нужно)
    # os.makedirs(os.path.join(page_dir, 'static', name))

    # 3. __init__.py
    with open(os.path.join(page_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(TEMPLATE_INIT.format(name=name))

    # 4. routes.py
    with open(os.path.join(page_dir, 'routes.py'), 'w', encoding='utf-8') as f:
        f.write(TEMPLATE_ROUTES.format(name=name))

    # 5. index.html
    with open(os.path.join(page_dir, 'templates', name, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(TEMPLATE_HTML.format(name=name, Title=Title))

    # 6. Вставляем регистрацию в app/__init__.py
    init_path = os.path.join(app_dir, '__init__.py')
    if os.path.exists(init_path):
        lines = open(init_path, 'r', encoding='utf-8').read().splitlines()
        new_lines = []
        for line in lines:
            if line.strip().startswith("return app"):
                # вставляем перед этой строкой
                new_lines.append(REGISTER_SNIPPET.format(name=name))
            new_lines.append(line)
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(new_lines))
        print(f"Зарегистрировали Blueprint '{name}' в app/__init__.py")
    else:
        print("Предупреждение: не найден app/__init__.py, пропускаю регистрацию.")

    print(f"✅ Страница '{name}' создана в app/{name}/")
    print("Теперь можешь перезапустить сервер и зайти на:")
    print(f"    http://127.0.0.1:5000/{name}/")

if __name__ == "__main__":
    main()
