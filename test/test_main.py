from selenium import webdriver
from unittest import TestCase
import unittest
from time import sleep


class TestAzercell(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser_driver = webdriver.Firefox(
            executable_path=r'C:/Users/hasan/OneDrive/AikaDesktopFIles/Python/final-task-AikaHasanova/geckodriver')
        cls.browser_driver.implicitly_wait(20)
        cls.browser_driver.get('http://azercell.com/my/login')
        cls.browser_driver.find_element_by_css_selector('li.b-nav__list:nth-child(3) > a:nth-child(1)').click()
        cls.browser_driver.find_element_by_css_selector('#mat-input-1').click()
        cls.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('518179001')
        cls.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        cls.browser_driver.find_element_by_css_selector('#mat-input-2').send_keys('a12345')
        cls.browser_driver.find_element_by_css_selector('.btn').click()

    def test_main_numbertype_line_balance_expire_removaldate_current_tariff(self):#M001
        actual_result = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.row.b-card__top > div.col-xs-6.b-card__top--right.text-right > button').text

        expected_result = 'Pre-paid'
        assert expected_result == actual_result
        actual_line = self.browser_driver.find_element_by_css_selector('.text-success > strong:nth-child(1)').text
        expected_line = 'Open'
        assert expected_line == actual_line

        actual_balance = self.browser_driver.find_element_by_css_selector('.main-color').text
        actual_balance = actual_balance.strip()
        print('balance', actual_balance)
        expected_balance = '71.33 AZN'
        assert expected_balance in actual_balance

        actual_expdate = self.browser_driver.find_element_by_css_selector(
            'p.text-left:nth-child(2) > b:nth-child(1)').text
        expected_expdate = ': 06/10/2020'
        assert expected_expdate == actual_expdate

        actual_rmvdate = self.browser_driver.find_element_by_css_selector(
            '.inline-block > b:nth-child(1)').text
        expected_rmvdate = '04/01/2021'
        assert expected_rmvdate == actual_rmvdate

        actual_tariff = self.browser_driver.find_element_by_css_selector(
            '.tariff > b:nth-child(1)').text
        expected_tariff = 'Azercellim'
        assert expected_tariff in actual_tariff



    def test_main_linestatus(self):#M002
        #alt.self.browser_driver.find_element_by_class_name('mat-slide-toggle-label').click()
        self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
        assert self.browser_driver.find_element_by_css_selector('.alert-dialog')

    def test_cancel_line_deactivation(self):#M004 passed
        self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
        self.browser_driver.find_element_by_css_selector('button.mat-button:nth-child(1) > span:nth-child(1)').click()
        assert self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')

    def test_line_activation(self):#M006
        self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
        self.browser_driver.find_element_by_css_selector('button.mat-button:nth-child(2)').click()
        self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
        actual_line_status = self.browser_driver.find_element_by_css_selector(
            '.text-success > strong:nth-child(1)').text
        expected_line_status='Open'
        assert expected_line_status in actual_line_status



    def test_main_page_in_english(self):#M027

        expected_main = 'Main'
        actual_main = self.browser_driver.find_element_by_css_selector(
            'div.col-xs-6:nth-child(1) > h3:nth-child(1)').text
        assert expected_main == actual_main

        expected_prepaid = 'Pre-paid'
        actual_prepaid = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.row.b-card__top > div.col-xs-6.b-card__top--right.text-right > button').text
        assert expected_prepaid == actual_prepaid

        expected_balance = 'Balance'
        actual_balance = self.browser_driver.find_element_by_css_selector(
            '.main--title').text
        assert expected_balance == actual_balance

        expected_line_status = 'LINE STATUS'
        actual_line_status = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(1) > span:nth-child(1)').text
        assert expected_line_status == actual_line_status

        expected_tariff = 'TARIFF'
        actual_tariff = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(2) > span:nth-child(1)').text
        assert expected_tariff == actual_tariff

        expected_status = 'Open'
        actual_status= self.browser_driver.find_element_by_css_selector(
            '.text-success').text
        assert expected_status == actual_status

        expected_azercellim = 'Azercellim'
        actual_azercellim = self.browser_driver.find_element_by_css_selector(
            'strong.main-color').text
        assert expected_azercellim == actual_azercellim

        expected_one_way_blocking = 'ONE-WAY BLOCKING'
        actual_one_way_blocking = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(7) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_one_way_blocking == actual_one_way_blocking

        expected_removal_date = 'REMOVAL DATE'
        actual_removal_date = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(9) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_removal_date == actual_removal_date

    def test_main_page_in_russian(self):#M028
        self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nav-container.white-back > div > div.b-nav.col-md-10.col-xs-11.col-md-offset-1 > ul.b-nav__left > li:nth-child(4) > a').click()
        expected_main = 'Главная'
        actual_main = self.browser_driver.find_element_by_css_selector(
            'div.col-xs-6:nth-child(1)').text
        assert expected_main == actual_main
        expected_prepaid = 'Предоплата'
        actual_prepaid = self.browser_driver.find_element_by_css_selector(
            '.btn').text
        assert expected_prepaid == actual_prepaid
        expected_balance = 'Баланс'
        actual_balance = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.b-card__inner.text-start > div:nth-child(2) > span').text
        assert expected_balance == actual_balance
        expected_line_status = 'ЛИНИЯ НОМЕРА'
        actual_line_status = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(1) > span:nth-child(1)').text
        assert expected_line_status == actual_line_status
        expected_tarif = 'ТАРИФ'
        actual_tarif = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(2) > span:nth-child(1)').text
        assert expected_tarif == actual_tarif
        expected_open = 'Открыта'
        actual_open = self.browser_driver.find_element_by_css_selector(
            '.text-success').text
        assert expected_open == actual_open
        expected_azercellim = 'Azercellim'
        actual_azercellim = self.browser_driver.find_element_by_css_selector(
            'strong.main-color').text
        assert expected_azercellim == actual_azercellim
        expected_blocking = 'ОДНОСТОРОННЕЕ ЗАКРЫТИЕ'
        actual_blocking = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(7) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_blocking == actual_blocking
        expected_removal_date = 'ДАТА ЛИКВИДАЦИИ'
        actual_removal_date = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(9) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_removal_date == actual_removal_date


    def test_main_page_in_azeri(self):#M029
        self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nav-container.white-back > div > div.b-nav.col-md-10.col-xs-11.col-md-offset-1 > ul.b-nav__left > li:nth-child(5) > a').click()
        expected_main = 'Əsas'
        actual_main = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.row.b-card__top > div.col-xs-6.b-card__top--left > h3').text
        assert expected_main == actual_main
        expected_prepaid = 'Fakturasız xətt'
        actual_prepaid = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.row.b-card__top > div.col-xs-6.b-card__top--right.text-right > button').text
        assert expected_prepaid == actual_prepaid
        expected_balance = 'Balans'
        actual_balance = self.browser_driver.find_element_by_css_selector(
            '.main--title').text
        assert expected_balance == actual_balance
        expected_line_status = 'NÖMRƏNIN XƏTTI'
        actual_line_status = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(1) > span:nth-child(1)').text
        assert expected_line_status == actual_line_status
        expected_tarif = 'TARIF'
        actual_tarif = self.browser_driver.find_element_by_css_selector(
            'div.l-widget:nth-child(2) > span:nth-child(1)').text
        assert expected_tarif == actual_tarif
        expected_open = 'Açıqdır'
        actual_open = self.browser_driver.find_element_by_css_selector(
            '.text-success').text
        assert expected_open == actual_open
        expected_azercellim = 'Azercellim'
        actual_azercellim = self.browser_driver.find_element_by_css_selector(
            'strong.main-color').text
        assert expected_azercellim == actual_azercellim
        expected_blocking = 'BIRTƏRƏFLI BAĞLANMA'
        actual_blocking = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(7) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_blocking == actual_blocking
        expected_removal_date = 'LƏĞV OLUNMA TARIXI'
        actual_removal_date = self.browser_driver.find_element_by_css_selector(
            '.b-card__inner > w-progress:nth-child(9) > div:nth-child(1) > span:nth-child(1)').text
        assert expected_removal_date == actual_removal_date



    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
