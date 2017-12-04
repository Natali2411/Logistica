from pages.page import Page
from selenium.webdriver.common.by import By


class StartPage(Page):
    @property
    def logout_button(self):
        return self.driver.find_element_by_xpath('//*[@id="signoutLink"]')

    @property
    def main_block(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div')

    @property
    def reg_credit_card(self):
        return self.driver.find_element_by_xpath('*//div[@class="title-book"]//a')

