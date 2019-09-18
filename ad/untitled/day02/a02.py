from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
driver.get("http://localhost:8080/WoniuSales-20171128-V1.3-bin/")


def login(a = "admin",b = "admin123",c = "0000"):
    driver.find_element_by_id("username").send_keys(a)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(b)
    driver.find_element_by_id("verifycode").send_keys(c)
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    time.sleep(2)
    l1 = driver.find_element_by_link_text("注销").text
    if l1 == "注销":
        print("登陆测试成功")

    else:
        print("登陆测试失败")

def vipxz():
    login()
    driver.find_element_by_link_text("会员管理").click()
    time.sleep(2)
    a = driver.find_element_by_id("childsex")
    Select(a).select_by_value("女")
    driver.execute_script('document.getElementById("childdate").removeAttribute("readonly");')
    driver.find_element_by_id("childdate").clear()
    driver.find_element_by_id("childdate").send_keys("2008-08-08")
    driver.find_element_by_name().clear()

#批量导入
def pldr():
    login()
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[3]/a").click()
    driver.find_element_by_xpath("//*[@id='batchfile']").send_keys("C:\\Users\\Administrator\\Desktop\\销售出库单-2019-Test.xls")


# vipxz()
pldr()