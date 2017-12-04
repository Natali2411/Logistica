from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.start_page import StartPage
from pages.choose_branch import ChooseBranch

class LogisticaApp():
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(20)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 20)
        self.wd.maximize_window()
        self.login_page = LoginPage(driver, base_url)
        self.choose_branch = ChooseBranch(driver, base_url)
        self.start_page = StartPage(driver, base_url)
        #self.internal_page = InternalPage(driver, base_url)

    def login(self, username, password):
        self.login_page.login_input.clear()
        self.login_page.login_input.send_keys(username)
        self.login_page.pass_input.clear()
        self.login_page.pass_input.send_keys(password)
        self.login_page.submit_button.click()

    def logout(self):
        self.start_page.logout_button.click()

    def quit(self):
        self.wd.quit()