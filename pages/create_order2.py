from pages.page import Page
from selenium.webdriver.common.by import By

class CreateOrderNet2(Page):
    """Locators on the page of registering service package through the Internet, second step"""

    @property
    def packageType_list(self):
        return self.driver.find_element_by_id('packageId')

    @property
    def currency_list(self):
        return self.driver.find_element_by_xpath('//*[@id="selectPackageGroup"]/div[2]/div[2]/button/span[1]')

    @property
    def cardType_list(self):
        return self.driver.find_element_by_id('cardType')

    @property
    def next_but(self):
        return self.driver.find_element_by_id('nextButton')
