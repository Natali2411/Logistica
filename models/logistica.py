from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage
from pages.start_page import StartPage
from pages.choose_branch import ChooseBranch
from pages.choose_card import ChooseCard
from pages.logistica_card import LogisticaCard

class LogisticaApp():
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(20)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 20)
        self.wd.maximize_window()
        self.login_page = LoginPage()
        self.choose_branch = ChooseBranch()
        self.start_page = StartPage()
        self.choose_card = ChooseCard()
        self.logistica_card = LogisticaCard()
        #self.internal_page = InternalPage(driver, base_url)

    def login(self, username, password):
        self.login_page.login_input.clear()
        self.login_page.login_input.send_keys(username)
        self.login_page.pass_input.clear()
        self.login_page.pass_input.send_keys(password)
        self.login_page.submit_button.click()
        # to choose an appropriate branch:
        # init_page.choose_branch.branch_list_button.click()
        # init_page.choose_branch.branch_list.click()
        self.choose_branch.next_button.click()

    def logout(self):
        self.start_page.logout_button.click()

    def quit(self):
        self.wd.quit()

    def reg_creditcard(self, lastname, firstname, middlename, phonenum, famValue, childNum, docSr, docNo, taxNo, empType, expYear, expMon,
                       mainInc, addInc, loanSum, partner, resource):
        self.start_page.reg_credit_card.click()
        self.choose_card.card_maximum.click()
        self.choose_card.lastname_input.clear()
        self.choose_card.lastname_input.send_keys(lastname)
        self.choose_card.firstname_input.clear()
        self.choose_card.firstname_input.send_keys(firstname)
        self.choose_card.middlename_input.clear()
        self.choose_card.middlename_input.send_keys(middlename)
        self.choose_card.phonenum_input.clear()
        self.choose_card.phonenum_input.send_keys(phonenum)
        famTypeList = Select(self.choose_card.familyStatus_list)
        famTypeList.select_by_value(famValue)
        self.choose_card.numOfChildren_input.clear()
        self.choose_card.numOfChildren_input.send_keys(childNum)
        # choose docType
        self.choose_card.docSr_input.clear()
        self.choose_card.docSr_input.send_keys(docSr)
        self.choose_card.docNo_input.clear()
        self.choose_card.docNo_input.send_keys(docNo)
        self.choose_card.identcode_input.clear()
        self.choose_card.identcode_input.send_keys(taxNo)
        empTypeList = Select(self.choose_card.employ_type_list)
        empTypeList.select_by_value(empType)
        self.choose_card.workExpYear_input.clear()
        self.choose_card.workExpYear_input.send_keys(expYear)
        self.choose_card.workExpMon_input.clear()
        self.choose_card.workExpMon_input.send_keys(expMon)
        self.choose_card.mainIncome_input.clear()
        self.choose_card.mainIncome_input.send_keys(mainInc)
        self.choose_card.addIncome_input.clear()
        self.choose_card.addIncome_input.send_keys(addInc)
        self.choose_card.loan_input.clear()
        self.choose_card.loan_input.send_keys(loanSum)
        self.choose_card.partner_input.clear()
        self.choose_card.partner_input.send_keys(partner)
        self.choose_card.resource_input.clear()
        self.choose_card.resource_input.send_keys(resource)
        #self.choose_card.continue_but.click()
