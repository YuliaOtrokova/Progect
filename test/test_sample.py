from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By


def test_sample():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.saucedemo.com/")


    assert driver.title == 'Swag Labs'
    driver.quit()