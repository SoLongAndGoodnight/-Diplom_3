from locators import LoginPageLocators
from .base import BasePageObject


class LoginPageObject(BasePageObject):
    def fill_login_field(self, input_email: str):
        element = self.find_visible_element_by_locator(LoginPageLocators.INPUT_EMAIL)
        element.send_keys(input_email)

    def fill_password_field(self, input_password):
        element = self.find_visible_element_by_locator(LoginPageLocators.INPUT_PASSWORD)
        element.send_keys(input_password)

    def click_submit_button(self):
        element = self.find_visible_element_by_locator(LoginPageLocators.SUBMIT_BUTTON)
        element.click()

    def login(self, email, password):
        self.fill_login_field(email)
        self.fill_password_field(password)
        self.click_submit_button()

    def click_profile_button(self):
        element = self.find_visible_element_by_locator(LoginPageLocators.PROFILE_BUTTON)
        element.click()

    def check_submit_button_visible(self):
        element = self.find_visible_element_by_locator(LoginPageLocators.SUBMIT_BUTTON)
        return element

    def go_to_profile(self):
        element = self.find_visible_element_by_locator(LoginPageLocators.PROFILE_BUTTON)
        element.click()

    def click_restore_password(self):
        element = self.find_visible_element_by_locator(LoginPageLocators.RESTORE_PASSWORD_LINK)
        element.click()

    def email_field_displayed_and_enabled(self):
        password_input = self.find_visible_element_by_locator(LoginPageLocators.ACTIVE_EMAIL_FIELD)
        return password_input.is_displayed() and password_input.is_enabled()
