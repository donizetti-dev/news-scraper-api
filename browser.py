import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_driver(link):
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options = options)
    driver.get(link)
    return driver