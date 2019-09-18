from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class login():

     def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")

     def driver1(self):
        return self.driver


     def username_name(self,username):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)

     def password_pwd(self,password):
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login").click()


     def kslogin(self):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_id("login").click()


