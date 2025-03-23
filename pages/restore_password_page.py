from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ResetPasswordLocators
from .base import BasePageObject


class RestorePasswordPageObject(BasePageObject):
    def restore_password_for_email(self, param):
        self.driver.find_element(*ResetPasswordLocators.INPUT_EMAIL).send_keys("lizakorotkova17123@yandex.ru")
        self.driver.find_element(*ResetPasswordLocators.RESET_BUTTON).click()

    def click_on_eye(self):
        self.driver.find_element(*ResetPasswordLocators.EYE_SVG).click()
