from selenium import webdriver
import time
class login2():

     def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")


     def driver(self):
         return self.driver

     def logining(self,username,password):

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login").click()
        try:
            time.sleep(1)
            expected = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/a[5]").text
            return expected
        except:
            time.sleep(1)
            expected = self.driver.find_element_by_id("msg").text
            return expected

     def rapid(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_id("login").click()
