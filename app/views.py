from flask import render_template

def contacts():
    """Страница контактов"""
    return render_template('contacts.html', title='Контакты')

def index():
    """Главная страница"""
    return render_template('index.html', title='Главная')

def category():
    """Страница категории"""
    return render_template('category.html', title='Категория 1')