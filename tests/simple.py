'''
1. Поиск в шапке позитивный test_search_header_positive
2. Поиск в шапке негативный test_search_header_negative
3 - 4. Проверка меню (xpath) test_menu_simple
5. Скачать логотип, проверить размер фото -test_downloaded_file_size
6. Календарь походов - фильтрация по цене - test_search_form
7. форма поиска на главной - test_search_form_main
'''
import time

from model.pages.main_page import MainPage
from model.pages.search_page import SearchPage
from model.pages.news_page import NewsPage
from model.pages.route_page import RoutPage
from model.pages.allroutes import AllroutesPage
from model.utils.helper import scroll_to_element
from model.data.data_objects import MainSearchForm, AllroutsSearchForm

main_page = MainPage()
search_page = SearchPage()
news_page = NewsPage()
route_page = RoutPage()
allroutes_page = AllroutesPage()


def test_search_header_positive():
    main_page.open()
    main_page.header_search('Хибины')
    search_page.search_result_success('Хибины')


def test_search_header_negative():
    main_page.open()
    main_page.header_search('Хиhины')
    search_page.search_result_failure('Ничего не найдено по заданным критериям поиска.')


def test_menu_simple_desctop():  # для параметризации
    main_page.open()
    main_page.menu_desktop_click('Новости')
    news_page.title('НОВОСТИ')


def test_menu_simple_mobile():  # для параметризации
    main_page.open()
    main_page.mobile_burger_button_click()
    main_page.menu_mobile_click('Новости')
    news_page.title('НОВОСТИ')


def test_search_form_main():
    search_data = MainSearchForm(first_date_delta=1,
                                 second_date_delta=100,
                                 regions=['Кавказ', 'Алтай'],
                                 trip_types=['Горный'],
                                 difficult=['Средняя'])

    main_page.open()
    scroll_to_element('.main_slider_pager')

    main_page.search_form_date_fill(search_data.first_date_delta, search_data.second_date_delta)
    main_page.search_form_region_fill(search_data.regions)
    main_page.search_form_trip_type_fill(search_data.trip_types)
    main_page.search_form_difficult_fill(search_data.difficult)
    main_page.search_form_submit()

    scroll_to_element('#text1')
    route_page.search_result_check()


def test_search_form():
    search_data = AllroutsSearchForm(min_price=29000,
                                     max_price=45000)

    allroutes_page.open()
    #очищаем результаты поиска
    allroutes_page.max_cost_fill(0)
    time.sleep(2)

    allroutes_page.min_cost_fill(search_data.min_price)
    allroutes_page.max_cost_fill(search_data.max_price)

    allroutes_page.search_result_success('Найден')
    assert allroutes_page.price() >= search_data.min_price
    assert allroutes_page.price() <= search_data.max_price


def test_downloaded_file_size():
    main_page.logo_download()

    assert main_page.logo_file_size_check() == 10739

    #TODO в фикстуру
    #os.remove(download_file)
