import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from database import query_pending
from browser import get_driver




def main():
    driver = get_driver('url')


