'''
1. Поиск в шапке позитивный test_search_header_positive
2. Поиск в шапке негативный test_search_header_negative
3 - 4. Проверка меню (xpath) test_menu_simple
5. Скачать логотип, проверить размер фото -test_downloaded_file_size
6. Календарь походов - фильтрация по цене - test_search_form
7. форма поиска на главной - test_search_form_main
'''
from datetime import datetime, timedelta

from selene import browser, have, be, command, query

import os.path
import requests

def test_search_header_positive():
    browser.open('https://www.vpoxod.ru/')
    browser.element('#header-sitesearch-q').click().type('Хибины').press_enter()

    browser.element('.search-item[data-key="0"]').should(have.text('Хибины'))


def test_search_header_negative():
    browser.open('https://www.vpoxod.ru/')
    browser.element('#header-sitesearch-q').click().type('Хиpины').press_enter()

    browser.element('#site-search').should(have.text('Ничего не найдено по заданным критериям поиска.'))

def test_menu_simple_desctop(): #для параметризации
    browser.open('https://www.vpoxod.ru/')
    browser.element('//nav/ul/li/a[text()="Новости"]').click()
    browser.element('.main_top').should(have.text('НОВОСТИ'))

def test_menu_simple_mobile(): #для параметризации
    browser.open('https://www.vpoxod.ru/')
    #клик в меню
    browser.element('//nav/div/divul/li/a[text()="Новости"]').click()
    browser.element('h1').should(have.text('НОВОСТИ'))


def test_search_form_main():
    date1 = (datetime.now()).strftime("%d.%m.%Y")
    date2 = (datetime.now() + timedelta (days=60)).strftime("%d.%m.%Y")
    browser.open('https://www.vpoxod.ru/')
    browser.element('.main_slider_pager').perform(command.js.scroll_into_view)
    browser.element('#hikesearch-date-from').set_value(date1)
    browser.element('#hikesearch-date-to').set_value(date2)
    browser.all('.main_page_filter_box_field').element_by(have.text('РЕГИОН')).element('..').element(
        '.select2-search__field').type('Кавказ').press_enter()
    browser.all('.main_page_filter_box_field').element_by(have.text('ТИПЫ ПУТЕШЕСТВИЙ')).element('..').element(
        '.select2-search__field').type('Горные').press_enter()
    browser.all('.main_page_filter_box_field').element_by(have.text('СЛОЖНОСТЬ')).element('..').element(
        '.select2-search__field').type('Средняя').press_enter()
    browser.element('#main-page-hike-search-form button').click()
    browser.element('#text1').perform(command.js.scroll_into_view)
    browser.element('.route_search_result_content').should(be.visible)

def test_search_form():
    min_price = '29000'
    max_price = '45000'
    browser.open('https://www.vpoxod.ru/allroutes')
    browser.element('#max-cost').type('0').press_enter()
    browser.element('.route_search_result_content .pt-md').should(have.text('ничего не нашлось'))

    browser.element('#min-cost').type(min_price).press_enter()
    browser.element('#max-cost').set_value(max_price).press_enter()
    browser.element('.route_search_counters').should(have.text('Найден'))
    price = browser.all('.table_price_right')[0].get(query.text)
    price = ''.join(c for c in price if c.isdigit())
    assert int(price) >= int(min_price)
    assert int(price) <= int(max_price)





def test_downloaded_file_size():
    current_dir= os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.dirname(os.path.join(current_dir, 'resources'))
    os.chdir(download_dir)
    url = 'https://www.vpoxod.ru/img/logo/logo-20-years-orange.svg'

    r = requests.get(url)
    with open('logo-20-years-orange.svg', 'wb') as file:
        file.write(r.content)
    size = os.path.getsize('logo-20-years-orange.svg')

    assert size == 10739

    download_file = os.path.join(download_dir, 'logo-20-years-orange.svg')
    os.remove(download_file)

