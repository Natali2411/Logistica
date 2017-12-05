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
        return self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/p[1]/a')

    @property
    def logistic_card(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(1)>p:nth-child(3)>a:nth-child(1)')

    @property
    def logistic_card_old(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(1)>p:nth-child(4)>a:nth-child(1)')

    @property
    def reg_service_pac(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(2)> p:nth-child(2)>a:nth-child(1)')

    @property
    def reg_service_pac_net(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(2)>p:nth-child(3)>a:nth-child(1)')

    @property
    def ips_contact_cen(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(2)>p:nth-child(4)>a:nth-child(1)')

    @property
    def reg_retail_cred(self):
        return self.driver.find_element_by_css_selector('div.border-block-inner:nth-child(3)>p:nth-child(2)>a:nth-child(1)')

    @property
    def ithelp_email(self):
        return self.driver.find_element_by_css_selector('#footer>p:nth-child(1)>a:nth-child(1)')

    @property
    def client_search(self):
        return self.driver.find_element_by_id('clientSearchLink')