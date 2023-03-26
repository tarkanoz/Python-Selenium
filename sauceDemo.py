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

    def loginEmpty(self):
   
      print("benim adım selenium")
      userName = self.driver.find_element(By.ID,"user-name")
      password = self.driver.find_element(By.ID,"password")
      usernameText = userName.text
      passwordText = password.text
      if usernameText == "" and passwordText =="":
          loginButton = self.driver.find_element(By.ID,"login-button")
          loginButton.click()
          errorArea = self.driver.find_element(By.CLASS_NAME,"error-message-container")
          print("text : ",errorArea.text)
      if errorArea.text == "Epic sadface: Username is required":
           print("test success")
      else:
          print("test case error")
    def passwordEmpty(self):
        userName = self.driver.find_element(By.ID,"user-name")
        password = self.driver.find_element(By.ID,"password")
        userName.send_keys("kullanıcı") 
        passwordText = password.text
        if   passwordText == "":
          loginButton = self.driver.find_element(By.ID,"login-button")
          loginButton.click()
          errorArea = self.driver.find_element(By.CLASS_NAME,"error-message-container")
          print("text : ",errorArea.text)
        if errorArea.text =="Epic sadface: Password is required":
            print("test succs passwordEmpty")
        else:
            print("test case error")    
    def errorUser(self):
        userName = self.driver.find_element(By.ID,"user-name")
        password = self.driver.find_element(By.ID,"password")
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorArea = self.driver.find_element(By.CLASS_NAME,"error-message-container")
        print("text : ",errorArea.text)
        if errorArea.text == "Epic sadface: Sorry, this user has been locked out.":
            print("test success erroruSER")
        else:
            print("test case error")    

    def seccessLogin(self):
        userName = self.driver.find_element(By.ID,"user-name")
        password = self.driver.find_element(By.ID,"password")
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        get_url = self.driver.current_url
        print("The current url is:"+str(get_url))
        if str(get_url) == "https://www.saucedemo.com/inventory.html":
              print("test success login")
        else:
            print("test case error")    
        productLen = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print("product length :",len(productLen))
        if str(len(productLen)) == "6":
              print("test success product length")
        else:
            print("test case error")  



testDemo = SauceDemo()

# testDemo.loginEmpty()
# testDemo.passwordEmpty()
# testDemo.errorUser()
testDemo.seccessLogin()
testDemo.driver.close()
  