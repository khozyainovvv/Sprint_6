import pytest
import allure
from data.faq_data import FAQ_DATA
from data.urls import BASE_URL
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Проверка ответа на вопрос FAQ")
    @pytest.mark.parametrize("index, expected_answer", FAQ_DATA)
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer(index)
        assert actual_answer == expected_answer, f"Ответ для вопроса {index} не совпадает"