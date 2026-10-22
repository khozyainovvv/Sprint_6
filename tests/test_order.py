import pytest
import allure
from data.urls import BASE_URL, YANDEX_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Заказ самоката через верхнюю кнопку «Заказать»")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, rent_period, color", [
        ("Иван", "Иванов", "Москва, ул. Ленина, 1", "Черкизовская", "+79991234567", "15.10.2026", "сутки", "black"),
    ])
    def test_order_top(self, driver, name, surname, address, metro, phone, date, rent_period, color):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.fill_step_1(name, surname, address, metro, phone)
        order_page.fill_step_2(date, rent_period, color)

        assert order_page.is_success_modal_displayed(), "Модальное окно «Заказ оформлен» не появилось"

        order_page.click_view_status()
        main_page.click_logo_scooter()
        assert "qa-scooter" in main_page.get_current_url(), "Не перешли на главную «Самоката»"

    @allure.title("Заказ самоката через нижнюю кнопку «Заказать»")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, rent_period, color", [
        ("Пётр", "Петров", "Москва, ул. Пушкина, 2", "Сокольники", "+79997654321", "20.10.2026", "двое суток", "grey"),
    ])
    def test_order_bottom(self, driver, name, surname, address, metro, phone, date, rent_period, color):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_step_1(name, surname, address, metro, phone)
        order_page.fill_step_2(date, rent_period, color)

        assert order_page.is_success_modal_displayed(), "Модальное окно «Заказ оформлен» не появилось"

        order_page.click_view_status()
        main_page.click_logo_scooter()
        assert "qa-scooter" in main_page.get_current_url(), "Не перешли на главную «Самоката»"

    @allure.title("Проверка логотипа «Яндекс»")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_logo_yandex()

        main_page.switch_to_new_window()
        main_page.wait_for_url_contains(YANDEX_URL)
        assert YANDEX_URL in main_page.get_current_url(), "Не перешли на Яндекс"