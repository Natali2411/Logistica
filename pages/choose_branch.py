from pages.page import Page
from selenium.webdriver.common.by import By

class ChooseBranch(Page):
    """Locators for choosing branch after authorization: entering login and password"""
    @property
    def choose_branch_box(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div')

    @property
    def branch_list_button(self):
        return self.driver.find_element_by_id('shopid')

    @property
    def branch_list(self):
        return self.driver.find_element_by_xpath('*//input[@value=28124')

    @property
    def next_button(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/input[3]')