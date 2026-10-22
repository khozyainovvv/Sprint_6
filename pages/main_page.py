import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON, timeout=5)
        except Exception:
            pass

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index):
        locator = (MainPageLocators.FAQ_QUESTION[0], MainPageLocators.FAQ_QUESTION[1].format(index))
        self.click_element(locator)

    @allure.step("Получить ответ FAQ с индексом {index}")
    def get_faq_answer(self, index):
        locator = (MainPageLocators.FAQ_ANSWER[0], MainPageLocators.FAQ_ANSWER[1].format(index))
        return self.get_text(locator)

    @allure.step("Клик по верхней кнопке «Заказать»")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке «Заказать»")
    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу «Самокат»")
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу «Яндекс»")
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)