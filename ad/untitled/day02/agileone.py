from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")

def login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_id("login").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()




def add():
    login()
    driver.find_element_by_id("noticeid").click()
    driver.find_element_by_id("noticeid").send_keys("1")

    driver.find_element_by_id("creator").click()
    driver.find_element_by_id("creator").send_keys("admin")



    driver.find_element_by_id("headline").click()
    driver.find_element_by_id("headline").send_keys("我是谁")

    driver.find_element_by_xpath("//div/iframe").send_keys("wooooo")



    # driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").click()
    # driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys("我从哪里来,我要到哪里去")

    driver.find_element_by_id("add").click()


    for i in range(5):
        driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[1]").click()
    driver.implicitly_wait(5)
    a = driver.find_element_by_id("msg").text
    print(a)


add()