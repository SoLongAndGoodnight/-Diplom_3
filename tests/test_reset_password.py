import allure
from pages.login_page import LoginPageObject
from pages.restore_password_page import RestorePasswordPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site/login"


class TestResetPassword:
    @allure.title("Проверка функционала для смены пароля")
    def test_reset_password(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(3)

        login_page_object = LoginPageObject(driver)
        restore_password_page_object = RestorePasswordPageObject(driver)

        login_page_object.click_restore_password()

        with allure.step("Проверяем, что перешли на страницу 'Забыл пароль'"):
            assert "forgot-password" in driver.current_url

        with allure.step("Ввод почты"):
            restore_password_page_object.restore_password_for_email("lizakorotkova17123@yandex.ru")

        with allure.step("проверяем, что перешли на страницу восстановления пароля"):
            assert "forgot-password" in driver.current_url

        restore_password_page_object.click_on_eye()

        with allure.step("Дополнительный ассерт: убедимся, что поле реально доступно для ввода"):
            assert login_page_object.email_field_displayed_and_enabled()
