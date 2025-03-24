from locators import MainPageLocators
from .base import BasePageObject


class MainPageObject(BasePageObject):
    def wait_for_bun(self):
        self.find_visible_element_by_locator(MainPageLocators.BUN)

    def drag_and_drop_bun_to_cart(self):
        self.drag_and_drop(source_locator=MainPageLocators.BUN, target_locator=MainPageLocators.CART)

    def complete_order(self):
        element = self.find_element_by_locator(MainPageLocators.BUTTON_COMPLETE_ORDER)
        element.click()

    def complete_order_and_check_modal(self):
        self.complete_order()

        modal_order_complete = self.find_visible_element_by_locator(MainPageLocators.MODAL_ORDER_NUMBER)
        return modal_order_complete.is_displayed()

    def get_bun_counter(self):
        return self.find_visible_element_by_locator(MainPageLocators.BUN_COUNTER).text

    def click_bun(self):
        element = self.find_visible_element_by_locator(MainPageLocators.BUN)
        element.click()

    def is_modal_open(self):
        return self.find_visible_element_by_locator(MainPageLocators.MODAL_BUN).is_displayed()

    def close_modal(self):
        self.wait_until_element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        element = self.find_visible_element_by_locator(MainPageLocators.CLOSE_MODAL_BUTTON)
        element.click()

    def is_modal_closed(self):
        self.wait_until_element_invisible(MainPageLocators.MODAL_WRAPPER)

        element = self.find_element_by_locator(MainPageLocators.MODAL_WRAPPER)
        return not element.is_displayed()

    def check_bun_is_visible(self):
        self.find_visible_element_by_locator(MainPageLocators.BUN)

    def go_to_constructor(self):
        self.find_visible_element_by_locator(MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def wait_for_order_number_updated(self):
        self.wait_until_element_text_changed(MainPageLocators.ORDER_NUMBER_FOR_SAVE, "9999", timeout=7)

    def get_order_number(self):
        return self.find_visible_element_by_locator(MainPageLocators.ORDER_NUMBER_FOR_SAVE).text

    def click_orders_button(self):
        element = self.find_visible_element_by_locator(MainPageLocators.ORDERS_BUTTON)
        element.click()

    def order_page_is_displayed(self):
        orders_page = self.find_visible_element_by_locator(MainPageLocators.ORDERS_PAGE)
        return orders_page.is_displayed()

    def constructor_page_is_displayed(self):
        constructor_page = self.find_visible_element_by_locator(MainPageLocators.CONSTRUCTOR_PAGE)
        assert constructor_page.is_displayed()
