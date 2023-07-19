import time
import allure
import pytest
from allure_commons.types import Severity
from selene import browser

from model.pages.allroutes_page import AllroutesPage
allroutes_page = AllroutesPage()


@pytest.fixture(scope='function')
def result_clear():
    allroutes_page.open()
    allroutes_page.max_cost_fill(0)
    time.sleep(3)


@pytest.mark.parametrize('price1, price2', [(29000, 45000), (0, 3000), (45000, 90000)])
@allure.feature('Все путешествия: большая форма поиска')
@allure.story('Поиск по цене')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sgibneva-tl")
def test_price_search_success(browser_setup, result_clear, price1, price2):
    min_price = price1
    max_price = price2

    allroutes_page.min_cost_fill(min_price)
    allroutes_page.max_cost_fill(max_price)
    time.sleep(6)

    allroutes_page.search_result_success('Найден')
    allroutes_page.price_check(min_price, max_price)