from pages.page import Page
from models.logistica import LogisticaApp
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

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

@pytest.fixture()
def init_page_ie():
    driverLocation = "D:\\Python\\Selenium\\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = driverLocation
    cap = DesiredCapabilities().INTERNETEXPLORER.copy()
    cap['platform'] = "Win7"
    cap['version'] = "11"
    cap['browserName'] = "internet explorer"
    cap['ignoreProtectedModeSettings'] = True
    cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
    cap['nativeEvents'] = True
    cap['ignoreZoomSetting'] = True
    cap['requireWindowFocus'] = True
    cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    driver = webdriver.Ie(desired_capabilities=cap)
    page = LogisticaApp(driver=driver, base_url="https://kcfrntapu02.alfa.bank.int:8443/front/")
    yield page
    page.quit()