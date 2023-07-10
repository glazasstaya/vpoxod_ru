from model.pages.main_page import MainPage


main_page = MainPage()


def test_menu_first_level(browser_setup):
    main_page.open()

    main_page.menu_desktop_click('Новости')

    main_page.menu_result_title('НОВОСТИ')


def test_menu_second_level(browser_setup):
    main_page.open()

    main_page.menu_desktop_hover('О нас ')
    main_page.menu_desktop_click('Клуб Приключений')

    main_page.menu_result_title('ТУРКЛУБ АКТИВНОГО ТУРИЗМА')


def test_menu_third_level(browser_setup):
    main_page.open()

    main_page.menu_desktop_hover('Типы')
    main_page.menu_desktop_click('Сплав')

    main_page.menu_result_title('СПЛАВ')



