from . import app  # относительный импорт из текущего пакета
from .views import index, contacts, category

# Маршруты
# Для задания 2 (раскомментировать при необходимости)
# app.add_url_rule('/', view_func=contacts, methods=['GET'])
# app.add_url_rule('/<path:path>', view_func=contacts, methods=['GET'])

@app.errorhandler(404)
def page_not_found(e):
    from .views import contacts
    return contacts()