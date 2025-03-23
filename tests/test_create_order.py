import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    def test_create_order(self, driver, unique_user):
        driver.get(f"{BASE_URL}/login")
        driver.implicitly_wait(4)

        login_page_object = LoginPageObject(driver)
        main_page_object = MainPageObject(driver)

        with allure.step("Получаем данные уникального пользователя из API фикстуры"):
            input_email = unique_user["email"]
            input_password = unique_user["password"]

        with allure.step("Логин в аккаунт"):
            login_page_object.fill_login_field(input_email)
            login_page_object.fill_password_field(input_password)
            login_page_object.click_submit_button()

            main_page_object.waiting_element_bun()

        with allure.step("перетаскивание булки"):
            main_page_object.drag_and_drop_bun_to_cart()

        with allure.step("Оформление заказа и проверка модальника 'идентификатор заказа'"):
            assert main_page_object.complete_order_and_check_modal()
