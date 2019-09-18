from day03.common.loginmodel import *
class Announcements1():
    def __init__(self):
        self.log = login()
        self.log.kslogin()
        time.sleep(1)
        self.driver = self.log.driver1()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()

    #编号栏
    def number(self,num):
        time.sleep(2)
        self.driver.find_element_by_id("noticeid").clear()
        self.driver.find_element_by_id("noticeid").send_keys(num)

    #创建者栏
    def creator(self,str):
        time.sleep(1)
        self.driver.find_element_by_id("creator").clear()
        self.driver.find_element_by_id("creator").send_keys(str)

    #范围栏
    def scope(self,num1):
        time.sleep(1)
        self.driver.find_element_by_id("scope").click()
        se = self.driver.find_element_by_id("scope")
        Select(se).select_by_index(num1)


    #过期日期
    def  ExpirationDate(self,date):
        time.sleep(1)
        self.driver.find_element_by_id("expireddate").clear()
        self.driver.find_element_by_id("expireddate").send_keys(date)


    #标题栏
    def HeadLine(self,headlines):
        time.sleep(1)
        self.driver.find_element_by_id("headline").clear()
        self.driver.find_element_by_id("headline").send_keys(headlines)


    #内容栏
    def Content(self,con):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys("")
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys(con)


    #新增
    def add(self):
        time.sleep(1)
        self.driver.find_element_by_id("add").click()

    #编辑
    def compile(self,hl):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[2]/tbody/tr[1]/td[5]/label[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id("scope").click()
        se = self.driver.find_element_by_id("scope")
        Select(se).select_by_index(1)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/div/div/iframe").send_keys("a")
        self.driver.find_element_by_id("edit").click()

    #搜索
    def search(self,he):
        time.sleep(1)
        self.driver.find_element_by_id("headline").clear()
        self.driver.find_element_by_id("headline").send_keys(he)
        self.driver.find_element_by_id("search").click()


    #重置
    def reset(self):
        time.sleep(1)
        self.driver.find_element_by_id("reset").click()


    #删除确认
    def dele(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[2]/tbody/tr[1]/td[5]/label[2]").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()


