import os
from dotenv import load_dotenv
from database import insert_news

load_dotenv()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

URL = os.getenv("URL")
news= []

def navigate(link):
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options = options)
    driver.get(link)
    return driver

def scraper_news():
    driver = navigate(URL)

    items = driver.find_elements(By.XPATH,"//div[contains(@class,'_evt')]/h2//a")

    return items


def main():
    elements = scraper_news()
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