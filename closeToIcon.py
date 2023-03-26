from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# driver = webdriver.Chrome(ChromeDriverManager().install())

class SauceDemo:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    def icon(self):
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        iconUser = self.driver.find_element(By.CSS_SELECTOR,".login-box > form > div:nth-child(1) >svg")
        iconUserAttribute = iconUser.get_attribute("focusable")
        print(iconUserAttribute)
        iconPassword = self.driver.find_element(By.CSS_SELECTOR,".login-box > form > div:nth-child(2) >svg")
        iconPasswordAttribute = iconPassword.get_attribute("focusable")
        print(iconPasswordAttribute)
        button = self.driver.find_element(By.CLASS_NAME,"error-button")
        button.click()
        if str(iconPasswordAttribute) != "true" and str(iconPasswordAttribute) != "true":
           
             print("test closeİcon")
        else:
            print(iconPasswordAttribute) 
            print("test case error")
              
testDemo = SauceDemo()

testDemo.icon()
        