from locators import MainPageLocators, OrderListsLocators
from .base import BasePageObject


class OrderPageObject(BasePageObject):
    def go_to_orders_feed(self):
        self.find_visible_element_by_locator(MainPageLocators.LIST_FOR_ORDERS, timeout=10).click()

    def is_order_in_feed(self, order_number):
        return self.find_visible_element_by_locator(
            OrderListsLocators.get_order_number_locator(order_number), timeout=5
        ).is_displayed()

    def wait_for_order_number_in_orders_line_is_visible(self, last_order_number):
        self.find_visible_element_by_locator(
            OrderListsLocators.get_last_order_number_locator(last_order_number), timeout=5
        ).is_displayed()

    def get_all_time_ready_orders_count(self):
        return self.find_visible_element_by_locator(OrderListsLocators.ALL_TIME_READY_ORDERS, timeout=5).text

    def get_today_ready_orders(self):
        return self.find_visible_element_by_locator(OrderListsLocators.TODAY_READY_ORDERS).text

    def get_orders_in_work(self):
        return self.find_visible_element_by_locator(OrderListsLocators.IN_WORK).text

    def click_first_order_in_feed(self):
        return self.find_visible_element_by_locator(OrderListsLocators.FIRST_ORDER_IN_LIST).click()

    def modal_with_order_from_list_displayed(self):
        modal_with_order_from_list = self.find_element_by_locator(OrderListsLocators.MODAL_WITH_ORDER_FROM_LIST)
        return modal_with_order_from_list.is_displayed()
