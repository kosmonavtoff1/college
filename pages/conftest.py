import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome() # Инициализируем браузер Chrome
    yield browser
    print("\nquit browser..")
    browser.quit() # Закрываем браузер после выполнения теста