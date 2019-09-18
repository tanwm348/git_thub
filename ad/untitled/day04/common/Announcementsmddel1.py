
from day04.cases.cases登陆 import *
import time

class announcementss():
    def __init__(self):
        self.ad = login2()
        self.driver = self.ad.driver
        self.ad.rapid()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()






    #新增
    def add(self,num,creator,headline,content):
        time.sleep(2)
        #编号栏
        self.driver.find_element_by_id("noticeid").send_keys(num)
        #创建者栏
        self.driver.find_element_by_id("creator").clear()
        self.driver.find_element_by_id("creator").send_keys(creator)
        #标题栏
        self.driver.find_element_by_id("headline").clear()
        self.driver.find_element_by_id("headline").send_keys(headline)
        #内容栏
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").click()
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys(content)
        self.driver.find_element_by_id("add").click()
        cs1 = self.driver.find_element_by_id("msg").text
        cs1 = cs1[0:11:1]
        return cs1

     #编辑
    def compi(self,creator,headline,content):
        time.sleep(4)

        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[2]/tbody/tr[1]/td[5]/label[1]").click()

        #创建者栏
        self.driver.find_element_by_id("creator").clear()
        self.driver.find_element_by_id("creator").send_keys(creator)
        #标题栏
        self.driver.find_element_by_id("headline").clear()
        self.driver.find_element_by_id("headline").send_keys(headline)
        #内容栏
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").click()
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys(content)
        self.driver.find_element_by_id("edit").click()
        time.sleep(2)
        cs2 = self.driver.find_element_by_id("msg").text
        cs2 = cs2[0:11:1]
        return cs2

    #搜索
    def search1(self,headline):
        self.driver.find_element_by_id("headline").send_keys(headline)
        self.driver.find_element_by_id("search").click()
        cs4 = self.driver.find_element_by_id("totalRecord").text
        return cs4


    #重置
    def cz(self):
        self.driver.find_element_by_id("reset").click()
        cs5 = self.driver.find_element_by_id("headline").text
        return cs5


    #删除
    def dele(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[2]/tbody/tr[1]/td[5]/label[2]").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        cs6 = self.driver.find_element_by_id("msg").text
        cs6 = cs6[0:11:1]
        return cs6