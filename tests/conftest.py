import pytest
from selenium import webdriver
from utilities.eye_manager import Eyes_Manager

APP_UNDER_TEST = 'https://staging-financing-v2-auth.manafatech.com/auth/login'

driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get(APP_UNDER_TEST)
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture(scope='class')
def eyes():
    eyes_instance = Eyes_Manager.initialize_eyes()
    yield eyes_instance



