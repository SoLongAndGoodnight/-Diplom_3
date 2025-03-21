import time
import pytest
from locators import MainPageLocators, OrderListsLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"
def test_orders_list_modal_is_open(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    orders = driver.find_element(*MainPageLocators.ORDERS_BUTTON)
    orders.click()
    orders_page = driver.find_element(*MainPageLocators.ORDERS_PAGE)
    # Проверяем, что элемент 'Лента заказов' виден
    assert orders_page.is_displayed()

    #Клик на первый заказ в списке
    driver.find_element(*OrderListsLocators.FIRST_ORDER_IN_LIST).click()

    #Проверяем что модальное окно отображается
    modal_with_order_from_list = driver.find_element(*OrderListsLocators.MODAL_WITH_ORDER_FROM_LIST)
    assert modal_with_order_from_list.is_displayed()


