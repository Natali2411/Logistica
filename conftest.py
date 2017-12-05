from pages.page import Page
from models.logistica import LogisticaApp
import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="session")
def init_page():
    driver = webdriver.Firefox()
    page = LogisticaApp(driver=driver, base_url="https://kcfrntapu02.alfa.bank.int:8443/front/")
    yield page
    #page.quit()

@pytest.fixture()
def login(init_page):
    init_page.login(username='CFRONTTPT02', password='12345678')
    time.sleep(10)  # change later
    yield
    #init_page.logout()

