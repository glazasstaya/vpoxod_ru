from selene import browser, have, query


class AllroutesPage:

    def open(self):
        browser.open('/allroutes')

    def max_cost_fill(self, cost):
        browser.element('#max-cost').set_value(str(cost)).press_enter()

    def min_cost_fill(self, cost):
        browser.element('#min-cost').set_value(str(cost)).press_enter()

    def search_result_failure(self, text):
        browser.element('.route_search_result_content .pt-md').should(have.text(text))

    def search_result_success(self, text):
        browser.element('.route_search_counters').should(have.text(text))

    def price(self):
        price = browser.all('.table_price_right')[0].get(query.text)
        return int(''.join(c for c in price if c.isdigit()))

