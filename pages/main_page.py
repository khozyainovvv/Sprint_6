from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    FAQ_QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    FAQ_ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']//p")

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_BUTTON, timeout=5)
        except Exception:
            pass

    def click_faq_question(self, index):
        locator = (self.FAQ_QUESTION[0], self.FAQ_QUESTION[1].format(index))
        self.click_element(locator)

    def get_faq_answer(self, index):
        locator = (self.FAQ_ANSWER[0], self.FAQ_ANSWER[1].format(index))
        return self.get_text(locator)

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click_element(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)