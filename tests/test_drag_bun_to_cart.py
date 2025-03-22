from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import allure
from locators import MainPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestDragBunToCart:
    @allure.title("Проверка перетаскивания булочки в корзину")
    def test_drag_bun_to_cart(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        with allure.step("Находим булку и корзину"):
            bun = driver.find_element(*MainPageLocators.BUN)
            cart = driver.find_element(*MainPageLocators.CART)

        with allure.step("Проверяем количество булок до перетаскивания"):
            counter = driver.find_element(*MainPageLocators.BUN_COUNTER)
            assert counter.text == "0"

        with allure.step("Создаём действие — перетаскиваем булку в корзину"):
            actions = ActionChains(driver)
            actions.drag_and_drop(bun, cart).perform()
            time.sleep(2)

        with allure.step("Проверяем, что количество булок увеличилось"):
            WebDriverWait(driver, 5).until(lambda d: counter.text == "2")
            assert counter.text == "2", "Счетчик не увеличился до 2!"
