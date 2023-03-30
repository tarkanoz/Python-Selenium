from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import random
from PIL import Image
options = Options()
class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(random.randint(0,1000))
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):   
         self.driver.quit() 
    def test_login_empty(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        
        if usernameInput.text == "" and passwordInput.text == "":
            loginBtn = self.driver.find_element(By.ID,"login-button")
            loginBtn.click()  
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text =="Epic sadface: Username is required"
    def test_password_empty(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")  
        if passwordInput.text == "":
            loginBtn = self.driver.find_element(By.ID,"login-button")
            loginBtn.click()  
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text =="Epic sadface: Password is required"    
    def test_user_wrong(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("locked_out_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text =="Epic sadface: Sorry, this user has been locked out."
    def test_success_login(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        url = self.driver.current_url
        if str(url) =="https://www.saucedemo.com/inventory.html":
            all_products = self.driver.find_elements(By.XPATH,"//div[@class='inventory_item']")
            assert len(all_products) == 6
    def test_icon(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password") 
        if usernameInput.text == "" and passwordInput.text == "":
            loginBtn = self.driver.find_element(By.ID,"login-button")
            loginBtn.click()
        sleep(5)     
        user_icon = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg") 
        password_icon = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        if user_icon and password_icon:
            alert_icon = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg") 
            alert_icon.click() 
        sleep(5)          
        # assert user_icon.is_enabled() and password_icon.is_enabled() == False
    @pytest.mark.skip    
    def test_socialMedia_icon(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        icon_twiiter = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[1]/a")
        icon_twiiter.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)
        urlTwitter = self.driver.current_url
        assert str(urlTwitter) == "https://twitter.com/saucelabs"
        sleep(5)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        icon_facebook = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[2]/a")
        icon_facebook.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        urlFacebook = self.driver.current_url
        assert str(urlFacebook) == "https://www.facebook.com/saucelabs"
        sleep(5)
       
        self.driver.switch_to.window(self.driver.window_handles[0])
        # icon_linkedin = self.driver.find_element(By.XPATH,"//*[@id='page_wrapper']/footer/ul/li[3]/a")
        # icon_linkedin.click()
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # urlLinkedin = self.driver.current_url
        # assert str(urlLinkedin) == "https://www.linkedin.com/company/sauce-labs/"
        # sleep(5)
    
    def test_toCart(self):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        cartButton = self.driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a")
        cartButton.click()
        cartUrl = self.driver.current_url
        self.driver.save_screenshot(f"test_toCart-{str(cartUrl)}.png")
        self.driver.save_screenshot(f"{self.folderPath}+image.png")
        # image = Image.open("image.png")
        # image.show
        sleep(2)
        assert str(cartUrl) == "https://www.saucedemo.com/cart.html"
    @pytest.mark.parametrize("firstnametext,lastnametext,zipcodetext,result",[("aa","aa","aa","aa"),("11","11","11","11"),("a1","a1","a1","a1")])    
    def test_checkoutInput(self,firstnametext,lastnametext,zipcodetext,result):
        self.waitDriver((By.ID,"user-name"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")  
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID,"password"),10) 
        passwordInput =self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        cartButton = self.driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a")
        cartButton.click()
        checkoutButton = self.driver.find_element(By.CSS_SELECTOR,"#checkout")
        checkoutButton.click()
        firstname_input = self.driver.find_element(By.CSS_SELECTOR,"#first-name")
        lastname_input = self.driver.find_element(By.CSS_SELECTOR,"#last-name")
        zipcode_input = self.driver.find_element(By.CSS_SELECTOR,"#postal-code")
        firstname_input.send_keys(firstnametext)
        lastname_input.send_keys(lastnametext)
        zipcode_input.send_keys(zipcodetext)
        sleep(5)
        firstname_value =firstname_input.get_attribute("value")
        lastname_value = lastname_input.get_attribute("value")
        zipcode_value = zipcode_input.get_attribute("value")
        self.driver.save_screenshot(f"{self.folderPath}+/test_invalid_login-{firstname_value}-{lastname_value}-{zipcode_value}.png")
        self.driver.save_screenshot(f"{self.folderPath}+image.png")
        assert firstname_value and lastname_value and zipcode_value  == result



    def waitDriver(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) 
        