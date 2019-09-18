from day04.cases.cases登陆 import logincase
from day04.cases.case编辑 import comcase
from day04.cases.case公告管理新增 import anncases
from day04.cases.case搜索 import recase
from day04.cases.case重置 import czcase
from day04.cases.case删除 import decase
import time

from day04.util.Rexcel import *


#start函数

def getDict(str):
    mydict = {}
    data = str.split("\n")
    for i in data:
        newdata = i.split("=")
        mydict[newdata[0]] = newdata[1]
    return mydict




# 获取excel数据

m = rexcel()
s = m.read("D:\\登陆.xlsx")
#获取sheet表的所有所有行数
for i in range(1,11):
    datalist = s.row_values(i) 
    module = datalist[2]#模块名
    funname = datalist[3]#功能
    testdatadict = getDict(datalist[4])#测试数据
    expected = datalist[5]#预期结果

    #登陆
    if module == "login":
       l = logincase()
       if funname == "login":
            driver = l.login(testdatadict["username"],testdatadict["password"],expected)
            time.sleep(2)
            l.driver.quit()

    # #新增
    # if module=="add":
    #     time.sleep(2)
    #     a = anncases()
    #     if funname == "add":
    #         driver = a.addcase1(testdatadict["num"],testdatadict["creator"],testdatadict["headline"],testdatadict["content"],expected)
    #         time.sleep(2)
    #         a.driver.quit()
    #
    # #编辑
    # if module=="compile":
    #     time.sleep(2)
    #     c = comcase()
    #     if funname == "compile":
    #         driver = c.com1(testdatadict["creator"],testdatadict["headline"],testdatadict["content"],expected)
    #         time.sleep(2)
    #         c.driver.quit()
    #
    #
    # #搜索
    # if module == "search":
    #     time.sleep(2)
    #     r = recase()
    #     print(funname)
    #     if funname == "search":
    #         driver = r.rec(testdatadict["headline"],expected)
    #         time.sleep(2)
    #         r.driver.quit()
    #
    # #重置
    # if module=="reset":
    #     time.sleep(2)
    #     c1 = czcase()
    #     if funname == "reset":
    #         driver = c1.cz11(expected)
    #         time.sleep(2)
    #         c1.driver.quit()
    #
    # #删除
    # if module=="delete":
    #     time.sleep(2)
    #     d = decase()
    #     if funname == "delete":
    #         driver = d.dete(expected)
    #         time.sleep(2)
    #         d.driver.quit()