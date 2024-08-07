import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import logging

class Automation(unittest.TestCase): 

    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_a_success_login(self):
        # steps
        driver = self.browser # buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID, "login-button").click()
    
    def test_failed_login(self):
        # steps
        driver = self.browser # buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("regular_user") # isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_error = driver.find_element(By.TAG_NAME, "form").text # find element by tag name
        self.assertEqual(response_error, 'Epic sadface: Username and password do not match any user in this service')

    def test_succes_logout(self):
        # steps
        driver = self.browser # buka web browser
        Automation.test_a_success_login(self) # call login function
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click() # open sidebar menu
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click() # click 

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()