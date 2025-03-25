import allure
from pages.main_page import MainPageObject
from urls import BASE_URL


class TestDragBunToCart:
    @allure.title("Проверка перетаскивания булочки в корзину")
    def test_drag_bun_to_cart(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageObject(driver)

        with allure.step("Проверяем, что счетчик булок равен 0"):
            assert main_page.get_bun_counter() == "0", "Счетчик булок не равен 0 при старте!"

        with allure.step("Перетаскиваем булку в корзину"):
            main_page.drag_and_drop_bun_to_cart()

        with allure.step("Проверяем, что счетчик булок увеличился до 2"):
            assert main_page.get_bun_counter() == "2", "Счетчик не увеличился до 2!"
