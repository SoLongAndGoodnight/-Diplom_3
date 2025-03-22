import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators, OrderListsLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestOrderNumberInAllTimeOrders:
    @allure.title("Проверка, что после заказа меняется счетик бургеров за все время")
    def test_order_number_in_all_time_orders_calculator(self, driver, unique_user):
        with allure.step("Логин в аккаунт"):
            driver.get(f"{BASE_URL}/login")
            driver.implicitly_wait(4)

            driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(unique_user["email"])
            driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(unique_user["password"])
            driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        with allure.step("идем в лист заказов и запоминаем количество заказов"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))

        with allure.step("кликаем на Лист заказов"):
            driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.ALL_TIME_READY_ORDERS))

        with allure.step("запоминаем количество заказов"):
            all_time_ready_orders = driver.find_element(*OrderListsLocators.ALL_TIME_READY_ORDERS).text

        with allure.step("идем в конструктор"):
            constructor = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
            constructor.click()

            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

        with allure.step("перетаскивание булки"):
            bun = driver.find_element(*MainPageLocators.BUN)
            cart = driver.find_element(*MainPageLocators.CART)

            actions = ActionChains(driver)
            actions.drag_and_drop(bun, cart).perform()

        with allure.step("оформление заказа и проверка модальника 'идентификатор заказа'"):
            button_order = driver.find_element(*MainPageLocators.BUTTON_COMPLETE_ORDER)

            button_order.click()
            time.sleep(2)


        with allure.step("ждём, пока текст обновится и станет не 9999 - это без time.sleep(2) не работает"):
            WebDriverWait(driver, 7).until(
                lambda d: driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text != "9999"
            )

        with allure.step("сохраняем текст из веб-элемента в переменную"):
            order_number = driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text

        print(f"Номер заказа: {order_number}")

        with allure.step("закрываем модальник"):
            driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

        with allure.step("явное ожидание, чтобы элемент гарантированно был кликабельным"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))

        with allure.step("кликаем на Лист заказов"):
            driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.ALL_TIME_READY_ORDERS))

        with allure.step("сохраняем новое количество заказов после оформления"):
            new_all_time_ready_orders = driver.find_element(*OrderListsLocators.ALL_TIME_READY_ORDERS).text

        with allure.step("принтим старое и новое количество для отладки"):
            print(f"Количество заказов ДО: {all_time_ready_orders}, ПОСЛЕ: {new_all_time_ready_orders}")

        with allure.step("ассерт — убеждаемся, что количество заказов увеличилось"):
            assert int(new_all_time_ready_orders) > int(all_time_ready_orders), "Количество заказов не увеличилось после оформления нового!"

