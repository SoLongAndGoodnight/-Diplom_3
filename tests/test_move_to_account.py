import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(login_page.profile_button_locator()))
            login_page.go_to_profile()

        with allure.step("Проверяем, что кнопка 'Выйти' видна"):
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(account_page.exit_button_locator()))
            assert account_page.is_exit_button_visible(), "Кнопка 'Выйти' не найдена — пользователь не залогинился!"
