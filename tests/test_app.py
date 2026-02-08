import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dash.testing.browser import Browser

@pytest.fixture
def dash_duo():
    driver_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "chromedriver.exe"
    )

    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    browser = Browser(driver=driver)

    yield browser

    browser.driver.quit()
