from pages.login_page import LoginPage
from pages.start_page import StartPage
from selenium.webdriver.common.by import By
import time



def test_creditcard(init_page, login):
    init_page.reg_creditcard(lastname='Тютюнник', firstname='Наталія', middlename='Василівна', phonenum='983294154', famValue='WIDOWED',
                             childNum=2, docSr='ME', docNo='357825', taxNo='1234567890', empType='OWN_BUSINESS', expYear='2', expMon='3',
                             mainInc='25000', addInc='5000', loanSum='0', partner='Partner1', resource='Resource1')
