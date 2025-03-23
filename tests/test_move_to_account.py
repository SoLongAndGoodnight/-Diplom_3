import allure
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site/login"


class TestAccountLogin:
    @allure.title("Проверка перехода в личный аккаунт")
    def test_account_login(self, driver, unique_user):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        login_page = LoginPageObject(driver)
        account_page = AccountPageObject(driver)

        with allure.step("Получаем данные уникального пользователя из API фикстуры"):
            email = unique_user["email"]
            password = unique_user["password"]

        with allure.step("Заполняем форму и выполняем вход"):
            login_page.login(email, password)

        with allure.step("Переходим в профиль"):
            login_page.go_to_profile()

        with allure.step("Проверяем, что кнопка 'Выйти' видна"):
            assert account_page.exit_button_displayed(), "Кнопка 'Выйти' не найдена — пользователь не залогинился!"
