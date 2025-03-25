import allure
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from urls import LOGIN_URL


class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    def test_create_order(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Логин в аккаунт"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("перетаскивание булки"):
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            assert main_page_object.complete_order_and_check_modal()
