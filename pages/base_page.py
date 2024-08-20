import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
#1
    @allure.step('Скролл до нужного элемента списка-')
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
#2
    @allure.step('Загрузка элемента списка-')
    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))
#3
    @allure.step('Клик элемента-')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()
#4
    @allure.step('Ввод данных в поле "ввод"-')
    def input_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)
#5
    @allure.step('Получение текста из названия элемента-')
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text
#6
    @allure.step('Переход к следующей вкладке-')
    def go_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
#7
    @allure.step('Получение заголовка страницы-')
    def get_title(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(
            MainPageLocators.title_dzen))
        return self.driver.title
#8
    @allure.step('Проверка отображения элемента на странице-')
    def check_displaying_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()