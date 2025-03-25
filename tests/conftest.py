import requests
import uuid

import pytest
from selenium import webdriver

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError("Укажи браузер: --browser=chrome или --browser=firefox")

    driver.maximize_window()
    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome или firefox",
    )


@pytest.fixture
def unique_user():
    unique_email = f"test_user_{uuid.uuid4().hex[:8]}@mail.com"
    user_data = {
        "email": unique_email,
        "password": "password123",
        "name": "UniqueTestUser"
    }

    # Регистрируем нового пользователя
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    assert response.status_code == 200, f"Failed to register user: {response.status_code}, response: {response.json()}"
    token = response.json()["accessToken"]

    # Добавляем токен в данные пользователя
    user_data["token"] = token
    yield user_data

    # Удаляем пользователя после теста
    requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": f"Bearer {token}"})
