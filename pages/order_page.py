import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить шаг 1: имя={name}, фамилия={surname}, адрес={address}, метро={metro}, телефон={phone}")
    def fill_step_1(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

        metro_field = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_field.send_keys(metro)
        self.click_element(OrderPageLocators.metro_option(metro))

        self.find_element(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить шаг 2: дата={date}, срок={rent_period}, цвет={color}")
    def fill_step_2(self, date, rent_period, color):
        self.find_element(OrderPageLocators.DATE_FIELD).send_keys(date)
        day = date.split('.')[0]
        self.click_element(OrderPageLocators.date_day(day))

        self.click_element(OrderPageLocators.RENT_DROPDOWN)
        self.click_element(OrderPageLocators.rent_option(rent_period))

        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

        self.find_element(OrderPageLocators.COMMENT_FIELD).send_keys("Тестовый комментарий")
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES)

    @allure.step("Проверить, что модальное окно «Заказ оформлен» отображается")
    def is_success_modal_displayed(self):
        return self.find_element(OrderPageLocators.SUCCESS_TITLE).is_displayed()

    @allure.step("Клик по кнопке «Посмотреть статус»")
    def click_view_status(self):
        self.click_element(OrderPageLocators.VIEW_STATUS_BUTTON)