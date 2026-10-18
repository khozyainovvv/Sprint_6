from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    CONFIRM_NO = (By.XPATH, "//button[text()='Нет']")

    SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    def fill_step_1(self, name, surname, address, metro, phone):
        self.find_element(self.NAME_FIELD).send_keys(name)
        self.find_element(self.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.ADDRESS_FIELD).send_keys(address)

        metro_field = self.find_element(self.METRO_FIELD)
        metro_field.send_keys(metro)
        self.click_element((By.XPATH, f"//div[contains(@class, 'Order_Text') and text()='{metro}']"))

        self.find_element(self.PHONE_FIELD).send_keys(phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_step_2(self, date, rent_period, color):
        self.find_element(self.DATE_FIELD).send_keys(date)
        day = date.split('.')[0]
        self.click_element((By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))
        self.click_element(self.RENT_DROPDOWN)
        self.click_element((By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rent_period}']"))
        if color == "black":
            self.click_element(self.COLOR_BLACK)
        elif color == "grey":
            self.click_element(self.COLOR_GREY)
        self.find_element(self.COMMENT_FIELD).send_keys("Тестовый комментарий")
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_YES)

    def is_success_modal_displayed(self):
        return self.find_element(self.SUCCESS_TITLE).is_displayed()

    def click_view_status(self):
        self.click_element(self.VIEW_STATUS_BUTTON)