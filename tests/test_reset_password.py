import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import LoginPageLocators
from locators import ResetPasswordLokators


BASE_URL = "https://stellarburgers.nomoreparties.site/login"

def test_reset_password(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    driver.find_element(*LoginPageLocators.RESTORE_PASSWORD_LINK).click()
    driver.find_element(*ResetPasswordLokators.INPUT_EMAIL).send_keys("lizakorotkova17123@yandex.ru")
    driver.find_element(*ResetPasswordLokators.RESET_BUTTON).click()
    driver.find_element(*ResetPasswordLokators.EYE_SVG).click()



