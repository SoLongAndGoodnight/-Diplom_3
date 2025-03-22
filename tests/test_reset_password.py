import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, ResetPasswordLokators


BASE_URL = "https://stellarburgers.nomoreparties.site/login"

class TestResetPassword:
    @allure.title("Проверка функционала для смены пароля")
    def test_reset_password(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(3)

        driver.find_element(*LoginPageLocators.RESTORE_PASSWORD_LINK).click()
        with allure.step("Проверяем, что перешли на страницу 'Забыл пароль'"):
            assert "forgot-password" in driver.current_url

        with allure.step("Ввод почты"):
            driver.find_element(*ResetPasswordLokators.INPUT_EMAIL).send_keys("lizakorotkova17123@yandex.ru")
            driver.find_element(*ResetPasswordLokators.RESET_BUTTON).click()

        with allure.step("проверяем, что перешли на страницу восстановления пароля"):
            assert "forgot-password" in driver.current_url

        driver.find_element(*ResetPasswordLokators.EYE_SVG).click()

        with allure.step("Ждём, пока поле пароля станет активным (подсветится)"):
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(LoginPageLocators.ACTIVE_EMAIL_FIELD))

        with allure.step("Дополнительный ассерт: убедимся, что поле реально доступно для ввода"):
            password_input = driver.find_element(*LoginPageLocators.ACTIVE_EMAIL_FIELD)
            assert password_input.is_displayed() and password_input.is_enabled()
