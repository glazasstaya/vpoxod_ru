from selene import browser, have


class NewsPage:

    def open(self):
        browser.open('/news')

    def title(self, text):
        browser.element('.main_top').should(have.text(text))