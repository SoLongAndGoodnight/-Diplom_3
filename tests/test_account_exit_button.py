import time
import allure
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site/login"


class TestAccountLogin:
    @allure.title("Проверка, что можно войти и выйти из аккаунта")
    def test_account_login(self, driver, unique_user):
        with allure.step("Открываем страницу логина"):
            driver.get(BASE_URL)
            driver.implicitly_wait(4)

        login_page_object = LoginPageObject(driver)
        account_page_object = AccountPageObject(driver)

        with allure.step("Получаем данные уникального пользователя из API фикстуры"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

        with allure.step("Находим элементы и выполняем логин"):
            login_page_object.fill_login_field(input_email)
            login_page_object.fill_password_field(input_password)
            login_page_object.click_submit_button()

        with allure.step("Ждём загрузку профиля и переходим в аккаунт"):
            time.sleep(4)
            login_page_object.click_profile_button()
            time.sleep(3)

        with allure.step("Находим кнопку выхода и кликаем"):
            account_page_object.click_exit_button()

        with allure.step("Проверяем, что видна кнопка 'Войти'"):
            assert login_page_object.check_submit_button_visible()
