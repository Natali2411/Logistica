from pages.page import Page
from selenium.webdriver.common.by import By


class ChooseCard(Page):
    @property
    def logout_but(self):
        return self.driver.find_element_by_css_selector('.top_buts>a:nth-child(2)')

    @property
    def backToStartPage_but(self):
        return self.driver.find_element_by_css_selector('.top_buts>a:nth-child(1)')

    @property
    def card_maximum(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CCGRCB"]')

    @property
    def card_cash(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CCCASH"]')

    @property
    def card_skypass_world(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CC_MAU__MCWRLD"]')

    @property
    def card_skypass_plat(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CC_MAU__MCPLTN"]')

    @property
    def card_eko_maximum(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CC_EKO"]')

    @property
    def card_connect_debworld(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CC_MTS__MCDWRD"]')

    @property
    def card_foxclub(self):
        return self.driver.find_element_by_xpath('//input[@id="productCode"][@value="CC_FOX__MCWRLD"]')

    @property
    def lastname_input(self):
        return self.driver.find_element_by_id('lastNameUkr')

    @property
    def firstname_input(self):
        return self.driver.find_element_by_id('firstNameUkr')

    @property
    def middlename_input(self):
        return self.driver.find_element_by_id('middleNameUkr')

    @property
    def phonenum_input(self):
        return self.driver.find_element_by_id('contInf2Cellur')

    @property
    def familyStatus_list(self):
        return self.driver.find_element_by_xpath('//*[@id="applicantFamilyStatusTypeId"]')

    @property
    def numOfChildren_input(self):
        return self.driver.find_element_by_id('numberOfChildren')

    #check locator
    @property
    def pass_radiobut(self):
        return self.driver.find_element_by_xpath('//*[@id="docTypeId"][@value="1"]')
    # check locator
    @property
    def passId_radiobut(self):
        return self.driver.find_element_by_xpath('//*[@id="docTypeId"][@value="29"]')

    @property
    def docSr_input(self):
        return self.driver.find_element_by_id('docSr')

    @property
    def docNo_input(self):
        return self.driver.find_element_by_id('docNo')

    @property
    def identcode_input(self):
        return self.driver.find_element_by_id('taxId')

    @property
    def employ_type_list(self):
        return self.driver.find_element_by_id('typeOfEmployment')

    @property
    def workExpYear_input(self):
        return self.driver.find_element_by_id('totalWorkExpYears')

    @property
    def workExpMon_input(self):
        return self.driver.find_element_by_id('totalWorkExpMonths')

    @property
    def mainIncome_input(self):
        return self.driver.find_element_by_id('financeBasicIncomeAmount')

    @property
    def addIncome_input(self):
        return self.driver.find_element_by_id('financeAdditionalIncomeAmount')

    @property
    def loan_input(self):
        return self.driver.find_element_by_id('morLoanInOtherBank_monthlyPaym')

    @property
    def partner_input(self):
        return self.driver.find_element_by_id('partner')

    @property
    def resource_input(self):
        return self.driver.find_element_by_id('resource')

    @property
    def continue_but(self):
        return self.driver.find_element_by_css_selector('a.but_1:nth-child(1)')

    @property
    def findOrder_but(self):
        return self.driver.find_element_by_css_selector('.forward')

    @property
    def viewDoc_link(self):
        return self.driver.find_element_by_id('view_doc')

    @property
    def askQuest_link(self):
        return self.driver.find_element_by_css_selector('.skype_talk')

