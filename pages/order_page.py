from selenium.webdriver.common.by import By
from locators import MainPageLocators, OrderListsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPageObject:
    def __init__(self, driver):
        self.driver = driver

    def go_to_orders_line(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))
        self.driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

    def is_order_in_feed(self, order_number):
        order_locator = (By.XPATH, f'//ul/li/a/div[1]/p[contains(text(), "{order_number}")]')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(order_locator))
        return self.driver.find_element(*order_locator).is_displayed()

    def wait_for_order_number_in_orders_line_is_visible(self, last_order_number):
        order_locator = (By.XPATH, f'//ul/li/a/div[1]/p[contains(text(), "{last_order_number}")]')

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(order_locator)
        )

        self.driver.find_element(*order_locator).is_displayed()

    def get_all_time_ready_orders_count(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.ALL_TIME_READY_ORDERS))
        return self.driver.find_element(*OrderListsLocators.ALL_TIME_READY_ORDERS).text

    def get_today_ready_orders(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.TODAY_READY_ORDERS))
        return self.driver.find_element(*OrderListsLocators.TODAY_READY_ORDERS).text
