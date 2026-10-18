import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("entry_point, name, surname, address, metro, phone, date, rent_period, color", [
        ("top", "Иван", "Иванов", "Москва, ул. Ленина, 1", "Черкизовская", "+79991234567", "15.10.2026", "сутки", "black"),
        ("bottom", "Пётр", "Петров", "Москва, ул. Пушкина, 2", "Сокольники", "+79997654321", "20.10.2026", "двое суток", "grey"),
    ])
    def test_order_scooter(self, driver, entry_point, name, surname, address, metro, phone, date, rent_period, color):
        main_page = MainPage(driver)
        main_page.driver.get("https://qa-scooter.education-services.ru/")
        main_page.accept_cookies()

        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_step_1(name, surname, address, metro, phone)

        order_page.fill_step_2(date, rent_period, color)

        assert order_page.is_success_modal_displayed(), "Модальное окно «Заказ оформлен» не появилось"

        order_page.click_view_status()

        main_page.click_logo_scooter()
        assert "qa-scooter" in driver.current_url, "Не перешли на главную «Самоката»"

    @allure.title("Проверка логотипа «Яндекс»")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.driver.get("https://qa-scooter.education-services.ru/")
        main_page.accept_cookies()
        main_page.click_logo_yandex()
        assert len(driver.window_handles) == 2, "Новое окно не открылось"