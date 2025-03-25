from locators import AccountPageLocators
from .base import BasePageObject


class AccountPageObject(BasePageObject):
    def click_exit_button(self):
        element = self.find_visible_element_by_locator(AccountPageLocators.EXIT_BUTTON)
        element.click()

    def click_order_history(self):
        self.find_visible_element_by_locator(AccountPageLocators.ORDER_HISTORY).click()

    def active_link_displayed(self):
        return self.find_element_by_locator(AccountPageLocators.ACTIVE_ORDER_HISTORY).is_displayed()

    def exit_button_displayed(self):
        return self.find_visible_element_by_locator(AccountPageLocators.EXIT_BUTTON).is_displayed()

    def get_last_order_number(self):
        return self.find_visible_element_by_locator(AccountPageLocators.LAST_ORDER_NUMBER).text
