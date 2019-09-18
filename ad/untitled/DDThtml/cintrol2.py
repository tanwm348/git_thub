import json
from until1 import *
from common1 import *
import time
import random

class TestWoniu:
    def __init__(self):
       self.file = "./woniu.xlsx"




    def start(self):
        #POST请求
        eo=ExcelOperaten(self.file)
        sheet = eo.get_all_sheetnames()
        com = common1()
        #遍历页数
        for j in sheet:
            # 登陆
            if j == "login":
                s_nrows = eo.get_nrows("login")

                for i in range(1,s_nrows): #遍历每一行
                    #获取每一行的内容
                    data=eo.get_excel_data("login",i)

                    headers = json.loads(data[5])
                    url=data[3]
                    body=json.loads(data[7])
                    method=data[4]
                    if data[10].upper()=="Y":

                        if method=="POST":
                           cookie = ""
                           res = com.post(url,body,headers,cookie)

                           com.logincase(res,data)

            #简历编辑
            elif j == "compile":

                s_nrows1 = eo.get_nrows("compile")

                for i in range(1,s_nrows1): #遍历每一行
                    data=eo.get_excel_data("compile",i)

                    headers =json.loads(data[5])

                    url=data[3]
                    # body = eo.myDict(data[7])
                    body=json.loads(data[7])

                    method=data[4]

                    if data[10].upper()=="Y":

                        if method=="POST":
                           cookie = eo.login()
                           res = com.post(url,body,headers,cookie)

                           com.compilecase(res,data)


            #订阅
            elif j == "subscribe":

                s_nrows1 = eo.get_nrows("subscribe")

                for i in range(1,s_nrows1): #遍历每一行
                    data=eo.get_excel_data("subscribe",i)

                    headers =json.loads(data[5])

                    url=data[3]
                    # body = eo.myDict(data[7])

                    body=json.loads(data[7])

                    method=data[4]

                    if data[10].upper()=="Y":

                        if method=="POST":
                           cookie = eo.login()
                           email_ex = body["email"]
                           # print(data[9],type(data[9]))
                           # time.sleep(3)
                           email_sql = eo.select1(data[9])
                           res = com.post(url,body,headers,cookie)

                           com.subscribecase(res,data,email_ex,email_sql)


            #个人用户注册
            elif j == "registe_pu":
                s_nrows1 = eo.get_nrows("registe_pu")

                for i in range(1,s_nrows1): #遍历每一行
                    data=eo.get_excel_data("registe_pu",i)

                    headers =json.loads(data[5])

                    url=data[3]
                    # body = eo.myDict(data[7])
                    if "%s" in data[7]:
                       num = random.randint(1,1000000000)

                       body = json.loads(data[7]%(str(num)))
                       # print(body)

                    else:
                       body=json.loads(data[7])


                    method=data[4]

                    if data[10].upper()=="Y":

                        if method=="POST":
                           cookie = ""
                           # registe_sql = eo.select1(data[9])
                           res = com.post(url,body,headers,cookie)
                           com.registe_pucase(res,data)



            # 企业用户注册
            elif j == "registe_eu":
                s_nrows1 = eo.get_nrows("registe_eu")

                for i in range(1,s_nrows1): #遍历每一行
                    data=eo.get_excel_data("registe_eu",i)

                    headers =json.loads(data[5])

                    url=data[3]
                    # body = eo.myDict(data[7])
                    if "%s" in data[7]:
                       num = random.randint(1,1000000000)

                       body = json.loads(data[7]%(str(num),str(num)))
                       # print(body)

                    else:

                       body=json.loads(data[7])


                    method=data[4]

                    if data[10].upper()=="Y":

                        if method=="POST":
                           cookie = ""


                           # registe_sql = eo.select1(data[9])
                           res = com.post(url,body,headers,cookie)

                           com.registe_eucase(res,data)



    # def logintime(self):
    #
    #     time1 = time.time()
    #     self.start()
    #
    #     time2 = time.time()
    #     time3 = time2-time1
    #     time4 = datetime.timedelta(seconds = time3)
    #     return time4
    #
    # def addtime(self):
    #
    #     time1 = time.time()
    #     self.start()
    #     time2 = time.time()
    #     time3 = time2-time1
    #     time4 = datetime.timedelta(seconds = time3)
    #     return time4





if __name__ == '__main__':

    te = TestWoniu()
    te.start()
    # te.add()