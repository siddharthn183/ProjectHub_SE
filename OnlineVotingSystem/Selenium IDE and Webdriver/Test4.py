# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest4():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test4(self):
    self.driver.get("http://127.0.0.1:5501/Home/index.html")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Login →").click()
    self.driver.find_element(By.LINK_TEXT, "About us").click()
  