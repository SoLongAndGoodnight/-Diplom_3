import time
from locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from .base import BasePageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class MainPageObject(BasePageObject):
    def wait_for_bun(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

    def drag_and_drop_bun_to_cart(self):
        bun = self.driver.find_element(*MainPageLocators.BUN)
        cart = self.driver.find_element(*MainPageLocators.CART)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(bun, cart).perform()
        time.sleep(2)

    def complete_order(self):
        self.driver.find_element(*MainPageLocators.BUTTON_COMPLETE_ORDER).click()

    def complete_order_and_check_modal(self):
        self.complete_order()

        modal_order_complete = self.driver.find_element(*MainPageLocators.MODAL_ORDER_NUMBER)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.MODAL_ORDER_NUMBER))

        return modal_order_complete.is_displayed()

    def get_bun_counter(self):
        return self.driver.find_element(*MainPageLocators.BUN_COUNTER).text

    def get_bun(self):
        return self.driver.find_element(*MainPageLocators.BUN)

    def click_bun(self):
        self.get_bun().click()

    def is_modal_open(self):
        return self.driver.find_element(*MainPageLocators.MODAL_BUN).is_displayed()

    def close_modal(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BUTTON))
        self.driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

    def modal_wrapper_locator(self):
        return MainPageLocators.MODAL_WRAPPER

    def is_modal_closed(self):
        return not self.driver.find_element(*MainPageLocators.MODAL_WRAPPER).is_displayed()

    def check_bun_is_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

    def go_to_constructor(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def wait_for_order_number_updated(self):
        WebDriverWait(self.driver, 7).until(
            lambda d: self.driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text != "9999"
        )

    def get_order_number(self):
        return self.driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text

    def click_orders_button(self):
        self.driver.find_element(*MainPageLocators.ORDERS_BUTTON).click()

    def order_page_is_displayed(self):
        orders_page = self.driver.find_element(*MainPageLocators.ORDERS_PAGE)
        return orders_page.is_displayed()
