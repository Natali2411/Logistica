from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_login(init_page):
    init_page.login(username='CFRONTTPT02', password='12345678')
    time.sleep(10)  # change later
    assert 'Виберіть відділення' in init_page.choose_branch.choose_branch_box.text
    #init_page.choose_branch.branch_list_button.click()
    #init_page.choose_branch.branch_list.click()
    init_page.choose_branch.next_button.click()
    assert init_page.start_page.main_block

