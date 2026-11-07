import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", default="en", help="Browser language")


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": request.config.getoption("language")})
    if os.getenv("CHROME_BINARY"):
        options.binary_location = os.environ["CHROME_BINARY"]
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
