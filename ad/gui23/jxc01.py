from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://localhost:8080/WoniuSales-20171128-V1.3-bin/")

#测试登陆成功
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

#测试输入错误用户名
def fuser(a,b):
    driver.find_element_by_id("username").send_keys(a)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(b)
    driver.find_element_by_id("verifycode").send_keys("0000")
    l2 = driver.find_element_by_xpath("/html/body/div[4]/div/form/div[1]/span").text
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    if l2 == "你还没有登录，请先登录。":
        print("测试输入错误用户名成功")

    else:
       print("测试输入错误用户名失败")

#测试输入错误密码
def fpwd(a,b,c):
    driver.find_element_by_id("username").send_keys(a)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(b)
    driver.find_element_by_id("verifycode").send_keys(c)
    l3 = driver.find_element_by_xpath("/html/body/div[4]/div/form/div[1]/span").text
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    print(l3)
    if l3 == "你还没有登录，请先登录。":
        print("测试输入错误密码成功")

    else:
       print("测试输入错误密码失败")

#测试输入错误验证码
def fyzm(a,b,c):
    driver.find_element_by_id("username").send_keys(a)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(b)
    driver.find_element_by_id("verifycode").send_keys(c)
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    l4 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div").text
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/button").click()
    print(l4)
    if l4 == "验证码失效，请重新输入.":
        print("测试输入错误验证码成功")

    else:
       print("测试输入错误验证码失败")

#销售出库
def spck(a):
    login()
    driver.find_element_by_link_text("销售出库").click()
    driver.find_element_by_id("barcode").send_keys(a)
    driver.find_element_by_css_selector("div.container:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(3)").click()
    driver.find_element_by_id("submit").click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    l9 =driver.find_element_by_id("totalbuycount").text
    if l9 =="0":
        print("销售出库测试成功")
    else:
        print("销售出库测试失败")

#spck(6955203636348)










#商品入库
def sprk(a,b):
    login()
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[2]/a").click()
    time.sleep(2)
    driver.find_element_by_id("goodsserial").send_keys(a)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[1]/div[4]").click()
    driver.find_element_by_id("quantity").send_keys(b)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div/input").click()
    driver.switch_to.alert.accept()
    l5 = driver.find_element_by_xpath("//*[@id='barcode']").text
    if l5 == "":
        print("商品入库测试成功")
    else:
        print("商品入库测试失败")




#会员管理新增
def vipxz(a,b,c=2,d=2):
    driver.find_element_by_link_text("会员管理").click()
    time.sleep(2)
    driver.find_element_by_id("customerphone").send_keys(a)
    driver.find_element_by_id("customername").clear()
    driver.find_element_by_id("customername").send_keys(b)
    driver.find_element_by_id("creditkids").send_keys(c)
    driver.find_element_by_id("creditcloth").send_keys(d)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[1]").click()
    l6 = driver.find_element_by_xpath("//*[@id='creditkids']").text
    if l6 == "":
        print("会员管理新增测试成功")
    else:
        print("会员管理新增测试失败")



#会员管理修改
def vipxg():

    driver.find_element_by_link_text("会员管理").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr[2]/td[11]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='editBtn']").click()
    l7 = driver.find_element_by_class_name("bootbox-body").text
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    if l7 == "修改客户信息成功.":
        print("会员管理修改测试成功")


    else:
        print("会员管理修改测试失败")



#会员管理查询
def vipcx():
    # driver.find_element_by_link_text("会员管理").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]").click()
    l8 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr/td[11]/a").text
    if l8 == "修改":
        print("会员管理查询测试成功")
    else:
        print("会员管理查询测试失败")




# fuser("admin1","admin123")#输入错误用户名
# fpwd("admin","admin","0000")#输入错误密码
# fyzm("admin","admin123","00000")#输入错误验证码



# sprk("M7S1787D",b=1) #商品入库
# vipxz(337,"张三") #会员管理新增
# vipxg()# 会员管理修改
# vipcx() #会员管理查询
