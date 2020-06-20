from selenium import webdriver
from unittest import TestCase
import unittest

unittest.TestLoader.sortTestMethodsUsing = None


class TestAzercell(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser_driver = webdriver.Firefox(
            executable_path=r'C:/Users/hasan/OneDrive/AikaDesktopFIles/Python/final-task-AikaHasanova/geckodriver')
        cls.browser_driver.implicitly_wait(60)
        cls.browser_driver.get('http://azercell.com/my/login')
        cls.browser_driver.find_element_by_css_selector('li.b-nav__list:nth-child(3) > a:nth-child(1)').click()

    def test_mobile_number_not_filled(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_input_value = ''
        expected_warning = 'Enter the number'
        actual_input_value = self.browser_driver.find_element_by_css_selector('#mat-input-1').get_attribute('value')
        assert expected_input_value == actual_input_value
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-0').text
        assert expected_warning == actual_warning

    def test_enter_number_without_prefix(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('8179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_warning = 'The number should consist of 9 digits'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-3').text
        assert expected_warning == actual_warning

    def test_enter_short_number(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('51817900')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_warning = 'The number should consist of 9 digits'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-3').text
        assert expected_warning == actual_warning

    # Unable to locate element: #mat-error-3 (it does not give an error msg in website)
    def test_enter_long_number(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('0518179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_warning = 'The number should consist of 9 digits'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-3').text
        assert expected_warning == actual_warning

    def test_login_with_registered_user_using_correct_credentials(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('518179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-2').send_keys('a12345')
        self.browser_driver.find_element_by_css_selector('.btn').click()
        expected_number = '+994518179001'
        actual_number = self.browser_driver.find_element_by_css_selector(
            'li.b-nav__lang:nth-child(2) > span:nth-child(2)').text
        assert expected_number == actual_number
        self.browser_driver.delete_all_cookies()
        self.browser_driver.get('http://azercell.com/my/login')

    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
        # self.browser_driver.find_element_by_css_selector('#mat-input-2').click
        # expected_input = ''
        # actual_input=self.browser.find_element_by_css_selector('#mat-input-1').get_attribute('value')
        # expected_input == actual_input
