from model.pages.main_page import MainPage
from model.pages.search_page import SearchPage

main_page = MainPage()
search_page = SearchPage()


def test_header_search_positive():
    main_page.open()

    main_page.header_search('Хибины')

    search_page.search_result_success('Хибины')


def test_header_search_negative():
    main_page.open()

    main_page.header_search('Хиhины')

    search_page.search_result_failure('Ничего не найдено по заданным критериям поиска.')
