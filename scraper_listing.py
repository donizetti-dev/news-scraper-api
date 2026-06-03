import sys
import os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(root)

from dotenv import load_dotenv
from database import insert_news
from browser import get_driver

load_dotenv()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep

URL = os.getenv("URL")
news= []

def load_page(driver):
    count_loop = 30
    for i in range(count_loop):
        
        qtd_news = len(scraper_news(driver))

        if qtd_news>=30:
            #30 notícias carregadas, seguindo processamento
            break


        driver.execute_script("document.querySelector('#feed-placeholder > div > div > div.load-more.gui-color-primary-bg > a').click()")

        sleep(0.5)


def scraper_news(driver) -> list:

    items = driver.find_elements(By.XPATH,"//div[contains(@class,'_evt')]/h2//a")

    return items


def main():
    driver = get_driver(URL)

    load_page(driver)

    elements = scraper_news(driver)
    for element in elements[:30]:

        link = element.get_attribute("href")
        news.append({
            "titulo": "PENDENTE",
            "subtitulo": "PENDENTE",
            "descricao": "PENDENTE",
            "link": link
        })

    insert_news(news)


if __name__=="__main__":
    main()