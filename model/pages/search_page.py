from selene import browser, have

class SearchPage:

    def search_result_success(self, text):
        browser.element('.search-item[data-key="0"]').should(have.text(text))

    def search_result_failure(self, text):
        browser.element('#site-search').should(have.text(text))