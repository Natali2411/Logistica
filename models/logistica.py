from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage
from pages.start_page import StartPage
from pages.choose_branch import ChooseBranch
from pages.choose_card import ChooseCard
from pages.logistica_card import LogisticaCard
from pages.logistica_card_search import LogCardSearch
from pages.create_order1 import CreateOrderNet1
from pages.create_order2 import CreateOrderNet2


class LogisticaApp():
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(20)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 20)
        self.wd.maximize_window()
        self.login_page = LoginPage(driver,base_url)
        self.choose_branch = ChooseBranch(driver,base_url)
        self.start_page = StartPage(driver,base_url)
        self.choose_card = ChooseCard(driver,base_url)
        self.logistica_card = LogisticaCard(driver,base_url)
        self.logistica_card_search = LogCardSearch(driver,base_url)
        self.create_order_net1 = CreateOrderNet1(driver,base_url)
        self.create_order_net2 = CreateOrderNet2(driver,base_url)
        # self.internal_page = InternalPage(driver, base_url)

    def login(self, username, password, brVal):
        self.login_page.login_input.clear()
        self.login_page.login_input.send_keys(username)
        self.login_page.pass_input.clear()
        self.login_page.pass_input.send_keys(password)
        self.login_page.submit_button.click()
        self.choose_branch.branch_input.clear()
        self.choose_branch.branch_input.send_keys(brVal)
        self.choose_branch.header_block.click()
        # to choose an appropriate branch:
        #branch = Select(self.choose_branch.branch_list)
        #branch.select_by_value(brVal)
        self.choose_branch.next_button.click()

    def logout(self):
        self.start_page.logout_button.click()

    def quit(self):
        self.wd.quit()

    def reg_creditcard(self, lastname, firstname, middlename, phonenum, famValue, childNum, docSr, docNo, taxNo,
                       empType, expYear, expMon,
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
        # self.choose_card.continue_but.click()

    def searchLogisticCard(self, packageNo, orderNo, cPref6, cSuff2, taxNo, embCardName, cardProject, dateCreateF=None,
                          dateCreateTo=None, datePersonFrom=None, datePersonTo=None, dateOnPrintFrom=None, dateExpFrom=None,
                          dateExpTo=None, dateLastChangeFrom=None, dateLastChangeTo=None, branchName=None, cardProducerVal=None,
                          renewCardVal=None, chipExistVal=None, urgentVal=None):
        self.logistica_card_search.search_tab.click()
        self.logistica_card_search.packageNo_input.clear()
        self.logistica_card_search.packageNo_input.send_keys(packageNo)
        self.logistica_card_search.orderNo_input.clear()
        self.logistica_card_search.orderNo_input.send_keys(orderNo)
        self.logistica_card_search.cardPrefix6_input.clear()
        self.logistica_card_search.cardPrefix6_input.send_keys(cPref6)
        self.logistica_card_search.cardSuffix2_input_input.clear()
        self.logistica_card_search.cardSuffix2_input_input.send_keys(cSuff2)
        self.logistica_card_search.identcode_input.clear()
        self.logistica_card_search.identcode_input.send_keys(taxNo)
        self.logistica_card_search.embCardName_input.clear()
        self.logistica_card_search.embCardName_input.send_keys(embCardName)
        self.logistica_card_search.cardProject_input.clear()
        self.logistica_card_search.cardProject_input.send_keys(cardProject)
        self.logistica_card_search.dateCreateFrom_input.clear()
        self.logistica_card_search.dateCreateFrom_input.send_keys(dateCreateF)
        self.logistica_card_search.dateCreateTo_input.clear()
        self.logistica_card_search.dateCreateTo_input.send_keys(dateCreateTo)
        self.logistica_card_search.datePersonFrom_input.clear()
        self.logistica_card_search.datePersonFrom_input.send_keys(datePersonFrom)
        self.logistica_card_search.datePersonTo_input.clear()
        self.logistica_card_search.datePersonTo_input.send_keys(datePersonTo)
        self.logistica_card_search.dateOnPrintFrom_input.clear()
        self.logistica_card_search.dateOnPrintFrom_input.send_keys(dateOnPrintFrom)
        self.logistica_card_search.dateExpFrom_input.clear()
        self.logistica_card_search.dateExpFrom_input.send_keys(dateExpFrom)
        self.logistica_card_search.dateExpTo_input.clear()
        self.logistica_card_search.dateExpTo_input.send_keys(dateExpTo)
        self.logistica_card_search.dateLastChangeFrom_input.clear()
        self.logistica_card_search.dateLastChangeFrom_input.send_keys(dateLastChangeFrom)
        self.logistica_card_search.dateLastChangeTo_input.clear()
        self.logistica_card_search.dateLastChangeTo_input.send_keys(dateLastChangeTo)
        self.logistica_card_search.branchName_input.clear()
        self.logistica_card_search.branchName_input.send_keys(branchName)
        producerList = Select(self.logistica_card_search.cardProducer_list)
        producerList.select_by_value(cardProducerVal)
        renewList = Select(self.logistica_card_search.renewCard_list)
        renewList.select_by_value(renewCardVal)
        chipExist = Select(self.logistica_card_search.chipExist_list)
        chipExist.select_by_value(chipExistVal)
        urgentList = Select(self.logistica_card_search.urgentSign_list)
        urgentList.select_by_value(urgentVal)
        self.logistica_card_search.search_but.click()

    def searchLogisticCardBarcode(self, barcodeVal):
        self.logistica_card_search.barcode_tab.click()
        self.logistica_card_search.barcode_input.clear()
        self.logistica_card_search.barcode_input.send_keys(barcodeVal)
        self.logistica_card_search.search_but.click()

    def regServicePackNet1(self, taxnoVal, lastNameVal, firstNameVal, phoneNumVal, emailVal, loyaltyCodeVal, sellPointVal, cardTypeVal):
        self.start_page.reg_service_pac_net.click()
        self.create_order_net1.identcode_input.clear()
        self.create_order_net1.identcode_input.send_keys(taxnoVal)
        self.create_order_net1.lastName_input.clear()
        self.create_order_net1.lastName_input.send_keys(lastNameVal)
        self.create_order_net1.firstName_input.clear()
        self.create_order_net1.firstName_input.send_keys(firstNameVal)
        self.create_order_net1.phoneNum_input.clear()
        self.create_order_net1.phoneNum_input.send_keys(phoneNumVal)
        self.create_order_net1.email_input.clear()
        self.create_order_net1.email_input.send_keys(emailVal)
        self.create_order_net1.loyaltyCode_input.clear()
        self.create_order_net1.loyaltyCode_input.send_keys(loyaltyCodeVal)
        sellPoint = Select(self.create_order_net1.salePoint_list)
        sellPoint.select_by_value(sellPointVal)
        cardType = Select(self.create_order_net1.cardType_list)
        cardType.select_by_value(cardTypeVal)
        self.create_order_net1.create_but.click()

    def regServicePackNet2(self, pacVal=None, currVal=None, cardTypeVal=None):
        pacType = Select(self.create_order_net2.packageType_list)
        pacType.select_by_value(pacVal)
        self.create_order_net2.currency_list.click()
        # choose currency
        if 'UAH' in currVal:
            self.create_order_net2.currency_UAH.click()
        if 'USD' in currVal:
            self.create_order_net2.currency_USD.click()
        if 'EUR' in currVal:
            self.create_order_net2.currency_EUR.click()
        cardType = Select(self.create_order_net2.cardType_list)
        cardType.select_by_value(cardTypeVal)
        self.create_order_net2.next_but.click()

    def regServicePackNet3(self):
        pass

