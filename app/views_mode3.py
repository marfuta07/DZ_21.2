from flask import request, jsonify, make_response
from app import app


# ============================================================
# РЕЖИМ 3: Задание 2 (with open + Content-Type: text/html)
# ============================================================

@app.route('/')
@app.route('/<path:path>')
def contacts_all(path=None):
    """Чтение HTML через with open() + Content-Type: text/html"""
    try:
        with open('app/templates/contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    except FileNotFoundError:
        return render_template('404.html'), 404


@app.route('/contacts')
def contacts():
    """Страница контактов с with open()"""
    try:
        with open('app/templates/contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    except FileNotFoundError:
        return render_template('404.html'), 404


# ============================================================
# POST-запрос (вывод в консоль)
# ============================================================

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')

    print("=" * 50)
    print("📩 НОВОЕ СООБЩЕНИЕ (Режим 3 - with open)")
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
    try:
        with open('app/templates/404.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        response = make_response(html_content, 404)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1>", 404


@app.errorhandler(500)
def internal_server_error(e):
    try:
        with open('app/templates/500.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        response = make_response(html_content, 500)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    except FileNotFoundError:
        return "<h1>500 - Ошибка сервера</h1>", 500
