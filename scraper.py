import os
from dotenv import load_dotenv
from database import insert_news

load_dotenv()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


URL = os.getenv("URL")
news= []

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options = options)
driver.get(URL)
elements = driver.find_elements(By.XPATH,"//div[contains(@class,'_evt')]/h2//a")


if __name__=="__main__":
    for element in elements[:5]:
        titulo = element.text
        link = element.get_attribute("href")
        news.append({
            "titulo": element.text,
            "subtitulo": "(IMPLEMENTAR)",
            "descricao": "(IMPLEMENTAR)",
            "link": link
        })
    insert_news(news)