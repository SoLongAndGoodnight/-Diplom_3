import time
import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.account_page import AccountPageObject
from pages.order_page import OrderPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = "https://stellarburgers.nomoreparties.site/api"


class TestOrder:
    @allure.title("Проверка того, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_from_order_history_visible_in_orders_line(self, driver, unique_user):
        driver.get(f"{BASE_URL}/login")
        driver.implicitly_wait(4)

        login_page_object = LoginPageObject(driver)
        main_page_object = MainPageObject(driver)
        account_page_object = AccountPageObject(driver)
        order_page_object = OrderPageObject(driver)

        with allure.step("Логин в аккаунт"):
            login_page_object.login(unique_user["email"], unique_user["password"])

        with allure.step("Проверка видимости веб элемента булочка"):
            main_page_object.check_bun_is_visible()

        with allure.step("Драг энд дроп булочки"):
            main_page_object.drag_and_drop_bun_to_cart()
            time.sleep(2)

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            main_page_object.complete_order()
            time.sleep(3)

        with allure.step("закрываем модальник, без time.sleep не работает"):
            main_page_object.close_modal()

        with allure.step("Идем в личный кабинет"):
            login_page_object.click_profile_button()

        with allure.step("Переходим в Историю заказов"):
            account_page_object.click_order_history()
            last_order_number = account_page_object.get_last_order_number()

            print(f"Номер последнего заказа: {last_order_number}")

        with allure.step("Переходим в ленту заказов"):
            order_page_object.go_to_orders_feed()

        with allure.step("Ожидаем появления заказа с нашим номером в ленте заказов"):
            order_page_object.wait_for_order_number_in_orders_line_is_visible(last_order_number)
