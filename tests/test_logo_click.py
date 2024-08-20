import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogo:
    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"-')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.wait_up_button_order()
        main_page.click_up_button_order()
        main_page.wait_logo_scooter()
        main_page.click_logo_scooter()
        main_page.wait_visibility_main_header()
        assert main_page.check_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" по клику на логотип "Яндекс"-')
    def test_logo_ya(self, driver):
        main_page = MainPage(driver)
        main_page.wait_logo_ya()
        main_page.click_logo_ya()
        main_page.go_next_tab()
        assert main_page.get_title() == 'Дзен'