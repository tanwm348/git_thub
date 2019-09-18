import threading
import requests
import time

class WoniuSales():

    def __init__(self):
       self.session = requests.session()



    #登陆
    def login(self):
        for i in range(50):
            url = "http://localhost:8080/WoniuSales-20171128-V1.3-bin/user/login"
            data = {"username":"admin","password":"admin123","verifycode":"0000"}
            res = self.session.post(url=url,data=data)
            if res.text == "login-pass":
                print("登陆测试成功")

            else:
                print("登陆测试失败")

    #查询
    def query(self):
        for i in range(50):
             url = "http://localhost:8080/WoniuSales-20171128-V1.3-bin/query/stored"
             data = {"goodsserial":"","goodsname":"","barcode":"","goodstype":"","earlystoretime":"","laststoretime":""}
             res = self.session.post(url=url,data=data)
             if "createtime" in res.text:
                 print("查询测试成功")

             else:
                 print("查询测试失败")




if __name__ == '__main__':
    wo = WoniuSales()
    #登陆线程
    t1 = time.time()
    for i in range(20):
        t = threading.Thread(target=wo.login)
        t.start()
        t.join()
    t2 = time.time()
    t3 = t2 - t1


    #查询线程
    t4 = time.time()
    for i in range(20):
        tt = threading.Thread(target=wo.query())
        tt.start()
        tt.join()
    t5 = time.time()
    t6 = t5 - t4
    print("登陆执行时间为:",t3)
    print("查询执行时间为:",t6)



