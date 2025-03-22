from locators import MainPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestModalBun:
    @allure.title("Проверка отображения модальника ингридиента 'Bun'")
    def test_modal_bun(self, driver):
        driver.get(BASE_URL)
        driver.implicitly_wait(4)

        with allure.step("Кликаем на ингридиент"):
            bun = driver.find_element(*MainPageLocators.BUN)
            bun.click()
            modal_bun = driver.find_element(*MainPageLocators.MODAL_BUN)
        with allure.step("Проверяем, что элемент виден"):
            assert modal_bun.is_displayed()

        with allure.step("Ищем крестик и закрываем"):
            modal_close_button = driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON)
            modal_close_button.click()

            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(MainPageLocators.MODAL_WRAPPER))

        with allure.step("Проверяем, что элемент теперь не виден"):
            assert not driver.find_element(*MainPageLocators.MODAL_WRAPPER).is_displayed()

