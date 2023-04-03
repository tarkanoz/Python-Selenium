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

class TestWrongLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_wrongLogin(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1280, 680)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"
    self.driver.close()
  
