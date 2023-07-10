import time
import allure
import pytest

from model.pages.allroutes_page import AllroutesPage
allroutes_page = AllroutesPage()


@pytest.fixture(scope='function')
def result_clear():
    allroutes_page.open()
    allroutes_page.max_cost_fill(0)
    time.sleep(2)


@pytest.mark.parametrize('price1, price2', [(29000, 45000), (0, 3000), (45000, 90000)])
def test_price_search_success(browser_setup, result_clear, price1, price2):
    min_price = price1
    max_price = price2

    allroutes_page.min_cost_fill(min_price)
    allroutes_page.max_cost_fill(max_price)
    time.sleep(2)

    allroutes_page.search_result_success('Найден')
    with allure.step('Проверить вождение цены в заданный диапазон'):
        assert allroutes_page.price() >= min_price
        assert allroutes_page.price() <= max_price
