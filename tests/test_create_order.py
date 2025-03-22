import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    def test_create_order(self, driver, unique_user):
        with allure.step("Логин в аккаунт"):
            driver.get(f"{BASE_URL}/login")
            driver.implicitly_wait(4)

            driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(unique_user["email"])
            driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(unique_user["password"])
            driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

        with allure.step("перетаскивание булки"):
            bun = driver.find_element(*MainPageLocators.BUN)
            cart = driver.find_element(*MainPageLocators.CART)

            actions = ActionChains(driver)
            actions.drag_and_drop(bun, cart).perform()
            time.sleep(2)

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            button_order = driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]')

            button_order.click()

            modal_order_complete = driver.find_element(*MainPageLocators.MODAL_ORDER_NUMBER)
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.MODAL_ORDER_NUMBER))

            assert modal_order_complete.is_displayed()
