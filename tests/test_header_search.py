import allure
from allure_commons.types import Severity

from model.pages.main_page import MainPage
from model.pages.search_page import SearchPage

main_page = MainPage()
search_page = SearchPage()


@allure.feature('Поиск в хедере')
@allure.story('Позитивный поиск')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sgibneva-tl")
def test_header_search_positive(browser_setup):
    main_page.open()

    main_page.header_search('Хибины')

    search_page.search_result_success('Хибины')


@allure.feature('Поиск в хедере')
@allure.story('Негативный поиск')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Sgibneva-tl")
def test_header_search_negative(browser_setup):
    main_page.open()

    main_page.header_search('Хиhины')

    search_page.search_result_failure('Ничего не найдено по заданным критериям поиска.')
