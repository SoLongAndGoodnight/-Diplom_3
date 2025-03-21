import time
import pytest
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = "https://stellarburgers.nomoreparties.site/api"


class TestCreateOrder:
    def test_create_order(self, driver, unique_user):
        """Логин в аккаунт"""
        driver.get(f"{BASE_URL}/login")
        driver.implicitly_wait(4)

        driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(unique_user["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(unique_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        #перетаскивание булки
        bun = driver.find_element(*MainPageLocators.BUN)
        cart = driver.find_element(*MainPageLocators.CART)
        counter = driver.find_element(*MainPageLocators.BUN_COUNTER)
        #assert counter.text == "0"

        actions = ActionChains(driver)
        actions.drag_and_drop(bun, cart).perform()
        time.sleep(2)

        #Оформление заказа и проверка модальника "идентификатор заказа"
        button_order = driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]')

        button_order.click()
        time.sleep(4)

        modal_order_complete = driver.find_element(*MainPageLocators.MODAL_ORDER_NUMBER)
        assert modal_order_complete.is_displayed()

        # # Ждём появления модального окна с номером заказа
        # WebDriverWait(driver, 5).until(
        #     EC.visibility_of_element_located((By.XPATH, '//section//div[1]/div/h2'))
        # )
        #
        # # Находим номер заказа
        # order_number = driver.find_element(By.XPATH, '//section//div[1]/div/h2').text
        # print(f"Полученный номер заказа: {order_number}")
        #
        # # Проверяем, что номер состоит только из цифр
        # assert order_number.isnumeric(), "Номер заказа не появился или неверный!"
        #
        # # Проверяем статус заказа по API
        # headers = {"Authorization": f"Bearer {unique_user['token']}"}
        # response = requests.get(f"{API_URL}/orders", headers=headers)
        # assert response.status_code == 200, "Не удалось получить статус заказа"
        # assert response.json()["orders"][0]["status"] == "in work", "Заказ не в статусе 'В работе'"