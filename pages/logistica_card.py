from pages.page import Page
from pages.start_page import StartPage
from selenium.webdriver.common.by import By

class LogisticaCard(Page):
    @property
    def acceptProducerCard_link(self):
        return self.driver.find_element_by_xpath('//div[@id="content"]/div[1]/a[1]')

    @property
    def acceptByBranch_link(self):
        return self.driver.find_element_by_xpath('//*[@id="content"]/div/a[2]')

    @property
    def delCardOnBranch_link(self):
        return self.driver.find_element_by_xpath('//*[@id="content"]/div/a[3]')

    @property
    def showAllCard_link(self):
        return self.driver.find_element_by_xpath('//*[@id="content"]/div/a[4]')

    @property
    def backToMainPage_link(self):
        return self.driver.find_element_by_id('dashboardLink')