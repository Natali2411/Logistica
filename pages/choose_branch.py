from pages.page import Page
from selenium.webdriver.common.by import By

class ChooseBranch(Page):
    """Locators for choosing branch after authorization: entering login and password"""
    @property
    def header_block(self):
        return self.driver.find_element_by_id('header')

    @property
    def choose_branch_box(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div')

    @property
    def branch_list(self):
        return self.driver.find_element_by_id('ShopId')

    @property
    def branch_input(self):
        return self.driver.find_element_by_id('shopIdSearch')

    @property
    def next_button(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/input[3]')