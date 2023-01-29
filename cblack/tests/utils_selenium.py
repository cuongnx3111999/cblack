import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def chrome_browser_instance(request):

    option = Options()
    option.headless=False
    browser = webdriver.Chrome(executable_path="F:\\chromedriver.exe",options=option)
    yield  browser
    browser.close()