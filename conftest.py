import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.base_url = 'https://www.vpoxod.ru'
    browser.config.window_height = 1000
    browser.config.window_width = 1800

    yield browser
    browser.quit()