import time
import allure
from locators import LoginPageLocators, AccountPageLocators
from pages.login_page import LoginPageObject
from pages.account_page import AccountPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site/login"


class TestAccountGoToHistory:
    @allure.title("Проверка, что пользователь может зайти в историю заказов")
    def test_account_go_to_history(self, driver, unique_user):
        with allure.step("Авторизация пользователя"):
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

            account_page_object.click_order_history()

        with allure.step("Проверяем, что ссылка стала активной (появился нужный класс)"):
            account_page_object.active_link()
