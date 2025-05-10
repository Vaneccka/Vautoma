# 🧠 GitGuide: Подробный гайд по Git для разработчиков

Git — это распределённая система контроля версий. Ниже приведены основные команды и приёмы, которые нужны для повседневной работы с Git.

---

## 📦 1. Начальная настройка Git

```bash
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"
```

Проверка текущих настроек:

```bash
git config --list
```

---

## 🏁 2. Инициализация нового репозитория

```bash
git init
```

Создаёт новый локальный репозиторий в текущей директории.

---

## 🌐 3. Подключение к удалённому репозиторию

```bash
git remote add origin https://github.com/username/project.git
```

Проверка:

```bash
git remote -v
```

---

## 📝 4. Добавление и коммиты

Проверить изменения:

```bash
git status
```

Добавить файл:

```bash
git add filename.ext
```

Добавить все изменения:

```bash
git add .
```

Создание коммита:

```bash
git commit -m "Комментарий к изменению"
```

---

## 🚀 5. Отправка изменений на сервер

Первый пуш:

```bash
git push -u origin main
```

Обычный пуш после:

```bash
git push
```

---

## 🔄 6. Получение обновлений

```bash
git pull
```

---

## 🌿 7. Работа с ветками

Создание новой ветки и переход в неё:

```bash
git checkout -b new-feature
```

Переключение на другую ветку:

```bash
git checkout main
```

Слияние ветки:

```bash
git merge new-feature
```

Удаление ветки:

```bash
git branch -d new-feature
```

---

## 📜 8. История и различия

Показать историю коммитов:

```bash
git log
```

Показать изменения в файлах:

```bash
git diff
```

---

## 🗑️ 9. Удаление файлов из индекса (без удаления на диске)

```bash
git rm --cached path/to/file
```

---

## 📁 10. .gitignore

Файл `.gitignore` указывает Git, какие файлы и папки **не нужно отслеживать**. Примеры:

```
__pycache__/
*.pyc
.venv/
.env
*.log
node_modules/
```

---

## 🧠 11. Рекомендации

- Делай `git pull` перед началом работы
- Используй осмысленные коммиты
- Работай в отдельных ветках для новых фич
- Используй `.gitignore` для исключения временных файлов

---

## ✅ 12. Быстрые команды (шпаргалка)

```bash
git init
git add .
git commit -m "init"
git remote add origin <URL>
git push -u origin main
```