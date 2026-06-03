import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from database import query_pending, update_details
from browser import get_driver
from logger_config import logger




def get_detail(driver):
    caption = driver.find_elements(By.XPATH,"//h2[contains(@class,'content-head__subtitle')]")

    description = driver.find_elements(By.XPATH,"//h2[contains(@class,'content-head__subtitle')]//ancestor::div[contains(@class,'mc-article-header')]//following::div[contains(@class,'mc-article-body')]//p[contains(@class,' content-text__container ')][1]")

    title = driver.find_elements(By.XPATH,"//main[contains(@class,'mc-body theme')]//h1[contains(@class,'content-head__title')]")


    return {'subtitulo':caption[0].text.replace("'",'"'),
            'descricao':description[0].text.replace("'",'"'), 
            'titulo':title[0].text.replace("'",'"')}



def main():
    logger.info(f'{"="*30}{__name__}{"="*30}')

    logger.info(f'Verifica linhas pendentes para busca de detalhes')
    process = query_pending()

    logger.info(f'Identificado {len(process)} processos pendentes')

    for news in process:
        driver = get_driver(news['link'])

        dict_details = get_detail(driver)
        logger.info(f'Identificado detalhes para notícia {dict_details['titulo']}')

        logger.info(f'Atualiza id {news['id']} com informações extraídas')
        update_details(news['id'],dict_details)

        logger.info(f'Finaliza driver')
        driver.quit()

    logger.info(f'Fim da execução')


if __name__=='__main__':
    main()


