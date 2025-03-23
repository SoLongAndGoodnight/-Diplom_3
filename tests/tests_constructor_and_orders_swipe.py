from locators import MainPageLocators
import allure

from pages.main_page import MainPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestSwipeConstructorAndOrdersPage:
    @allure.title("Проверка перехода по разделам 'Конструктор бургеров' и 'Лента заказов'")
    def test_constructor_and_orders_swipe(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        main_page_object = MainPageObject(driver)

        with allure.step("Ищем кнопку 'Лента заказов'"):
            main_page_object.click_orders_button()

        with allure.step("Проверяем, что элемент 'Лента заказов' виден"):
            assert main_page_object.order_page_is_displayed()

        with allure.step("Ищем кнопку 'Конструктор бургеров'"):
            main_page_object.go_to_constructor()

        with allure.step("Проверяем, что элемент 'Конструктор заказов' виден"):
            main_page_object.constructor_page_is_displayed()
