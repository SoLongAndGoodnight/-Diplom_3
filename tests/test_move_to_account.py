import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, AccountPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site/login"

class TestAccountLogin:
    @allure.title("Проверка перехода в личный аккаунт")
    def test_account_login(self, driver, unique_user):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        with allure.step("Получаем данные уникального пользователя из API фикстуры"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

        with allure.step("Находим элементы и выполняем логин"):
            driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(input_email)
            driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(input_password)
            driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        with allure.step("Ждём загрузку профиля и переходим в аккаунт"):
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.PROFILE_BUTTON))
            driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()

        with allure.step("Проверяем, что видна кнопка 'Выйти'"):
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountPageLocators.EXIT_BUTTON))
            exit_button = driver.find_element(*AccountPageLocators.EXIT_BUTTON)
            assert exit_button, "Кнопка выхода не найдена — пользователь не залогинился"
