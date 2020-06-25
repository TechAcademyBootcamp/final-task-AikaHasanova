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



    def test_main_page_in_russian(self):#M028
        self.browser_driver.find_element_by_css_selector('li.b-nav__lang:nth-child(4) > a:nth-child(1)').click()
        expected_main = 'Главная'
        actual_main = self.browser_driver.find_element_by_css_selector(
            'div.col-xs-6:nth-child(1) > h3:nth-child(1)').text
        assert expected_main == actual_main

        expected_prepaid = 'Предоплата'
        actual_prepaid = self.browser_driver.find_element_by_css_selector('.btn').text
        assert expected_prepaid == actual_prepaid

        expected_line = 'Линия номера'
        actual_line=self.browser_driver.find_element_by_css_selector('div.switch:nth-child(2) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_line==actual_line

        expected_open = 'Открыта'
        actual_open = self.browser_driver.find_element_by_css_selector(
            '.text-success').text
        assert expected_open == actual_open

        expected_line_activation = 'Линия связи'
        actual_line_activation=self.browser_driver.find_element_by_css_selector('div.switch:nth-child(4) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_line_activation in actual_line_activation

        expected_roaming = 'Роуминг линия'
        actual_roaming=self.browser_driver.find_element_by_css_selector('div.switch:nth-child(6) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_roaming in actual_roaming

        expected_roaming_text = 'Перед выездом заграницу рекомендуется учитывать тарифы по роумингу и выгодные предложения. Дополнительно '
        actual_roaming_text=self.browser_driver.find_element_by_css_selector('p.text-left:nth-child(3)').text
        assert expected_roaming_text== actual_roaming_text

        expected_roaming_more = 'Дополнительно'
        actual_roaming_more=self.browser_driver.find_element_by_css_selector('p.text-left:nth-child(3) > a:nth-child(1)').text
        assert expected_roaming_more == actual_roaming_more

        expected_balance = 'Основной баланс: 71.33 AZN'
        actual_balance = self.browser_driver.find_element_by_css_selector('p.simple-p:nth-child(1)').text
        assert expected_balance in actual_balance

        expected_expdate = 'Последняя дата пользования: 06/10/2020 '
        actual_expdate=self.browser_driver.find_element_by_css_selector('p.text-left:nth-child(2)').text
        assert actual_expdate == expected_expdate

    def test_main_page_in_english(self):
        expected_main = 'Main'
        actual_main = self.browser_driver.find_element_by_css_selector(
            'div.col-xs-6:nth-child(1) > h3:nth-child(1)').text
        assert expected_main == actual_main

        expected_prepaiid = 'Pre-paid'
        actual_prepaid = self.browser_driver.find_element_by_css_selector('.btn').text
        assert expected_prepaiid == actual_prepaid

        expected_line_status = 'Line status'
        actual_line_status = self.browser_driver.find_element_by_css_selector(
            'div.switch:nth-child(2) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_line_status == actual_line_status

        expected_open = 'Open'
        actual_open = self.browser_driver.find_element_by_css_selector('.text-success').text
        assert expected_open == actual_open

        expected_line_activation = 'Line activation'
        actual_line_activation = self.browser_driver.find_element_by_css_selector(
            'div.switch:nth-child(4) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_line_activation == actual_line_activation

        expected_roaming_line = 'Roaming line'
        actual_roaming_line = self.browser_driver.find_element_by_css_selector(
            'div.switch:nth-child(6) > div:nth-child(1) > p:nth-child(1)').text
        assert expected_roaming_line == actual_roaming_line

        expected_text = 'More'
        actual_text = self.browser_driver.find_element_by_css_selector('p.text-left:nth-child(3) > a:nth-child(1)').text
        assert expected_text == actual_text

        expected_textone = 'You are recommended to consider roaming tariffs and cost-efficient offers before travelling abroad. More'
        actual_textone = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > div.b-card.no-top-padding > div.b-card__inner > div:nth-child(6) > p').text
        assert expected_textone == actual_textone

        expected_main_balance = 'Main balance: 71.33 AZN'
        actual_main_balance = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > v-balance-simple > div > div > div > div:nth-child(2) > p.simple-p.simple-p--secondary.no-margin').text
        assert expected_main_balance == actual_main_balance

        # expected_expire_date = 'Expiry date: 06/10/2020'
        # actual_expire_date = self.browser_driver.find_element_by_css_selector('body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > v-balance-simple > div > div > div > div:nth-child(2)').text
        # assert expected_expire_date == actual_expire_date
        expected_removal_date = 'Removal date: 04/01/2021'
        actual_removal_date = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > v-balance-simple > div > div > div > div:nth-child(3) > div > p').text
        assert expected_removal_date == actual_removal_date

        expected_more = 'MORE'
        actual_more = self.browser_driver.find_element_by_css_selector(
            'body > app-root > app-entry > v-header > div > div.nagi-container > app-main > div > v-balance-simple > div > div > div > div.text-left > a').text
        assert expected_more == actual_more

        expected_tariff = 'Tariff'
        actual_tariff = self.browser_driver.find_element_by_css_selector('h3.ng-star-inserted').text
        assert expected_tariff == actual_tariff

        expected_current_tariff = 'Current tariff: Azercellim'
        actual_current_tariff = self.browser_driver.find_element_by_css_selector('.tariff').text
        assert expected_current_tariff == actual_current_tariff

        expected_second_more = 'MORE'
        actual_second_more = self.browser_driver.find_element_by_css_selector(
            'div.text-left:nth-child(4) > a:nth-child(1)').text
        assert expected_second_more == actual_second_more



    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
