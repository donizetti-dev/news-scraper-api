import os
from dotenv import load_dotenv
from database import insert_news
from browser import get_driver

load_dotenv()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

URL = os.getenv("URL")
news= []



def scraper_news(driver):

    items = driver.find_elements(By.XPATH,"//div[contains(@class,'_evt')]/h2//a")

    return items


def main():
    driver = get_driver(URL)

    elements = scraper_news(driver)
    for element in elements[:5]:

        titulo = element.text
        link = element.get_attribute("href")
        input(element)
        element.click()
        time.sleep(100)
        input(element)
        news.append({
            "titulo": element.text,
            "subtitulo": "(IMPLEMENTAR)",
            "descricao": "(IMPLEMENTAR)",
            "link": link
        })

    insert_news(news)


if __name__=="__main__":
    main()