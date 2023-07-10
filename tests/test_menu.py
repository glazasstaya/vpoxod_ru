import allure
from allure_commons.types import Severity
from model.pages.main_page import MainPage


main_page = MainPage()


@allure.feature('Меню')
@allure.story('Проверка пунктов меню первого уровня')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sgibneva-tl")
def test_menu_first_level(browser_setup):
    main_page.open()

    main_page.menu_click('Новости')

    main_page.menu_result_title('НОВОСТИ')


@allure.feature('Меню')
@allure.story('Проверка пунктов меню второго уровня')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sgibneva-tl")
def test_menu_second_level(browser_setup):
    main_page.open()

    main_page.menu_hover('О нас ')
    main_page.menu_click('Клуб Приключений')

    main_page.menu_result_title('ТУРКЛУБ АКТИВНОГО ТУРИЗМА')


@allure.feature('Меню')
@allure.story('Проверка пунктов меню третьего уровня')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sgibneva-tl")
def test_menu_third_level(browser_setup):
    main_page.open()

    main_page.menu_hover('Типы')
    main_page.menu_click('Сплав')

    main_page.menu_result_title('СПЛАВ')



