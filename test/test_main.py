from selenium import webdriver
from unittest import TestCase
import unittest


class TestAzercell(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser_driver = webdriver.Firefox(
            executable_path=r'C:/Users/hasan/OneDrive/AikaDesktopFIles/Python/final-task-AikaHasanova/geckodriver')
        cls.browser_driver.implicitly_wait(10)
        cls.browser_driver.get('http://azercell.com/my/login')