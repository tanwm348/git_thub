from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import random
driver = webdriver.Firefox()
driver.get("http://localhost:8080/WoniuSales-20171128-V1.3-bin/")

#测试登陆成功
def login(a = "admin",b = "admin123",c = "0000"):
    driver.find_element_by_id("username").send_keys(a)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(b)
    driver.find_element_by_id("verifycode").send_keys(c)
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    driver.implicitly_wait(2)
    l1 = driver.find_element_by_link_text("注销").text
    if l1 == "注销":
        print("登陆测试成功")

    else:
        print("登陆测试失败")



#商品出库
def spck(a):
    driver.find_element_by_link_text("销售出库").click()
    driver.find_element_by_id("barcode").send_keys(a)

    driver.find_element_by_css_selector("div.container:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(3)").click()
    l8 = driver.find_element_by_id("tempbuyprice").text
    driver.find_element_by_id("submit").click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(2)

    l9 =driver.find_element_by_id("totalbuycount").text
    if l9 =="0":
        print("销售出库测试成功")
        return l8
    else:
        print("销售出库测试失败")





#商品入库
def sprk(a):
    login()
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[2]/a").click()
    time.sleep(2)
    s = driver.find_element_by_id("batchname")
    Select(s).select_by_index(2)
    driver.find_element_by_id("goodsserial").send_keys(a)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[1]/div[4]").click()
    driver.find_element_by_id("quantity").send_keys(1)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div/input").click()
    driver.switch_to.alert.accept()
    l5 = driver.find_element_by_id("message").get_attribute("value")
    if l5 == "成功：商品入库成功，请继续录入下一笔":
        print("商品入库测试成功")
    else:
        print("商品入库测试失败")



#会员管理新增
def vipxz():
    driver.find_element_by_link_text("会员管理").click()
    driver.implicitly_wait(3)
    a = random.randint(400,1000000)
    driver.find_element_by_id("customerphone").send_keys(a)
    driver.find_element_by_id("customername").clear()
    driver.find_element_by_id("customername").send_keys("张三")
    driver.find_element_by_id("childdate").click()
    driver.find_element_by_xpath("/html/body/div[6]/div[3]/table/thead/tr[1]/th[2]").click()
    for i in range(11):
        driver.find_element_by_xpath("/html/body/div[6]/div[4]/table/thead/tr/th[1]").click()
    driver.find_element_by_xpath("/html/body/div[6]/div[4]/table/tbody/tr/td/span[8]").click()
    driver.find_element_by_xpath("/html/body/div[6]/div[3]/table/tbody/tr[2]/td[6]").click()
    driver.find_element_by_id("creditkids").send_keys(2)
    driver.find_element_by_id("creditcloth").send_keys(2)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[1]").click()
    l6 = driver.find_element_by_xpath("//*[@id='creditkids']").text
    if l6 == "":
        print("会员管理新增测试成功")
    else:
        print("会员管理新增测试失败")


#会员管理修改
def vipxg():
    driver.find_element_by_link_text("会员管理").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr[2]/td[11]/a").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//*[@id='editBtn']").click()
    l7 = driver.find_element_by_class_name("bootbox-body").text
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    if l7 == "修改客户信息成功.":
        print("会员管理修改测试成功")


    else:
        print("会员管理修改测试失败")



#会员管理查询
def vipcx():
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()
    l8 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr/td[11]/a").text
    if l8 == "修改":
        print("会员管理查询测试成功")
    else:
        print("会员管理查询测试失败")


#批量导入
def pldr():
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[3]/a").click()
    driver.find_element_by_xpath("//*[@id='batchfile']").send_keys("C:\\Users\\Administrator\\Desktop\\销售出库单-2019-Test.xls")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div/input").click()
    time.sleep(2)
    o = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div").text
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/button").click()

    if o == "你已经导入本批次，请勿重复导入.":
        print("批量导入测试成功")
    else:
        print("批量导入测试失败")

#销售报表
def xsbb():
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[6]/a").click()

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[1]").click()#当日明细

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[2]").click()#七日明细

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[3]").click()#当月明细
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[1]/tbody/tr[1]/td[13]/input").click()#退货
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[2]").click()# 确认
    driver.implicitly_wait(3)
    l6 = driver.find_element_by_id("mysell-today").get_attribute("value")
    if l6 == "0元":
        print("退货测试成功")

    else:
        print("退货测试失败")

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[4]").click()
    l7 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[2]/tbody/tr[1]/td[9]").text
    if l7 == "现金":
        print("当日摘要测试成功")
    else:
        print("当日摘要测试失败")

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[5]").click()
    l7 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[2]/tbody/tr[1]/td[9]").text
    if l7 == "现金":
        print("七日摘要测试成功")
    else:
        print("七日摘要测试失败")


    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[6]").click()
    l7 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[2]/tbody/tr[1]/td[9]").text
    if l7 == "现金":
        print("当月摘要测试成功")
    else:
        print("当月摘要测试失败")


    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[7]").click()
    l8 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[3]/tbody/tr/td[2]").text
    if l8 == "1件":
        print("当月按类汇总测试成功")
    else:
        print("当月按类汇总测试失败")

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[8]").click()
    l8 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[3]/tbody/tr/td[2]").text
    if l8 == "1件":
        print("当年按类汇总测试成功")
    else:
        print("当年按类汇总测试失败")


    driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[9]").click()
    l9 = driver.find_element_by_xpath("/html/body/div[4]/div[3]/table[4]/tbody/tr[2]/td[8]").text
    if int(l9) == 0:
        print("退货记录测试成功")
    else:
        print("退货记录测试失败")


    l1 = driver.find_element_by_id("totalsell-month").get_attribute("value")#当前金额
    time.sleep(2)
    l2 = spck(6955203659750)
    time.sleep(2)
    driver.find_element_by_link_text("销售报表").click()
    l3 = driver.find_element_by_id("totalsell-month").get_attribute("value")
    time.sleep(2)
    l1= l1.replace("元","",1)
    l3 =l3.replace("元","",1)
    l2 =int(float(l2))
    l1 = int(l1)
    l3 = int(l3)
    print(l1)
    print(l2)
    print(l3)
    if l3 == l2 + l1:
        print("当月销售总额测试成功")
    else:
        print("当月销售总额测试失败")




sprk("ME42302") #商品入库
vipxz() #会员管理新增
vipxg()# 会员管理修改
vipcx() #会员管理查询
pldr() #批量导入

xsbb()#销售报表