import time
from locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from .base import BasePageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class MainPageObject(BasePageObject):
    def waiting_element_bun(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

    def drag_and_drop(self):
        bun = self.driver.find_element(*MainPageLocators.BUN)
        cart = self.driver.find_element(*MainPageLocators.CART)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(bun, cart).perform()
        time.sleep(2)

    def complete_order_and_check_modal(self):
        self.driver.find_element(*MainPageLocators.BUTTON_COMPLETE_ORDER).click()
        modal_order_complete = self.driver.find_element(*MainPageLocators.MODAL_ORDER_NUMBER)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.MODAL_ORDER_NUMBER))

        return modal_order_complete.is_displayed()