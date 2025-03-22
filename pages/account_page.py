from locators import AccountPageLocators

from .base import BasePageObject


class AccountPageObject(BasePageObject):
    def click_exit_button(self):
        self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).click()

    def click_order_history(self):
        self.driver.find_element(*AccountPageLocators.ORDER_HISTORY).click()

    def active_link(self):
        return self.driver.find_element(*AccountPageLocators.ACTIVE_ORDER_HISTORY).is_displayed()