from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AccountPageLocators

from .base import BasePageObject


class AccountPageObject(BasePageObject):
    def click_exit_button(self):
        self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).click()

    def click_order_history(self):
        self.driver.find_element(*AccountPageLocators.ORDER_HISTORY).click()

    def active_link(self):
        return self.driver.find_element(*AccountPageLocators.ACTIVE_ORDER_HISTORY).is_displayed()

    def exit_button_displayed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(AccountPageLocators.EXIT_BUTTON))
        return self.driver.find_element(*AccountPageLocators.EXIT_BUTTON).is_displayed()

    def get_last_order_number(self):
        return self.driver.find_element(*AccountPageLocators.LAST_ORDER_NUMBER).text
