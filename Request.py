"""Стандартные фунцкции для парсинга
Вхоные данные: урл адрес, хедер, реквест (тот что из главной программы, а не библиотеки)"""

import requests


def get_html(url, HEADERS, param=None):  # Получаем реквест страницы
    r = requests.get(url, headers=HEADERS, params=param)  # Делаем запрос и сохраняем его
    return r  # возвращаем запрос


def get_response(request):
    response_html = request.text
    if request.status_code == 200:
        return response_html
    else:
        return None
