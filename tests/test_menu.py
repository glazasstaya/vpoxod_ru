from model.pages.main_page import MainPage
from model.pages.news_page import NewsPage


news_page = NewsPage()
main_page = MainPage()


def test_menu_simple_desctop():  # для параметризации
    main_page.open()

    main_page.menu_desktop_click('Новости')

    news_page.title('НОВОСТИ')


def test_menu_simple_mobile():  # для параметризации
    main_page.open()

    main_page.mobile_burger_button_click()
    main_page.menu_mobile_click('Новости')

    news_page.title('НОВОСТИ')
