import allure
from selene import browser, have, query


class AllroutesPage:

    @allure.step('Открыть страницу Все путешествия')
    def open(self):
        browser.open('/allroutes')

    @allure.step('Заполнить поле максимальной цены')
    def max_cost_fill(self, cost):
        browser.element('#max-cost').set_value(str(cost)).press_enter()

    @allure.step('Заполнить поле минимальной цены')
    def min_cost_fill(self, cost):
        browser.element('#min-cost').set_value(str(cost)).press_enter()

    @allure.step('Проверить результат поиска')
    def search_result_success(self, text):
        browser.element('.route_search_counters').should(have.text(text))

    def price(self):
        price = browser.all('.table_price_right')[0].get(query.text)
        return int(''.join(c for c in price if c.isdigit()))

