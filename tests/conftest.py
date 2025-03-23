import pytest
from selenium import webdriver
import requests
import uuid

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


def driver():
    driver = webdriver.Chrome()  # или webdriver.Firefox() в зависимости от вашего браузера
    driver.maximize_window()
    yield driver

    driver.quit()


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
