import sys
import os

from dotenv import load_dotenv
from database import insert_news
from browser import get_driver
from logger_config import logger

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
    logger.info(f'Iniciando função')

    count_loop = 30
    logger.info(f'Inicia loop para carregar página até 30 casos')
    for i in range(count_loop):
        
        qtd_news = len(scraper_news(driver))

        if qtd_news>=30:
            #30 notícias carregadas, seguindo processamento
            logger.info(f'30 notícias carregadas, seguindo processamento')
            break

        logger.info(f'Aguardando carregamento {i}\{count_loop} notícias carregadas: {qtd_news}')    
        driver.execute_script("document.querySelector('#feed-placeholder > div > div > div.load-more.gui-color-primary-bg > a').click()")

        sleep(0.5)


def scraper_news(driver) -> list:
    logger.info(f'Buscando notícias')
    items = driver.find_elements(By.XPATH,"//div[contains(@class,'_evt')]/h2//a")

    return items


def main():
    logger.info(f'{"="*30}{__name__}{"="*30}')
    
    logger.info(f'Inicia navegador')
    driver = get_driver(URL)

    logger.info(f'Chama função para carregar página')
    load_page(driver)

    logger.info(f'Chama função para busca de notícias')
    elements = scraper_news(driver)

    logger.info(f'Loop sobre notícias para insert de links no banco')
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