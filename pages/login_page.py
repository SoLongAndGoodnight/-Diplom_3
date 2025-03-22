from locators import LoginPageLocators
from .base import BasePageObject


class LoginPageObject(BasePageObject):
    def fill_login_field(self, input_email):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(input_email)

    def fill_password_field(self, input_password):
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(input_password)

    def click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def click_profile_button(self):
        self.driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()

    def check_submit_button_visible(self):
         return self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()