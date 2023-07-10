import allure
from selene import browser, be

class RoutPage:

    @allure.step('Проверить результат поиска')
    def search_result_check(self):
        browser.element('.route_search_result_content').should(be.visible)