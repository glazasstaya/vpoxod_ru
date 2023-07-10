from model.pages.main_page import MainPage
from model.data.data_objects import MainSearchForm
from model.pages.route_page import RoutPage
from model.utils.helper import scroll_to_element


main_page = MainPage()
route_page = RoutPage()


def test_main_search_form_success():
    search_data = MainSearchForm(first_date_delta=1,
                                 second_date_delta=100,
                                 regions=['Кавказ', 'Алтай'],
                                 trip_types=['Горный'],
                                 difficult=['Средняя'])

    main_page.open()
    scroll_to_element('.main_slider_pager')

    main_page.search_form_date_fill(search_data.first_date_delta, search_data.second_date_delta)
    main_page.search_form_region_fill(search_data.regions)
    main_page.search_form_trip_type_fill(search_data.trip_types)
    main_page.search_form_difficult_fill(search_data.difficult)
    main_page.search_form_submit()

    scroll_to_element('#text1')
    route_page.search_result_check()