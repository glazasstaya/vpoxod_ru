import allure
import pytest
import os

from allure_commons.types import Severity

from model.utils.helper import dir_checout
from model.pages.main_page import MainPage


main_page = MainPage()


@pytest.fixture(scope='function')
def file_remove():
    yield
    dir_checout(['tests', 'resources'])
    os.remove('logo-20-years-orange.svg')


@allure.feature('Логотип')
@allure.story('Проверка размера логотипа')
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Sgibneva-tl")
def test_downloaded_file_size(file_remove):
    main_page.logo_download()

    assert main_page.logo_file_size_check() == 10739

