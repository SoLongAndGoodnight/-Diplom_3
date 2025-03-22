import time
import allure
from locators import LoginPageLocators, AccountPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/login"

class TestAccountGoToHistory:
    @allure.title("Проверка, что пользователь может зайти в историю заказов")
    def test_account_go_to_history(self, driver, unique_user):
        with allure.step("Авторизация пользователя"):
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
            time.sleep(4)
            driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()
            time.sleep(3)

            driver.find_element(*AccountPageLocators.ORDER_HISTORY).click()

        with allure.step("Проверяем, что ссылка стала активной (появился нужный класс)"):
            active_link = driver.find_element(*AccountPageLocators.ACTIVE_ORDER_HISTORY)
            assert active_link
