import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators, OrderListsLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestOrderNumberInAllTimeOrders:
    def test_order_number_in_all_time_orders(self, driver, unique_user):
        """Логин в аккаунт"""
        driver.get(f"{BASE_URL}/login")
        driver.implicitly_wait(4)

        driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(unique_user["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(unique_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        # идем в лист заказов и запоминаем количество заказов
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))

        # Кликаем на Лист заказов
        driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.ALL_TIME_READY_ORDERS))

        # запоминаем количество заказов
        today_ready_orders = driver.find_element(*OrderListsLocators.TODAY_READY_ORDERS).text

        #Идем в конструктор
        constructor = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
        constructor.click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.BUN))

        #перетаскивание булки
        bun = driver.find_element(*MainPageLocators.BUN)
        cart = driver.find_element(*MainPageLocators.CART)

        actions = ActionChains(driver)
        actions.drag_and_drop(bun, cart).perform()
        time.sleep(2)

        #Оформление заказа и проверка модальника "идентификатор заказа"
        button_order = driver.find_element(*MainPageLocators.BUTTON_COMPLETE_ORDER)

        button_order.click()
        time.sleep(2)

        # Ждём, пока текст обновится и станет не "9999"
        WebDriverWait(driver, 7).until(
            lambda d: driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text != "9999"
        )

        # Сохраняем ТЕКСТ из веб-элемента в переменную
        order_number = driver.find_element(*MainPageLocators.ORDER_NUMBER_FOR_SAVE).text

        # Принтим сам номер заказа, а не объект элемента
        print(f"Номер заказа: {order_number}")

        driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

        # Явное ожидание, чтобы элемент гарантированно был кликабельным
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LIST_FOR_ORDERS))

        # Кликаем на Лист заказов
        driver.find_element(*MainPageLocators.LIST_FOR_ORDERS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderListsLocators.TODAY_READY_ORDERS))

        # Сохраняем новое количество заказов после оформления
        new_today_ready_orders = driver.find_element(*OrderListsLocators.TODAY_READY_ORDERS).text

        # Принтим старое и новое количество
        print(f"Количество заказов ДО: {today_ready_orders}, ПОСЛЕ: {new_today_ready_orders}")

        # Ассерт — убеждаемся, что количество заказов увеличилось
        assert int(new_today_ready_orders) > int(today_ready_orders), "Количество заказов не увеличилось после оформления нового!"
