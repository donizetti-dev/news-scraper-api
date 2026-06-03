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
    count = 0
    for element in elements[:5]:

        link = element.get_attribute("href")
        news.append({
            "titulo": "PENDENTE",
            "subtitulo": "PENDENTE",
            "descricao": "PENDENTE",
            "link": link
        })
        count+=1
        print(count)
    insert_news(news)


if __name__=="__main__":
    main()