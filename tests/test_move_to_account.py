import allure
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject
from urls import LOGIN_URL


class TestAccountLogin:
    @allure.title("Проверка перехода в личный аккаунт")
    def test_account_login(self, driver, unique_user):
        driver.get(LOGIN_URL)

        login_page_object = LoginPageObject(driver)
        account_page = AccountPageObject(driver)

        with allure.step("Заполняем форму и выполняем вход"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

            login_page_object.login(input_email, input_password)

        with allure.step("Переходим в профиль"):
            login_page_object.go_to_profile()

        with allure.step("Проверяем, что кнопка 'Выйти' видна"):
            assert account_page.exit_button_displayed(), "Кнопка 'Выйти' не найдена — пользователь не залогинился!"
