from selene import browser, be

class RoutPage:

    def search_result_check(self):
        browser.element('.route_search_result_content').should(be.visible)