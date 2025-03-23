from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators
from .base import BasePageObject


class LoginPageObject(BasePageObject):
    def fill_login_field(self, input_email):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(input_email)

    def fill_password_field(self, input_password):
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(input_password)

    def click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def login(self, email, password):
        self.fill_login_field(email)
        self.fill_password_field(password)
        self.click_submit_button()

    def click_profile_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.PROFILE_BUTTON))
        self.driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()

    def check_submit_button_visible(self):
         return self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()

    def profile_button_locator(self):
        return LoginPageLocators.PROFILE_BUTTON

    def go_to_profile(self):
        """Переход в профиль через кнопку 'Личный кабинет'."""
        self.driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()
