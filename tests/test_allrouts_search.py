import time
import pytest

from model.pages.allroutes_page import AllroutesPage
from model.data.data_objects import AllroutsSearchForm


allroutes_page = AllroutesPage()


@pytest.fixture(scope='function')
def result_clear():
    allroutes_page.open()
    allroutes_page.max_cost_fill(0)
    time.sleep(2)


def test_price_search_success(result_clear):
    search_data = AllroutsSearchForm(min_price=29000,
                                     max_price=45000)

    allroutes_page.min_cost_fill(search_data.min_price)
    allroutes_page.max_cost_fill(search_data.max_price)

    allroutes_page.search_result_success('Найден')
    assert allroutes_page.price() >= search_data.min_price
    assert allroutes_page.price() <= search_data.max_price
