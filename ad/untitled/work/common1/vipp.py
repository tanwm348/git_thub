from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import random
class vip():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/WoniuSales-20171128-V1.3-bin/")
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin123")
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[5]/a").click()

    #手机号码
    def customerphone(self,num):
        time.sleep(2)
        self.driver.find_element_by_id("customerphone").clear()
        self.driver.find_element_by_id("customerphone").send_keys(num)


    #会员昵称
    def customername(self,uname):
        time.sleep(2)
        self.driver.find_element_by_id("customername").clear()
        self.driver.find_element_by_id("customername").send_keys(uname)

    #小孩性别
    def childsex(self,num):
        time.sleep(1)
        se = self.driver.find_element_by_id("childsex")
        Select(se).select_by_index(num)

    #出生日期
    def childdate(self,date):
        time.sleep(1)
        self.driver.execute_script('document.getElementById("childdate").removeAttribute("readonly");')
        self.driver.find_element_by_id("childdate").clear()
        self.driver.find_element_by_id("childdate").send_keys(date)
        self.driver.find_element_by_id("creditkids").click()

    #母婴积分
    def creditkids(self,sum):
        time.sleep(1)
        self.driver.find_element_by_id("creditkids").clear()
        self.driver.find_element_by_id("creditkids").send_keys(sum)

    #童装积分
    def creditcloth(self,sum):
        time.sleep(1)
        self.driver.find_element_by_id("creditcloth").clear()
        self.driver.find_element_by_id("creditcloth").send_keys(sum)


    #新增
    def add(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[1]").click()

    #x新增失败
    def fadd(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()


    #修改
    def editBtn(self,num,uname):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr[1]/td[11]/a").click()
        time.sleep(1)
        self.driver.find_element_by_id("customerphone").clear()
        self.driver.find_element_by_id("customerphone").send_keys(num)
        time.sleep(1)
        self.driver.find_element_by_id("customername").clear()
        self.driver.find_element_by_id("customername").send_keys(uname)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='editBtn']").click()


    #查询
    def sele(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()

    #随机数
    def numm(self):
        num = random.randint(400,1000000)
        return num


    #driver
    def dri(self):
        return  self.driver