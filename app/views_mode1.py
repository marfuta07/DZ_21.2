from flask import render_template, request, jsonify
from app import app


# ============================================================
# РЕЖИМ 1: Полноценный сайт (Задание 1)
# ============================================================

@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/category')
def category():
    return render_template('category.html', title='Категория 1')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')


# ============================================================
# POST-запрос (вывод в консоль)
# ============================================================

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')

    print("=" * 50)
    print("📩 НОВОЕ СООБЩЕНИЕ (Режим 1)")
    print("=" * 50)
    print(f"👤 Имя: {name}")
    print(f"📧 Email: {email}")
    print(f"📝 Сообщение: {message}")
    print("=" * 50)

    return jsonify({'success': True, 'message': 'Сообщение отправлено!'})


# ============================================================
# Обработчики ошибок
# ============================================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500