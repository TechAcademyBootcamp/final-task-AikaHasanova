from selenium import webdriver
from unittest import TestCase
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
        cls.browser_driver.find_element_by_css_selector('a.sidenav__element:nth-child(3)').click()
        sleep(1)

    def test_language_compatibility_between_VCC_and_redirected_URL_of_tariff(self):
        self.browser_driver.find_element_by_css_selector('app-tariff-card.scroll-card:nth-child(2) > div:nth-child(1) > div:nth-child(4) > a:nth-child(3) > span:nth-child(1)').click()






    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
