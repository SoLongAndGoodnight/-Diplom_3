from locators import ResetPasswordLocators
from .base import BasePageObject


class RestorePasswordPageObject(BasePageObject):
    def restore_password_for_email(self, email):
        self.find_element_by_locator(ResetPasswordLocators.INPUT_EMAIL).send_keys(email)
        self.find_element_by_locator(ResetPasswordLocators.RESET_BUTTON).click()

    def click_on_eye(self):
        self.find_element_by_locator(ResetPasswordLocators.EYE_SVG).click()
