import allure
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject
from urls import LOGIN_URL


class TestAccountGoToHistory:
    @allure.title("Проверка, что пользователь может зайти в историю заказов")
    def test_account_go_to_history(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        account_page_object = AccountPageObject(driver)

        with allure.step("Находим элементы и выполняем логин"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("Ждём загрузку профиля и переходим в аккаунт"):
            login_page_object.click_profile_button()

            account_page_object.click_order_history()

        with allure.step("Проверяем, что ссылка стала активной (появился нужный класс)"):
            assert account_page_object.active_link_displayed()
