from locators import MainPageLocators
import allure

BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestSwipeConstructorAndOrdersPage:
    @allure.title("Проверка перехода по разделам 'Конструктор бургеров' и 'Лента заказов'")
    def test_constructor_and_orders_swipe(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        with allure.step("Ищем кнопку 'Лента заказов'"):
            orders = driver.find_element(*MainPageLocators.ORDERS_BUTTON)
            orders.click()
        orders_page = driver.find_element(*MainPageLocators.ORDERS_PAGE)
        with allure.step("Проверяем, что элемент 'Лента заказов' виден"):
            assert orders_page.is_displayed()

        with allure.step("Ищем кнопку 'Конструктор бургеров'"):
            constructor = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
            constructor.click()
            constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)

        with allure.step("Проверяем, что элемент 'Конструктор заказов' виден"):
            assert constructor_page.is_displayed()
