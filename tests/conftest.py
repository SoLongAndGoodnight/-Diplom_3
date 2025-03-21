import pytest
from selenium import webdriver
import requests
import uuid

@pytest.fixture
#def driver():
    #return webdriver.Chrome()
    #driver.maximize_window()
    #yield
    #


def driver():
    # Создание экземпляра WebDriver
    driver = webdriver.Chrome()  # или webdriver.Firefox() в зависимости от вашего браузера
    driver.maximize_window()
    yield driver  # Возвращаем драйвер тесту и приостанавливаем фикстуру

    # Завершение работы драйвера после выполнения теста
    driver.quit()


BASE_URL = "https://stellarburgers.nomoreparties.site/api"

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
