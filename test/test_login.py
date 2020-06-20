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

    def test_mobile_number_not_filled(self):  # passed
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_input = ''
        expected_warning = 'Enter the number'
        actual_input = self.browser_driver.find_element_by_css_selector('#mat-input-1').get_attribute('value')
        assert expected_input == actual_input
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-0').text
        assert expected_warning == actual_warning

    def test_enter_number_without_prefix(self):  # passed
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('8179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_warning = 'The number should consist of 9 digits'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-3').text
        assert expected_warning == actual_warning

    def test_enter_short_number(self):  # passed
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

    def test_enter_number_with_wrong_prefix(self):  # AssertionError
        # self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('058179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_warning = 'The number is wrong'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-error-2').text
        assert expected_warning == actual_warning

    def test_none_numeric_symbols_to_mobile_number_field(self):  # AssertionError
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('51EiA9@$1')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        expected_input = 'value'
        actual_input = self.browser_driver.find_element_by_css_selector('#mat-input-1').get_attribute('value')
        assert expected_input == actual_input
        self.browser_driver.delete_all_cookies()
        self.browser_driver.get('http://azercell.com/my/login')

    def test_password_not_filled(self):  # passed
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('518179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        self.browser_driver.find_element_by_css_selector('div.row:nth-child(5)').click()
        expected_input_password = ''
        expected_warning_password = 'Enter the password'
        actual_input_password = self.browser_driver.find_element_by_css_selector('#mat-input-2').get_attribute('value')
        assert expected_input_password == actual_input_password
        actual_warning_password = self.browser_driver.find_element_by_css_selector('#mat-error-1').text
        assert expected_warning_password == actual_warning_password

    def test_fill_password_field_alphanumeric_special_characters(self):  # passed
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('518179001')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-2').send_keys('a1!@2A')
        expected_password = "a1!@2A"
        actual_password = self.browser_driver.find_element_by_css_selector('#mat-input-2').get_attribute('value')
        assert expected_password == actual_password

    def try_to_login_with_not_registered_number(self):
        self.browser_driver.get('http://azercell.com/my/login')
        self.browser_driver.find_element_by_css_selector('#mat-input-1').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-1').send_keys('518951066')
        self.browser_driver.find_element_by_css_selector('#mat-input-2').click()
        self.browser_driver.find_element_by_css_selector('#mat-input-2').send_keys('123456a')
        self.browser_driver.find_element_by_css_selector('.btn').click()
        expected_warning = 'Wrong password'
        actual_warning = self.browser_driver.find_element_by_css_selector('#mat-input-2').text
        assert expected_warning == actual_warning

    def test_login_with_registered_user_using_correct_credentials(self):  # passed
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
