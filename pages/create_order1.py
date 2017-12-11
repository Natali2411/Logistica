from pages.page import Page
from selenium.webdriver.common.by import By

class CreateOrderNet1(Page):
    """Locators on the page of registering service package through the Internet, first step"""

    @property
    def identcode_input(self):
        return self.driver.find_element_by_id('taxId')

    @property
    def lastName_input(self):
        return self.driver.find_element_by_id('lastNameUkr')

    @property
    def firstName_input(self):
        return self.driver.find_element_by_id('firstNameUkr')

    @property
    def phoneNum_input(self):
        return self.driver.find_element_by_id('contInf2CellurSite')

    @property
    def email_input(self):
        return self.driver.find_element_by_id('contInf5EMail')

    @property
    def loyaltyCode_input(self):
        return self.driver.find_element_by_id('externalCode')

    @property
    def salePoint_list(self):
        return self.driver.find_element_by_id('salePoint')

    @property
    def cardType_list(self):
        return self.driver.find_element_by_id('cardType')

    @property
    def create_but(self):
        return self.driver.find_element_by_xpath('//*[@id="createAppForm"]/button')