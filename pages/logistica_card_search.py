from pages.page import Page
from pages.logistica_card import LogisticaCard
from pages.start_page import StartPage


class LogCardSearch(StartPage, LogisticaCard):
    #Locators on the page on searching logistic cards
    @property
    def search_tab(self):
        return self.driver.find_element_by_xpath('//*[@id="searchTabs"]/a[1]')

    @property
    def barcode_tab(self):
        return self.driver.find_element_by_xpath('//*[@id="searchTabs"]/a[2]')

    @property
    def barcodeSearch_but(self):
        return self.driver.find_element_by_xpath('//*[@id="findByCodeForm"]/div[2]/div/input')

    @property
    def barcode_input(self):
        return self.driver.find_element_by_id('codes')

    @property
    def packageNo_input(self):
        return self.driver.find_element_by_id('batchId')

    @property
    def orderNo_input(self):
        return self.driver.find_element_by_id('orderId')

    @property
    def cardPrefix6_input(self):
        return self.driver.find_element_by_id('cardPrefix')

    @property
    def cardSuffix2_input(self):
        return self.driver.find_element_by_id('cardSuffix')

    @property
    def identcode_input(self):
        return self.driver.find_element_by_id('taxId')

    @property
    def embCardName_input(self):
        return self.driver.find_element_by_id('embCardName')

    @property
    def cardProject_input(self):
        return self.driver.find_element_by_id('cardProject')

    @property
    def dateCreateFrom_input(self):
        return self.driver.find_element_by_id('dateCreateFrom')

    @property
    def dateCreateTo_input(self):
        return self.driver.find_element_by_id('dateCreateTo')

    @property
    def datePersonFrom_input(self):
        return self.driver.find_element_by_id('datePersonFrom')

    @property
    def datePersonTo_input(self):
        return self.driver.find_element_by_id('datePersonTo')

    @property
    def dateOnPrintFrom_input(self):
        return self.driver.find_element_by_id('dateOnPrintFrom')

    @property
    def dateOnPrintTo_input(self):
        return self.driver.find_element_by_id('dateOnPrintTo')

    @property
    def datePersonTo_input(self):
        return self.driver.find_element_by_id('')

    @property
    def dateExpFrom_input(self):
        return self.driver.find_element_by_id('dateExpFrom')

    @property
    def dateExpTo_input(self):
        return self.driver.find_element_by_id('dateExpTo')

    @property
    def dateLastChangeFrom_input(self):
        return self.driver.find_element_by_id('dateLastChangeFrom')

    @property
    def dateLastChangeTo_input(self):
        return self.driver.find_element_by_id('dateLastChangeTo')

    @property
    def branchName_input(self):
        return self.driver.find_element_by_id('findByCodeForm:shopNameShort')

    @property
    def cardProducer_list(self):
        return self.driver.find_element_by_id('manufacturer')

    @property
    def renewCard_list(self):
        return self.driver.find_element_by_id('renewLabel')

    @property
    def chipExist_list(self):
        return self.driver.find_element_by_id('chipExist')

    @property
    def urgentSign_list(self):
        return self.driver.find_element_by_id('urgent')

    @property
    def search_but(self):
        return self.driver.find_element_by_xpath('//*[@id="filterCards"]/div[17]/div/input')