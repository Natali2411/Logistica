import time
from pages.login_page import LoginPage
from pages.start_page import StartPage
from models.logistica import LogisticaApp
from selenium.webdriver.common.by import By


def test_create_servicepack_net(init_page, login):
    init_page.regServicePackNet1(taxnoVal='1141633536', lastNameVal='Пархомцева', firstNameVal='Тетяна',
                                 phoneNumVal='972570575', emailVal='default@ukr.net', loyaltyCodeVal='123', sellPointVal='PS_cB', cardTypeVal='CARBON')
    assert init_page.create_order_net2
    init_page.regServicePackNet2(pacVal="1", currVal=['UAH', 'USD'], cardTypeVal="WZ")
    time.sleep(60)


