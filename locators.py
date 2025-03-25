from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")
    ACTIVE_EMAIL_FIELD = (By.XPATH, '//label[contains(@class, "input__placeholder-focused")]')


class ResetPasswordLocators:
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    EYE_SVG = (By.CSS_SELECTOR, 'form fieldset:nth-of-type(1) .input__icon svg')


class AccountPageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY = (By.XPATH, '//li[@class="Account_listItem__35dAP"]/a[contains(text(), "История заказов")]')
    ACTIVE_ORDER_HISTORY = (By.XPATH, '//a[contains(@class, "Account_link_active__2opc9")]')
    LAST_ORDER_NUMBER = (By.XPATH, '//ul/li[last()]/a/div[1]/p[contains(@class, "text text_type_digits-default")]')


class MainPageLocators:
    BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    MODAL_BUN = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close")]')
    MODAL_WRAPPER = (By.XPATH, '//div[contains(@class, "undefined mb-4")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    ORDERS_BUTTON = (By.XPATH, "//a[@href='/feed']")
    ORDERS_PAGE = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    CONSTRUCTOR_PAGE = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    CART = (By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]')
    BUN_COUNTER = (By.XPATH, '//p[contains(@class, "counter_counter__num")]')
    MODAL_ORDER_NUMBER = (By.XPATH,'//section//div[1]/div/p[contains(text(), "идентификатор заказа")]')
    ORDER_NUMBER_FOR_SAVE = (By.XPATH, '//h2[contains(@class, "text_type_digits-large")]')
    BUTTON_COMPLETE_ORDER = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    LIST_FOR_ORDERS = (By.XPATH, '//p[contains(text(), "Лента Заказов")]')

    @staticmethod
    def get_last_order_number_locator(last_order_number):
        return By.XPATH, f'//ul/li/a/div[1]/p[contains(text(), "{last_order_number}")]'


class OrderListsLocators:
    FIRST_ORDER_IN_LIST = (By.CSS_SELECTOR, 'main ul > li:first-child')
    MODAL_WITH_ORDER_FROM_LIST = (By.XPATH, '//section[2]/div[contains(@class, "Modal_modal__container")]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close")]')
    IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
    ALL_TIME_READY_ORDERS = (By.XPATH, '//p[contains(text(), "Выполнено за все время:")]/following-sibling::p')
    TODAY_READY_ORDERS = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня:")]/following-sibling::p')

    @staticmethod
    def get_order_number_locator(order_number):
        return By.XPATH, f'//ul/li/a/div[1]/p[contains(text(), "{order_number}")]'

