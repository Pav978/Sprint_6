import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData

class OrderPage(BasePage):
#1
    @allure.step('Заполнение формы №1-')
    def input_data_in_first_form(self, test_data: object) -> object:
        self.wait_visibility_element(OrderPageLocators.name)
        self.click_element(OrderPageLocators.name)
        self.input_keys(OrderPageLocators.name, test_data[0])
        self.click_element(OrderPageLocators.lastname)
        self.input_keys(OrderPageLocators.lastname, test_data[1])
        self.click_element(OrderPageLocators.address)
        self.input_keys(OrderPageLocators.address, test_data[2])
        self.click_element(OrderPageLocators.metro)
        self.input_keys(OrderPageLocators.metro, test_data[3])
        self.click_element(OrderPageLocators.choice_metro)
        self.click_element(OrderPageLocators.phone)
        self.input_keys(OrderPageLocators.phone, test_data[4])
        self.click_element(OrderPageLocators.button_next)
#2
    @allure.step('Заполнение формы 2-')
    def input_data_in_second_form(self, test_data):
        self.wait_visibility_element(OrderPageLocators.date)
        self.click_element(OrderPageLocators.date)
        self.input_keys(OrderPageLocators.date, test_data[5])
        self.click_element(OrderPageLocators.color_scooter)
        self.click_element(OrderPageLocators.renta_term)
        self.click_element(OrderPageLocators.term_renta)
        self.click_element(OrderPageLocators.commit)
        self.input_keys(OrderPageLocators.commit, test_data[6])
        self.click_element(OrderPageLocators.button_order)
        self.wait_visibility_element(OrderPageLocators.button_confirm_order)
        self.click_element(OrderPageLocators.button_confirm_order)
#3
    @allure.step('Клик по станции метро из списка-')
    def choice_metro(self):
        self.click_element(OrderPageLocators.choice_metro)
#4
    @allure.step('Ввод даты доставки самоката-')
    def send_keys_date_by_keyboard_input(self):
        self.input_keys(OrderPageLocators.date).send_keys(TestData.data_first_person[5])
#5
    @allure.step('Клик по выпадающему календарю')
    def click_date_in_calendar(self):
        self.click_element(OrderPageLocators.calendar_item)
#6
    @allure.step('Проверка отображения кнопки "Посмотреть статус"-')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_element(OrderPageLocators.button_view_order)