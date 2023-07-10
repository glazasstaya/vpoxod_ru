import pytest
import os
from selene.support.shared import browser
from model.utils.helper import dir_checout


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://www.vpoxod.ru'
    browser.config.window_height = 1000
    browser.config.window_width = 1800

    yield browser
    browser.quit()


