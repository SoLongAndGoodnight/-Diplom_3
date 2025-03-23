from selenium.webdriver.support.ui import WebDriverWait
import allure
from pages.main_page import MainPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestDragBunToCart:
    @allure.title("Проверка перетаскивания булочки в корзину")
    def test_drag_bun_to_cart(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        main_page = MainPageObject(driver)

        with allure.step("Проверяем, что счетчик булок равен 0"):
            assert main_page.get_bun_counter() == "0", "Счетчик булок не равен 0 при старте!"

        with allure.step("Перетаскиваем булку в корзину"):
            main_page.drag_and_drop_bun_to_cart()

        with allure.step("Проверяем, что счетчик булок увеличился до 2"):
            WebDriverWait(driver, 5).until(lambda d: main_page.get_bun_counter() == "2")
            assert main_page.get_bun_counter() == "2", "Счетчик не увеличился до 2!"
