import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Testitems:
    def test_items(self, browser):
        button = browser.find_element(By.CSS_SELECTOR,".btn-add-to-basket" )
        assert button




