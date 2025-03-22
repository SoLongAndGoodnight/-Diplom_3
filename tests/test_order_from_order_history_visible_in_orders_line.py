import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators, AccountPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = "https://stellarburgers.nomoreparties.site/api"


class TestOrder:
    @allure.title("Проверка того, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_from_order_history_visible_in_orders_line(self, driver, unique_user):
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
            time.sleep(3)

        with allure.step("закрываем модальник, без time.sleep не работает"):
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BUTTON))
            driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

        with allure.step("Идем в личный кабинет"):
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.PROFILE_BUTTON))
            driver.find_element(*LoginPageLocators.PROFILE_BUTTON).click()

        with allure.step("Переходим в Историю заказов"):
            driver.find_element(*AccountPageLocators.ORDER_HISTORY).click()

            last_order_number = driver.find_element(*AccountPageLocators.LAST_ORDER_NUMBER).text
            print(f"Номер последнего заказа: {last_order_number}")

        with allure.step("Переходим в ленту заказов"):
            driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

        with allure.step("Ожидаем появления заказа с нашим номером в ленте заказов"):
            order_locator = (By.XPATH, f'//ul/li/a/div[1]/p[contains(text(), "{last_order_number}")]')

            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(order_locator)
            )

        with allure.step("Проверяем, что заказ с нужным номером действительно появился в списке"):
            assert driver.find_element(
                *order_locator).is_displayed(), f"Заказ с номером {last_order_number} не найден в ленте заказов!"
