import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.order_page import OrderPageObject
from urls import LOGIN_URL


class TestOrderNumberInAllTimeOrders:
    @allure.title("Проверка, что после заказа меняется счетик бургеров за все время")
    def test_order_number_in_all_time_orders_calculator(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        order_page_object = OrderPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Логин в аккаунт"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("идем в лист заказов и запоминаем количество заказов"):
            main_page_object.go_to_orders_feed()
            all_time_ready_orders = order_page_object.get_all_time_ready_orders_count()

        with allure.step("идем в конструктор"):
            main_page_object.go_to_constructor()
            main_page_object.wait_for_bun()

        with allure.step("перетаскивание булки"):
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("оформление заказа и проверка модальника 'идентификатор заказа'"):
            main_page_object.complete_order()

        with allure.step("ждём, пока текст обновится и станет не 9999"):
            main_page_object.wait_for_order_number_updated()

        with allure.step("сохраняем текст из веб-элемента в переменную"):
            main_page_object.get_order_number()

        with allure.step("закрываем модальник"):
            main_page_object.close_modal()

        with allure.step("явное ожидание, чтобы элемент гарантированно был кликабельным"):
            main_page_object.go_to_orders_feed()

        with allure.step("сохраняем новое количество заказов после оформления"):
            new_all_time_ready_orders = order_page_object.get_all_time_ready_orders_count()

        with allure.step("ассерт — убеждаемся, что количество заказов увеличилось"):
            assert int(new_all_time_ready_orders) > int(all_time_ready_orders), "Количество заказов не увеличилось после оформления нового!"
