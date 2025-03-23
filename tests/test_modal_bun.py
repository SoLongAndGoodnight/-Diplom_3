import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPageObject

BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestModalBun:
    @allure.title("Проверка отображения модальника ингридиента 'Bun'")
    def test_modal_bun(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        main_page = MainPageObject(driver)

        with allure.step("Кликаем на ингредиент"):
            main_page.click_bun()
            assert main_page.is_modal_open(), "Модальное окно булки не открылось!"

        with allure.step("Закрываем модальное окно через крестик"):
            main_page.close_modal()
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(main_page.modal_wrapper_locator()))
            assert main_page.is_modal_closed(), "Модальное окно булки не закрылось!"
