import json
from DDT.until import *
from DDT.common import *
import time
import requests

class TestWoniu:
    def __init__(self):
       self.file = "./woniu.xlsx"
       self.cookie = ""
       url = "http://localhost:8080/WoniuSales-20171128-V1.3-bin/user/login"
       body = {"username":"admin","password":"admin123","verifycode":"0000"}
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       session = requests.session()
       session.post(url = url,data = body,headers = headers)


    def login(self):
        #POST请求
        eo=ExcelOperaten(self.file)
        s_nrows = eo.get_nrows("login")
        com = common1()
        for i in range(1,s_nrows): #遍历每一行
            data=eo.get_excel_data("login",i)

            headers = json.loads(data[5])
            url=data[3]
            body = eo.myDict(data[7])
            method=data[4]
            if data[10].upper()=="Y":

                if method=="POST":
                   res = com.post(url,body,headers)
                   com.logincase(res,data)





    def add(self):
        eo=ExcelOperaten(self.file)
        s_nrows1 = eo.get_nrows("add")
        # print(s_nrows1)
        com = common1()
        for i in range(1,s_nrows1): #遍历每一行
                data=eo.get_excel_data("add",i)
                # print(data)
                headers =json.loads(data[5])
                # print(headers,type(headers))
                url=data[3]
                # body = eo.myDict(data[7])
                body=json.loads(data[7])
                # print(body,type(body))
                method=data[4]

                if data[10].upper()=="Y":

                    if method=="POST":
                       # sql = "select*from customer where customerphone=13333334"
                       # select = eo.select1(sql)
                       res = com.post(url,body,headers)
                       # print(select)

                       com.addcase(res,data)


                       # print(res)



    def logintime(self):

        time1 = time.time()
        self.login()

        time2 = time.time()
        time3 = time2-time1
        time4 = datetime.timedelta(seconds = time3)
        return time4

    def addtime(self):

        time1 = time.time()
        self.add()
        time2 = time.time()
        time3 = time2-time1
        time4 = datetime.timedelta(seconds = time3)
        return time4





if __name__ == '__main__':

    te = TestWoniu()
    te.login()
    # te.add()