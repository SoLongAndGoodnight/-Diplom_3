from locators import AccountPageLocators

from .base import BasePageObject


class AccountPageObject(BasePageObject):
    def click_exit_button(self):
        self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).click()

    def click_order_history(self):
        self.driver.find_element(*AccountPageLocators.ORDER_HISTORY).click()

    def active_link(self):
        return self.driver.find_element(*AccountPageLocators.ACTIVE_ORDER_HISTORY).is_displayed()

    def exit_button_locator(self):
        return AccountPageLocators.EXIT_BUTTON

    def is_exit_button_visible(self):
        return self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).is_displayed()

    def get_last_order_number(self):
        return self.driver.find_element(*AccountPageLocators.LAST_ORDER_NUMBER).text