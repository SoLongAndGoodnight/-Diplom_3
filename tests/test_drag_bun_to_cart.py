from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
from locators import MainPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_drag_bun_to_cart(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(4)

    # Находим булку и корзину
    bun = driver.find_element(*MainPageLocators.BUN)
    cart = driver.find_element(*MainPageLocators.CART)

    # Проверяем количество булок до перетаскивания
    counter = driver.find_element(*MainPageLocators.BUN_COUNTER)
    assert counter.text == "0"

    # Создаём действие — перетаскиваем булку в корзину
    actions = ActionChains(driver)
    actions.drag_and_drop(bun, cart).perform()
    time.sleep(2)

    # Проверяем, что количество булок увеличилось
    WebDriverWait(driver, 5).until(lambda d: counter.text == "2")
    assert counter.text == "2", "Счетчик не увеличился до 2!"
