from pages.page import Page
from pages.create_order1 import CreateOrderNet1
from selenium.webdriver.common.by import By


class CreateOrderNet3(CreateOrderNet1):
    """Locators on the page of registering service package through the Internet, third step
    firstNameUkr, lastNameUkr, middleNameUkr, docSr, docNo, nextButton is using from class CreateOrderNet1"""

    @property
    def firstNameEng_input(self):
        return self.driver.find_element_by_id('firstNameEng')

    @property
    def secondNameEng_input(self):
        return self.driver.find_element_by_id('lastNameEng')

    @property
    def dateOfBirth_input(self):
        return self.driver.find_element_by_id('dateOfBirth')

    @property
    def delivTypeBranch_radio(self):
        return self.driver.find_element_by_id('deliveryType-TOBO')

    @property
    def delivTypeCourier_radio(self):
        return self.driver.find_element_by_id('deliveryType-RC')

    @property
    def docIssueDate_input(self):
        return self.driver.find_element_by_id('docIssueDate')

    @property
    def docIssPlace_input(self):
        return self.driver.find_element_by_id('docIssPlace')

    @property
    def placeOfBirth_input(self):
        return self.driver.find_element_by_id('placeOfBirth')
# Registration address
    @property
    def addressRegSearch_input(self):
        return self.driver.find_element_by_id('addressJurSearch')

    @property
    def addressStrSearch_input(self):
        return self.driver.find_element_by_id('addrStreetJur')

    @property
    def addressHouseNoSearch_input(self):
        return self.driver.find_element_by_id('addrHouseNoJur')

    @property
    def addrBuildNo_input(self):
        return self.driver.find_element_by_id('addrBuildNoJur')

    @property
    def privateHouse_check(self):
        return self.driver.find_element_by_id('privateHouseJur')

    @property
    def addrFlat_input(self):
        return self.driver.find_element_by_id('addrFlatJur')
# Actual address
    @property
    def sameAsRegAddress_check(self):
        return self.driver.find_element_by_id('sameAsJurAddress')

    @property
    def addrActualSearch_input(self):
        return self.driver.find_element_by_id('addressSearch')

    @property
    def addrActualStr_input(self):
        return self.driver.find_element_by_id('addrStreet')

    @property
    def addrActualHouseNo_input(self):
        return self.driver.find_element_by_id('addrHouseNo')

    @property
    def addrActualBuildNo_input(self):
        return self.driver.find_element_by_id('addrBuildNo')

    @property
    def addrActualFlatNo_input(self):
        return self.driver.find_element_by_id('addrFlat')

    @property
    def actualPrivateHouse_check(self):
        return self.driver.find_element_by_id('privateHouse')
# Financial monitoring
    @property
    def empType_checklist(self):
        return self.driver.find_element_by_xpath('//*[@id="finmonGroup"]/div[1]/div[2]/button/span[2]')

    @property
    def incSource_checklist(self):
        return self.driver.find_element_by_xpath('//*[@id="finmonGroup"]/div[11]/div[2]/button/span[2]')

    @property
    def incLevelsCode_list(self):
        return self.driver.find_element_by_id('incomeLevelsCode')

    @property
    def property_checklist(self):
        return self.driver.find_element_by_xpath('//*[@id="finmonGroup"]/div[13]/div[2]/button/span[2]')

    @property
    def delivAddrReg_radio(self):
        return self.driver.find_element_by_id('adressTypeDelivery-addrJur')

    @property
    def delivAddrActual_radio(self):
        return self.driver.find_element_by_id('adressTypeDelivery-addr')

    @property
    def delivAddrOther_radio(self):
        return self.driver.find_element_by_id('adressTypeDelivery-other')
# Delivery address
    @property
    def addrDelivSearch_input(self):
        return self.driver.find_element_by_id('addressDelivSearch')

    @property
    def addrDelivStr_input(self):
        return self.driver.find_element_by_id('addrStreetDelivery')

    @property
    def addrDelivHouseNo_input(self):
        return self.driver.find_element_by_id('addrHouseNoDelivery')

    @property
    def addrDelivBuidNo_input(self):
        return self.driver.find_element_by_id('addrBuildNoDelivery')

    @property
    def addrDelivFlat_input(self):
        return self.driver.find_element_by_id('addrFlatDelivery')

    @property
    def addrDelivPrivHouse_check(self):
        return self.driver.find_element_by_id('privateHouseDelivery')
# Buttons
    @property
    def back_but(self):
        return self.driver.find_element_by_id('backButton')