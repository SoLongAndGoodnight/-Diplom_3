import allure

from pages.main_page import MainPageObject
from pages.order_page import OrderPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestOrdersModalIsOpen:
    @allure.title("Проверка, что по клику на заказ, отображается модальное окно")
    def test_orders_list_modal_is_open(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(5)

        main_page_object = MainPageObject(driver)
        order_page_object = OrderPageObject(driver)

        main_page_object.click_orders_button()

        with allure.step("Проверяем, что элемент 'Лента заказов' виден"):
            assert main_page_object.order_page_is_displayed()

        with allure.step("Клик на первый заказ в списке"):
            order_page_object.click_first_order_in_feed()

        with allure.step("Проверяем что модальное окно отображается"):
            assert order_page_object.modal_with_order_from_list_displayed()
