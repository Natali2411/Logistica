from pages.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    @property
    def login_input(self):
        return self.driver.find_element_by_id('user')

    @property
    def pass_input(self):
        return self.driver.find_element_by_id('password')

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath('//*[@id="loginForm"]/p/input')

    @property
    def choose_branch_box(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div')