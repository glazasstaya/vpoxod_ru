import pytest
from selene.support.shared import browser
from model.utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.base_url = 'https://www.vpoxod.ru'
    browser.config.window_height = 1000
    browser.config.window_width = 1800

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    #attach.add_video(browser)
    browser.quit()