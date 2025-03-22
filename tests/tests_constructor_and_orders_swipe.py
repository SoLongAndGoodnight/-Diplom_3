from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_constructor_and_orders_swipe(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(4)

    orders = driver.find_element(*MainPageLocators.ORDERS_BUTTON)
    orders.click()
    orders_page = driver.find_element(*MainPageLocators.ORDERS_PAGE)
    # Проверяем, что элемент 'Лента заказов' виден
    assert orders_page.is_displayed()

    constructor = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
    constructor.click()
    constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)

    # Проверяем, что элемент 'Конструктор заказов' виден
    assert constructor_page.is_displayed()
