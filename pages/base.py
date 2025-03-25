from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_locator(self, locator: tuple[ByType, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def wait_until_element_visible(self, locator: tuple[ByType, str], timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_element_invisible(self, locator: tuple[ByType, str], timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_until_element_text_changed(self, locator: tuple[ByType, str], text: str, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(text_to_be_changed_in_element(locator, text))

    def wait_until_element_to_be_clickable(self, locator: tuple[ByType, str], timeout: int = 4):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_visible_element_by_locator(self, locator: tuple[ByType, str], timeout: int = 3) -> WebElement:
        self.wait_until_element_visible(locator, timeout=timeout)
        return self.find_element_by_locator(locator)

    def find_clickable_element_by_locator(self, locator: tuple[ByType, str], timeout: int = 3) -> WebElement:
        self.wait_until_element_to_be_clickable(locator, timeout=timeout)
        return self.find_element_by_locator(locator)

    def drag_and_drop(self, source_locator: tuple[ByType, str], target_locator: tuple[ByType, str]):
        source_element = self.find_visible_element_by_locator(source_locator)
        target_element = self.find_visible_element_by_locator(target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()


def text_to_be_changed_in_element(locator, text_, treat_blank_as_not_changed=True):
    def _predicate(driver):
        element = driver.find_element(*locator)
        element_text = element.text

        if treat_blank_as_not_changed and element_text == "":
            return False
        else:
            return text_ != element_text

    return _predicate
