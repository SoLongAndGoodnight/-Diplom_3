from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_modal_bun(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(4)

    bun = driver.find_element(*MainPageLocators.BUN)
    bun.click()
    modal_bun = driver.find_element(*MainPageLocators.MODAL_BUN)
    # Проверяем, что элемент виден
    assert modal_bun.is_displayed()

    modal_close_button = driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON)
    modal_close_button.click()

    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(MainPageLocators.MODAL_WRAPPER))

    # Проверяем, что элемент теперь не виден
    assert not driver.find_element(*MainPageLocators.MODAL_WRAPPER).is_displayed()


