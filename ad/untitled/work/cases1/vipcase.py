from work.common1.vipp import *

vip1 = vip()
driver = vip1.dri()
num = vip1.numm()

#新增成功
def add1():

    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l1 = driver.find_element_by_xpath("//*[@id='creditkids']").text
    if l1 == "":
        print("会员新增测试成功")
    else:
        print("会员新增测试失败")

#电话号码为空
def dhhm():
    vip1.customerphone("")
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.add()
    time.sleep(1)
    l2 = driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div").text
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    if l2 == "请输入客户的电话号码.":
        print("电话号码为空测试成功")
    else:
        print("电话号码为空测试成功")

#会员昵称为空
def hync():
    vip1.customerphone(num)
    vip1.customername("")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.add()
    time.sleep(1)
    l3 = driver.find_element_by_id("customername").text
    print(l3)
    if l3 == "":
        print("会员昵称为空测试成功")
    else:
        print("会员昵称为空测试失败")

#出生日期为空
def datee():
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    vip1.customerphone(num)
    vip1.customername("张三仨")
    vip1.childsex(1)
    vip1.childdate("")
    vip1.add()
    time.sleep(1)
    l4 = driver.find_element_by_xpath("//*[@id='creditkids']").text
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    if l4 == "":
        print("出生日期为空测试成功")
    else:
        print("出生日期为空测试失败")

#母婴积分为空
def myjf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids("")
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l5 = driver.find_element_by_xpath("//*[@id='creditkids']").text
    if l5 == "":
        print("母婴积分为空测试成功")
    else:
        print("母婴积分为空测试失败")

#童装积分为空
def tzjf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth("")
    vip1.add()
    time.sleep(1)
    l6 = driver.find_element_by_id("creditcloth").text
    # driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    if l6 == "":
        print("童装积分为空测试成功")
    else:
        print("童装积分为空测试失败")


#输入21位电话号码
def fdhhm():
    vip1.customerphone("123456789123456789123")
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l7 = driver.find_element_by_id("customerphone").get_attribute("value")
    print(l7)
    if l7 == "123456789123456789123":
        print("电话号码输入21位测试成功")
    else:
        print("电话号码输入21位测试失败")

#电话号码输入字母
def dhhmzm():
    vip1.customerphone("aaaaa")
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l8 = driver.find_element_by_id("customerphone").get_attribute("value")
    print(l8)
    if l8 == "aaaaa":
        print("电话号码输入字母测试成功")
    else:
        print("电话号码输入字母测试失败")

#电话号码输入特殊字符
def dhhmtxzf():
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    vip1.customerphone("??????")
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l9 = driver.find_element_by_id("customerphone").get_attribute("value")
    print(l9)
    if l9 == "??????":
        print("电话号码输入特殊字符测试成功")
        driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    else:
        print("电话号码输入特特殊字符测试失败")


#输入21位会员昵称
def fhync():
    vip1.customerphone(num)
    vip1.customername("abcdefghijklmnopq")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    # driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
    vip1.creditkids(1)
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l10 = driver.find_element_by_id("customername").get_attribute("value")
    if l10 == "abcdefghijklmnopq":
        print("会员昵称输入21位字符测试成功")
    else:
        print("会员昵称输入21位字符测试失败")


#母婴积分输入21个数字
def fmyjf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    time.sleep(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids("123456789123456789123")
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l5 = driver.find_element_by_xpath("//*[@id='creditkids']").get_attribute("value")
    if l5 == "123456789123456789123":
        print("母婴积分输入21个数字测试成功")
    else:
        print("母婴积分输入21个数字测试失败")

#母婴积分输入字母
def myzfzm():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids("aaa")
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l11 = driver.find_element_by_xpath("//*[@id='creditkids']").get_attribute("value")
    if l11 == "aaa":
        print("母婴积分输入字母测试成功")
    else:
        print("母婴积分输入字母测试失败")

#母婴积分输入特殊字符
def myjfzf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids("???")
    vip1.creditcloth(1)
    vip1.add()
    time.sleep(1)
    l11 = driver.find_element_by_xpath("//*[@id='creditkids']").get_attribute("value")
    if l11 == "???":
        print("母婴积分输入特殊字符空测试成功")
    else:
        print("母婴积分输入特殊字符测试失败")

#童装积分输入21个数字
def ftzjf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth("123456789123456789123")
    vip1.add()
    time.sleep(1)
    l12 = driver.find_element_by_id("creditcloth").get_attribute("value")
    if l12 == "123456789123456789123":
        print("童装积分输入21个数字测试成功")
    else:
        print("童装积分输入21个数字测试失败")

#童装积分输入字母
def tzzfzm():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth("aaa")
    vip1.add()
    time.sleep(1)
    l13 = driver.find_element_by_id("creditcloth").get_attribute("value")
    if l13 == "aaa":
        print("童装积分输入字母测试成功")
    else:
        print("童装积分输入字母测试失败")

#童装积分输入特殊字符
def tzjfzf():
    vip1.customerphone(num)
    vip1.customername("张三三")
    vip1.childsex(1)
    vip1.childdate("2008-08-08")
    vip1.creditkids(1)
    vip1.creditcloth("???")
    vip1.add()
    time.sleep(1)
    l14 = driver.find_element_by_id("creditcloth").et_attribute("value")
    if l14 == "???":
        print("童装积分输入特殊字符空测试成功")
    else:
        print("童装积分输入特殊字符测试失败")


# 修改
def xg():
   time.sleep(1)
   vip1.editBtn(num,"啊啊啊啊啊")
   time.sleep(1)
   l15 = driver.find_element_by_class_name("bootbox-body").text
   driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button").click()
   if l15 == "修改客户信息成功.":
     print("会员管理修改测试成功")


   else:
     print("会员管理修改测试失败")



#查询
def cx():
    time.sleep(1)
    vip1.sele()
    time.sleep(2)
    l16 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/table/tbody/tr/td[11]/a").text
    if l16 == "修改":
        print("会员管理查询测试成功")
    else:
        print("会员管理查询测试失败")


if __name__ == '__main__':

    add1()
    dhhm()
    hync()
    datee()
    myjf()
    tzjf()
    fdhhm()
    dhhmzm()
    dhhmtxzf()
    fmyjf()
    myzfzm()
    myjfzf()
    ftzjf()
    tzzfzm()
    tzzfzm()
    # fhync()
    # xg()
    # cx()