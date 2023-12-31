import os.path
import time

import allure
import requests
from selene import browser, have
from model.utils.helper import now_delta, dir_checout


class MainPage:

    @allure.step('Открыть главную')
    def open(self):
        browser.open('')

    @allure.step('Ввести в поле поиска {text}')
    def header_search(self, text):
        browser.element('#header-sitesearch-q').click().type(text).press_enter()
        time.sleep(2)

    @allure.step('Кликнуть на пункт меню {text}')
    def menu_click(self, text):
        browser.element(f'//*[text()="{text}"]').click()

    @allure.step('Навести мышь на пункт меню {text}')
    def menu_hover(self, text):
        browser.element(f'//*[text()="{text}"]').hover()

    @allure.step('Проверить текст {text} после перехода по меню')
    def menu_result_title(self, text):
        browser.element('.main_top').should(have.text(text))

    @allure.step('Ввести даты в поля от и до')
    def search_form_date_fill(self, min_delta, max_delta):
        browser.element('#hikesearch-date-from').set_value(now_delta(min_delta))
        browser.element('#hikesearch-date-to').set_value(now_delta(max_delta))

    @allure.step('Ввести регион (один или несколько)')
    def search_form_region_fill(self, regions):
        for region in regions:
            browser.all('.main_page_filter_box_field').element_by(have.text('РЕГИОН')).element('..').element(
                '.select2-search__field').type(region).press_enter()

    @allure.step('Ввести тип путешествия (один или несколько)')
    def search_form_trip_type_fill(self, types):
        for type in types:
            browser.all('.main_page_filter_box_field').element_by(have.text('ТИПЫ ПУТЕШЕСТВИЙ')).element('..').element(
                '.select2-search__field').type(type).press_enter()

    @allure.step('Ввести сложность путешествия (одно или несколько значений)')
    def search_form_difficult_fill(self, types):
        for type in types:
            browser.all('.main_page_filter_box_field').element_by(have.text('СЛОЖНОСТЬ')).element('..').element(
                '.select2-search__field').type(type).press_enter()

    @allure.step('Отправить форму поиска')
    def search_form_submit(self):
        browser.element('#main-page-hike-search-form button').click()

    @allure.step('Скачать логотип')
    def logo_download(self):
        dir_checout(['tests', 'resources'])
        url = 'https://www.vpoxod.ru/img/logo/logo-20-years-orange.svg'
        r = requests.get(url)
        with open('logo-20-years-orange.svg', 'wb') as file:
            file.write(r.content)

    @allure.step('Проверить размер логотипа')
    def logo_file_size_check(self):
        dir_checout(['tests', 'resources'])
        return os.path.getsize('logo-20-years-orange.svg')

