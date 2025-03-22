from locators import AccountPageLocators

from .base import BasePageObject


class AccountPageObject(BasePageObject):
    def click_exit_button(self):
        self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).click()