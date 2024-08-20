import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
#1
    @allure.step('Ожидание загрузки верхней кнопки "Заказать" на странице заказа-')
    def wait_up_button_order(self):
        self.wait_visibility_element(MainPageLocators.up_button_order)
#2
    @allure.step('Клик по верхней кнопке "Заказать-"')
    def click_up_button_order(self):
        self.click_element(MainPageLocators.up_button_order)
#3
    @allure.step('Ожидание загрузки логотипа "Самокат"-')
    def wait_logo_scooter(self):
        self.wait_visibility_element(MainPageLocators.logo_scooter)
#4
    @allure.step('Ожидание загрузки логотипа "Яндекс"-')
    def wait_logo_ya(self):
        self.wait_visibility_element(MainPageLocators.logo_ya)
#5
    @allure.step('Клик по логотипу "Самокат"-')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.logo_scooter)
#6
    @allure.step('Клик по логотипу "Яндекс"-')
    def click_logo_ya(self):
        self.click_element(MainPageLocators.logo_ya)
#7
    @allure.step('Ожидание загрузки заголовка на стартовой странице-')
    def wait_visibility_main_header(self):
        self.wait_visibility_element(MainPageLocators.main_header)
#8
    @allure.step('Проверка заголовка стартовой страницы-')
    def check_main_header(self):
        return self.check_displaying_element(MainPageLocators.main_header)
#9

    @allure.step('Скролл и клик по вопросу из раздела "Вопросы о важнoм"-')
    def scroll_click_faq_items(self, data):
        self.scroll_element(MainPageLocators.questions)
        self.wait_visibility_element(MainPageLocators.questions_items[data])
        self.click_element(MainPageLocators.questions_items[data])
#10
    @allure.step('Ожидание ответа на вопрос-')
    def wait_visibility_answer(self, data):
        self.wait_visibility_element(MainPageLocators.answers_items[data])
#11
    @allure.step('Получение номера ответа-')
    def get_display_text_answer(self, data):
        return self.get_text_element(MainPageLocators.answers_items[data])