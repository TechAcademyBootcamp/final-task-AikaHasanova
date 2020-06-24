from selenium import webdriver
from unittest import TestCase
import unittest


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

    def test_cancel_line_deactivation(self):#M004
        self.browser_driver.find_element_by_css_selector(
            '#mat-slide-toggle-1 > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
        self.browser_driver.find_element_by_css_selector('button.mat-button:nth-child(1) > span:nth-child(1)').click()
        assert self.browser_driver.find_element_by_class_name('mat-slide-toggle-label')

    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
