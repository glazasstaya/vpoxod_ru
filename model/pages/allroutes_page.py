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

    @allure.step('Проверить вхождение цены в заданный диапазон')
    def price_check(self, min_price, max_price):
        prices = browser.all('.table_price_right')
        for price in prices:
            price_string = price.get(query.text)
            price_value = int(''.join(c for c in price_string if c.isdigit()))
            print(price_value)
            assert price_value >= min_price
            assert price_value <= max_price

