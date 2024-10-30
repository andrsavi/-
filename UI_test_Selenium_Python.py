from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие сайта
driver.get("https://example-store.com")
driver.maximize_window()

# Тест авторизации
def test_login():
    driver.find_element(By.ID, "login").click()
    driver.find_element(By.NAME, "username").send_keys("user")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3)
    assert "Dashboard" in driver.page_source

test_login()
driver.quit()

