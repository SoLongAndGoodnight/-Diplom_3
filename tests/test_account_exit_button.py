import allure
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject
from urls import LOGIN_URL


class TestAccountLogin:
    @allure.title("Проверка, что можно войти и выйти из аккаунта")
    def test_account_login(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        account_page_object = AccountPageObject(driver)

        with allure.step("Находим элементы и выполняем логин"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("Ждём загрузку профиля и переходим в аккаунт"):
            login_page_object.click_profile_button()

        with allure.step("Находим кнопку выхода и кликаем"):
            account_page_object.click_exit_button()

        with allure.step("Проверяем, что видна кнопка 'Войти'"):
            assert login_page_object.check_submit_button_visible()
