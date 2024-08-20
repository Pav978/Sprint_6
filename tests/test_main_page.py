import allure
import pytest
from pages.main_page import MainPage
from conftest import driver
from data import AnswerQuestion



class TestChapterQuestion:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка на наличие нужного текста в выпадающих списках раздела')
    @pytest.mark.parametrize('question_number, expected_answer', AnswerQuestion.test_data_answer)
    def test_click_text_question(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_click_faq_items(question_number)
        main_page.wait_visibility_answer(question_number)
        assert main_page.get_display_text_answer(question_number) == expected_answer