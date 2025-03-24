import time
import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.order_page import OrderPageObject
from urls import LOGIN_URL


class TestOrderNumber:
    @allure.title("Проверка, что после заказа, его номер появляется в работе")
    def test_order_number_in_work(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        order_page_object = OrderPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Логин в аккаунт"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("перетаскивание булки"):
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            main_page_object.complete_order()

        # NOTE: костыль для предотвращения получения ошибки ElementClickInterceptedException
        time.sleep(3)

        with allure.step("Ждём, пока текст обновится и станет не '9999'"):
            main_page_object.wait_for_order_number_updated()

        with allure.step("Сохраняем текст из веб-элемента в переменную"):
            order_number = main_page_object.get_order_number()

        with allure.step("Проверяем, что номер действительно появился и не равен 9999"):
            assert order_number.isnumeric(), "Номер заказа должен быть числом!"
            assert order_number != "9999", "Номер заказа не должен быть 9999!"

            main_page_object.close_modal()

        with allure.step("Кликаем на Лист заказов"):
            order_page_object.go_to_orders_feed()

        orders_in_work = order_page_object.get_orders_in_work()

        with allure.step("Проверяем, что наш номер заказа есть в этом списке"):
            assert order_number in orders_in_work, f"Номер заказа {order_number} не найден в списке 'В работе'!"
