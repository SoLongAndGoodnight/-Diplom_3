from locators import MainPageLocators, OrderListsLocators
import allure


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestOrdersModalIsOpen:
    @allure.title("Проверка, что по клику на заказ, отображается модальное окно")
    def test_orders_list_modal_is_open(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(5)

        orders = driver.find_element(*MainPageLocators.ORDERS_BUTTON)
        orders.click()
        orders_page = driver.find_element(*MainPageLocators.ORDERS_PAGE)
        with allure.step("Проверяем, что элемент 'Лента заказов' виден"):
            assert orders_page.is_displayed()

        with allure.step("Клик на первый заказ в списке"):
            driver.find_element(*OrderListsLocators.FIRST_ORDER_IN_LIST).click()

        with allure.step("Проверяем что модальное окно отображается"):
            modal_with_order_from_list = driver.find_element(*OrderListsLocators.MODAL_WITH_ORDER_FROM_LIST)
            assert modal_with_order_from_list.is_displayed()
