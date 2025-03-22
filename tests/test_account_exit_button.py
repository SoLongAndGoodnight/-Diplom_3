import time
from locators import LoginPageLocators, AccountPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/login"

def test_account_login(driver, unique_user):
    driver.get(BASE_URL)
    driver.implicitly_wait(4)

    # Получаем данные уникального пользователя из API фикстуры
    input_email = unique_user["email"]
    input_password = unique_user["password"]

    # Находим элементы и выполняем логин
    driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(input_email)
    driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(input_password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    # Ждём загрузку профиля и переходим в аккаунт
    time.sleep(4)
    driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()
    time.sleep(3)

    # Находим кнопку выхода и кликаем
    exit_button = driver.find_element(*AccountPageLocators.EXIT_BUTTON)
    exit_button.click()

    # Проверяем, что видна кнопка "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    assert submit_button.is_displayed()