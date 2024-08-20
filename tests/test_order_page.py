import allure
import pytest
from conftest import driver
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import *



class TestOrder:
    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка оформления заказа через вход в двух точках')
    @pytest.mark.parametrize('button, test_data', [(MainPageLocators.up_button_order, TestData.data_first_person),
                                                   (MainPageLocators.order_button_in_main, TestData.data_second_person)])
    def test_enter_two_points(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_element(button)
        order_page.wait_visibility_element(button)
        order_page.click_element(button)
        order_page.input_data_in_first_form(test_data)
        order_page.input_data_in_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()