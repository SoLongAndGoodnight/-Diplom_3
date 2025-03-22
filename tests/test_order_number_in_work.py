import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators, OrderListsLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestOrderNumber:
    @allure.title("Проверка, что после заказа, его номер появляется в работе")
    def test_order_number_in_work(self, driver, unique_user):
        with allure.step("Логин в аккаунт"):
            driver.get(f"{BASE_URL}/login")
            driver.implicitly_wait(4)

            driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(unique_user["email"])
            driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(unique_user["password"])
            driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        with allure.step("перетаскивание булки"):
            time.sleep(2)
            bun = driver.find_element(*MainPageLocators.BUN)
            cart = driver.find_element(*MainPageLocators.CART)

            actions = ActionChains(driver)
            actions.drag_and_drop(bun, cart).perform()
            time.sleep(2)

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            button_order = driver.find_element(*MainPageLocators.BUTTON_COMPLETE_ORDER)

            button_order.click()
            time.sleep(2)

        with allure.step("Ждём, пока текст обновится и станет не '9999'"):
            WebDriverWait(driver, 7).until(
                lambda d: driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text != "9999"
            )

        with allure.step("Сохраняем текст из веб-элемента в переменную"):
            order_number = driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text

        with allure.step("Принтим номер заказа"):
            print(f"Номер заказа: {order_number}")

        with allure.step("Проверяем, что номер действительно появился и не равен 9999"):
            assert order_number.isnumeric(), "Номер заказа должен быть числом!"
            assert order_number != "9999", "Номер заказа не должен быть 9999!"

            driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

        with allure.step("Явное ожидание, чтобы элемент гарантированно был кликабельным"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))

        with allure.step("Кликаем на Лист заказов"):
            driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.IN_WORK))

        orders_in_work = driver.find_element(*OrderListsLocators.IN_WORK).text

        with allure.step("Проверяем, что наш номер заказа есть в этом списке"):
            assert order_number in orders_in_work, f"Номер заказа {order_number} не найден в списке 'В работе'!"
