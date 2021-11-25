"""СКРИПТ ДЛЯ ПАРСИНГА
сайт: sanremer.ru
Скрипт вынесен отдельно чтоб в основной программе можно было переключаться на парсинг разных сайтов"""

from bs4 import BeautifulSoup
from Request import get_html, get_response


def get_link(response_html):
    soup = BeautifulSoup(response_html, 'html.parser')

    items = soup.find_all('div', class_='right-block')
    if items:
        link = items[0].find('a', class_='product-name').get('href')
        return link
    else:
        link = None
        return link


def get_content(link, HEADERS):
    request = get_html(link, HEADERS)
    response = get_response(request)

    soup = BeautifulSoup(response, 'html.parser')

    items = soup.find('div', class_='rte').text
    #   print('[TEST]', items)
    return items