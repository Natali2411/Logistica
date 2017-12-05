from pages.login_page import LoginPage
from pages.start_page import StartPage
from selenium.webdriver.common.by import By
import time

def test_login(init_page):
    init_page.login(username='CFRONTTPT02', password='12345678')
    time.sleep(10)  # change later
    assert init_page.start_page.main_block
    assert init_page.start_page.logout_button
