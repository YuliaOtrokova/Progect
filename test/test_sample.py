from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_sample():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
    driver.get("https://www.saucedemo.com/")
    assert driver.title == 'Swag Labs'
    driver.quit()
