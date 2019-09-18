from day03.common.Announcements import *
ann = Announcements1()
driver = ann.driver

#新增成功
def tadd():
    ann.number(1)
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs1 = driver.find_element_by_id("msg").text
    cs1 = cs1[0:3:1]
    if cs1 == "成功啦":
        print("新增测试成功")
    else:
        print("新增测试失败")

#编号为空
def kbh():
    ann.number("")
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs2 = driver.find_element_by_id("msg").text
    cs2 = cs2[0:3:1]
    if cs2 == "成功啦":
        print("编号为空测试成功")
    else:
        print("编号为空测试失败")

#创建者为空
def kcjz():
    ann.number("")
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs3 = driver.find_element_by_id("msg").text
    cs3 = cs3[0:3:1]
    if cs3 == "成功啦":
        print("创建者为空测试成功")
    else:
        print("创建者为空测试失败")

#过期日期为空
def date():
    ann.number("1")
    ann.creator("admin")
    ann.scope(0)
    ann.ExpirationDate("")
    ann.HeadLine("刘露")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs4 = driver.find_element_by_id("msg").text
    cs4 = cs4[0:3:1]
    if cs4 == "出错啦":
        print("过期日期为空测试成功")
    else:
        print("过期日期为空测试失败")


#范围为空
def kfw():
    ann.number("1")
    ann.creator("admin")
    ann.scope(0)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs5 = driver.find_element_by_id("msg").text
    cs5 = cs5[0:3:1]
    if cs5 == "出错啦":
        print("范围为空测试成功")
    else:
        print("范围为空测试失败")

#标题为空
def kbt():
    time.sleep(1)
    ann.number("1")
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("")
    ann.Content("刘露是什么")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs6 = driver.find_element_by_id("msg").text
    cs6 = cs6[0:3:1]
    if cs6 == "出错啦":
        print("标题为空测试成功")
    else:
        print("标题为空测试失败")

#空内容
def knr():
    time.sleep(1)
    ann.number("1")
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs7 = driver.find_element_by_id("msg").text
    cs7 = cs7[0:3:1]
    if cs7 == "成功啦":
        print("内容为空测试成功")
    else:
        print("内容空测试失败")


#编号输入字母
def bhzm():
    time.sleep(1)
    ann.number("aa")
    ann.creator("admin")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs8 = driver.find_element_by_id("msg").text
    cs8 = cs8[0:3:1]
    if cs8 == "出错啦":
        print("编号输入字母测试成功")
    else:
        print("编号输入字母应给出提示并报错")

#创建者输入31个字符
def ccjzf():
    time.sleep(1)
    ann.number("1")
    for i in range(30):
        ann.creator("哈")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs9 = driver.find_element_by_id("msg").text
    cs9 = cs9[0:3:1]
    if cs9 == "成功啦":
        print("输入31个字符测试成功")
    else:
        print("输入31个字符测试失败")

#年输入5位数,其他正常
def gdatefy():
    time.sleep(1)
    ann.number("1")
    ann.scope(1)
    ann.ExpirationDate("10000-08-08")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs10 = driver.find_element_by_id("msg").text
    cs10 = cs10[0:3:1]
    if cs10 == "出错啦":
        print("输入10000-08-08测试成功")
    else:
        print("输入10000-08-08测试失败")

#月输入13,其他正常
def gdatefm():
    time.sleep(1)
    ann.number("1")
    ann.scope(1)
    ann.ExpirationDate("2008-13-08")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs11 = driver.find_element_by_id("msg").text
    cs11 = cs11[0:3:1]
    if cs11 == "出错啦":
        print("输入2008-13-08测试成功")
    else:
        print("输入2008-13-08测试失败")

#日输入32,其他正常
def gdatefd():
    time.sleep(1)
    ann.number("1")
    ann.scope(1)
    ann.ExpirationDate("2008-12-32")
    ann.HeadLine("刘露")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs12 = driver.find_element_by_id("msg").text
    cs12 = cs12[0:3:1]
    if cs12 == "出错啦":
        print("输入2008-12-32测试成功")
    else:
        print("输入2008-13-32测试失败")

#标题输入110字符
def btc():
    time.sleep(1)
    ann.number("1")
    ann.scope(1)
    ann.ExpirationDate("2008-08-08")
    for i in range(11):
        ann.HeadLine("哈哈哈哈哈哈哈哈哈哈")
    ann.Content("")
    time.sleep(1)
    ann.add()
    time.sleep(1)
    cs13 = driver.find_element_by_id("msg").text
    cs13 = cs13[0:3:1]
    if cs13 == "出错啦":
        print("输入110个字符测试成功")
    else:
        print("输入110个字符测试失败")

#编辑
def bj():
    ann.compile("aa")
    time.sleep(1)
    cs14 = driver.find_element_by_id("msg").text
    cs14 = cs14[0:3:1]
    if cs14 == "成功啦":
        print("编辑测试成功")
    else:
        print("编辑测试失败")


#搜索
def ss():
    time.sleep(2)
    ann.search("刘露")
    time.sleep(2)
    cs15 = driver.find_element_by_id("totalRecord").text
    time.sleep(1)
    print(cs15)
    if "1" == cs15:
        print("搜索测试成功")

    else:
        print("搜索测试失败")

#重置
def cz():
    time.sleep(1)
    ann.reset()
    time.sleep(1)
    cs16 = driver.find_element_by_id("headline").text
    if cs16 == "":
        print("重置测试成功")
    else:
        print("重置测试失败")

#删除
def sc1():
    time.sleep(1)
    ann.dele()
    time.sleep(1)
    cs17 = driver.find_element_by_id("msg").text
    cs17 = cs17[0:3:1]
    if cs17 == "成功啦":
        print("删除测试成功")
    else:
        print("删除测试失败")








if __name__ == '__main__':

    tadd()
    kbh()
    kcjz()
    date()
    kfw()
    kbt()
    knr()
    bhzm()
    ccjzf()
    gdatefd()
    gdatefm()
    gdatefy()
    btc()
    bj()
    ss()
    cz()
    sc1()
    driver.quit()