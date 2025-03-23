import time
import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.order_page import OrderPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestOrderNumber:
    @allure.title("Проверка, что после заказа, его номер появляется в работе")
    def test_order_number_in_work(self, driver, unique_user):
        driver.get(f"{BASE_URL}/login")
        driver.implicitly_wait(4)

        login_page_object = LoginPageObject(driver)
        order_page_object = OrderPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Логин в аккаунт"):
            login_page_object.login(unique_user["email"], unique_user["password"])

        with allure.step("перетаскивание булки"):
            time.sleep(2)
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            main_page_object.complete_order()
            time.sleep(2)

        with allure.step("Ждём, пока текст обновится и станет не '9999'"):
            main_page_object.wait_for_order_number_updated()

        with allure.step("Сохраняем текст из веб-элемента в переменную"):
            order_number = main_page_object.get_order_number()

        with allure.step("Принтим номер заказа"):
            print(f"Номер заказа: {order_number}")

        with allure.step("Проверяем, что номер действительно появился и не равен 9999"):
            assert order_number.isnumeric(), "Номер заказа должен быть числом!"
            assert order_number != "9999", "Номер заказа не должен быть 9999!"

            main_page_object.close_modal()

        with allure.step("Кликаем на Лист заказов"):
            order_page_object.go_to_orders_feed()

        orders_in_work = order_page_object.get_orders_in_work()

        with allure.step("Проверяем, что наш номер заказа есть в этом списке"):
            assert order_number in orders_in_work, f"Номер заказа {order_number} не найден в списке 'В работе'!"
