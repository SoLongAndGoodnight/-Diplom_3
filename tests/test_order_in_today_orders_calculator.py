import time
import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.order_page import OrderPageObject
from urls import LOGIN_URL


class TestOrderNumberInTodayOrders:
    @allure.title("Проверка, что после заказа меняется счетик бургеров за сегодня")
    def test_order_number_in_all_time_orders(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        order_page_object = OrderPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Логин в аккаунт"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("Кликаем на Лист заказов"):
            order_page_object.go_to_orders_feed()

        with allure.step("запоминаем количество заказов"):
            today_ready_orders = order_page_object.get_today_ready_orders()

        with allure.step("Идем в конструктор"):
            main_page_object.go_to_constructor()

        main_page_object.wait_for_bun()

        with allure.step("перетаскивание булки"):
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            main_page_object.complete_order()

        # NOTE: костыль для предотвращения получения ошибки ElementClickInterceptedException
        time.sleep(3)

        with allure.step("Ждём, пока текст обновится и станет не '9999'"):
            main_page_object.wait_for_order_number_updated()

        with allure.step("Сохраняем ТЕКСТ из веб-элемента в переменную"):
            main_page_object.get_order_number()

        main_page_object.close_modal()

        with allure.step("Кликаем на Лист заказов"):
            order_page_object.go_to_orders_feed()

        with allure.step("Сохраняем новое количество заказов после оформления"):
            new_today_ready_orders = order_page_object.get_today_ready_orders()

        with allure.step("Убеждаемся, что количество заказов увеличилось"):
            assert int(new_today_ready_orders) > int(today_ready_orders), "Количество заказов не увеличилось после оформления нового!"
